#!/usr/bin/env python3
"""Install the shared personal AI workflow for Codex and Claude Code.

One source of truth lives in this repository:

  ai-workflow/WORKFLOW.md      shared working agreements both tools read
  skills/shared/<name>         generic skills, installed once into ~/.agents/skills
  skills/goal/<tool>/SKILL.md  the per-tool Goal workflow skill
  agents/<tool>/<file>         per-tool subagent role definitions
  entry/<tool>-<FILE>          the block merged into each tool's entry instructions

Claude Code sees the shared skills through symlinks into ~/.agents/skills, so a
shared method is edited in exactly one place. Every reference to WORKFLOW.md is
stored as the placeholder {{WORKFLOW_MD}} and rendered to an absolute path at
install time, which is what makes the repository portable between machines.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import shlex
import shutil
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]

TOKEN = "{{WORKFLOW_MD}}"
BEGIN = "<!-- BEGIN shared-ai-workflow -->"
END = "<!-- END shared-ai-workflow -->"

SHARED_SKILLS = (
    "test-driven-development",
    "diagnosing-bugs",
    "grill-me",
    "deslopify",
    "junior-to-senior",
    "last-20-percent",
)
CODEX_AGENTS = ("terra-worker.toml", "luna-worker.toml", "fresh-reviewer.toml")
# Definitions this setup used to install. An upgrade retires them instead of
# leaving a stale role behind for the tool to offer.
RETIRED_CODEX_AGENTS = ("solweaver-reviewer.toml",)
CLAUDE_AGENTS = ("sonnet-worker.md", "haiku-worker.md", "fresh-reviewer.md")

IGNORE = shutil.ignore_patterns("__pycache__", "*.py[co]", ".DS_Store")


class Plan:
    """An ordered, inspectable set of filesystem changes."""

    def __init__(self, home: Path, backup_root: Path, install_roots: tuple[Path, ...]) -> None:
        self.home = home
        self.backup_root = backup_root
        self.install_roots = install_roots
        self.copies: list[tuple[Path, Path, bool]] = []      # source, target, render
        self.trees: list[tuple[Path, Path]] = []             # source dir, target dir
        self.links: list[tuple[Path, Path]] = []             # link, target
        self.blocks: list[tuple[Path, str]] = []             # entry file, block body
        self.retire: list[Path] = []                         # paths to remove if present

    def targets(self) -> list[Path]:
        return (
            [target for _, target, _ in self.copies]
            + [target for _, target in self.trees]
            + [link for link, _ in self.links]
            + [path for path, _ in self.blocks]
            + list(self.retire)
        )

    def sources(self) -> list[Path]:
        return (
            [source for source, _, _ in self.copies]
            + [source for source, _ in self.trees]
        )


def paths_overlap(first: Path, second: Path) -> bool:
    """Lexical containment test.

    Deliberately does not follow symlinks: after a successful install the Claude
    skill links resolve onto the shared skill directories, and treating that as a
    write/write conflict would make every re-run fail.
    """
    first = Path(os.path.abspath(first))
    second = Path(os.path.abspath(second))
    return first == second or first in second.parents or second in first.parents


def render(text: str, workflow_md: Path) -> str:
    return text.replace(TOKEN, str(workflow_md))


def read_block(path: Path) -> str:
    body = path.read_text(encoding="utf-8").strip("\n")
    return f"{BEGIN}\n{body}\n{END}\n"


def merged_entry_text(existing: str | None, block: str) -> str:
    """Return the entry file content with exactly one managed block."""
    if existing is None:
        return block
    if BEGIN in existing and END in existing:
        head, _, rest = existing.partition(BEGIN)
        _, _, tail = rest.partition(END)
        return f"{head.rstrip()}\n\n{block}{tail.lstrip()}".strip("\n") + "\n"
    body = block[len(BEGIN) : -len(END) - 1].strip("\n")
    kept = existing.replace(body, "").strip("\n")
    return (f"{kept}\n\n{block}" if kept else block).strip("\n") + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--home",
        type=Path,
        default=Path.home(),
        help="Destination home directory (default: the current user's home).",
    )
    parser.add_argument("--workflow-dir", type=Path, default=None,
                        help="Shared workflow directory (default: <home>/.config/ai-workflow).")
    parser.add_argument("--shared-skills-dir", type=Path, default=None,
                        help="Shared skills directory (default: <home>/.agents/skills).")
    parser.add_argument("--codex-home", type=Path, default=None,
                        help="Codex configuration directory (default: <home>/.codex).")
    parser.add_argument("--claude-home", type=Path, default=None,
                        help="Claude Code configuration directory (default: <home>/.claude).")
    parser.add_argument("--upgrade", action="store_true",
                        help="Back up and replace anything that already exists and differs.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report the planned changes and write nothing.")
    return parser.parse_args(argv)


def build_plan(args: argparse.Namespace) -> tuple[Plan, Path, dict[str, Path]]:
    home = args.home.expanduser().resolve(strict=False)
    dirs = {
        "workflow": (args.workflow_dir or home / ".config/ai-workflow"),
        "shared": (args.shared_skills_dir or home / ".agents/skills"),
        "codex": (args.codex_home or home / ".codex"),
        "claude": (args.claude_home or home / ".claude"),
    }
    dirs = {key: path.expanduser().resolve(strict=False) for key, path in dirs.items()}
    workflow_md = dirs["workflow"] / "WORKFLOW.md"

    plan = Plan(home, dirs["workflow"] / "backups", tuple(dirs.values()))

    plan.copies.append((REPO_ROOT / "ai-workflow/WORKFLOW.md", workflow_md, False))
    plan.copies.append((REPO_ROOT / "scripts/test_global_setup.py",
                        dirs["workflow"] / "test_global_setup.py", False))

    for name in SHARED_SKILLS:
        plan.trees.append((REPO_ROOT / "skills/shared" / name, dirs["shared"] / name))
        plan.links.append((dirs["claude"] / "skills" / name, dirs["shared"] / name))

    plan.copies.append((REPO_ROOT / "skills/goal/codex/SKILL.md",
                        dirs["codex"] / "skills/goal/SKILL.md", True))
    plan.copies.append((REPO_ROOT / "skills/goal/claude/SKILL.md",
                        dirs["claude"] / "skills/goal/SKILL.md", True))

    for name in CODEX_AGENTS:
        plan.copies.append((REPO_ROOT / "agents/codex" / name,
                            dirs["codex"] / "agents" / name, True))
    for name in CLAUDE_AGENTS:
        plan.copies.append((REPO_ROOT / "agents/claude" / name,
                            dirs["claude"] / "agents" / name, True))

    for name in RETIRED_CODEX_AGENTS:
        plan.retire.append(dirs["codex"] / "agents" / name)

    plan.blocks.append((dirs["codex"] / "AGENTS.md", REPO_ROOT / "entry/codex-AGENTS.md"))
    plan.blocks.append((dirs["claude"] / "CLAUDE.md", REPO_ROOT / "entry/claude-CLAUDE.md"))

    return plan, workflow_md, dirs


def check_safety(plan: Plan) -> list[str]:
    problems = []
    missing = [source for source in plan.sources() if not source.exists()]
    missing += [source for _, source in plan.blocks if not source.exists()]
    for source in missing:
        problems.append(f"missing source: {source}")

    repo = REPO_ROOT.resolve(strict=False)
    for directory in plan.install_roots:
        resolved = directory.resolve(strict=False)
        if repo == resolved or resolved in repo.parents:
            problems.append(
                f"this repository lives inside an install directory: {repo} <-> {resolved}"
            )

    mutable = list(dict.fromkeys(plan.targets() + [plan.backup_root]))
    for source in plan.sources():
        for target in mutable:
            if paths_overlap(source, target):
                problems.append(f"source/write overlap: {source} <-> {target}")
    for index, first in enumerate(mutable):
        for second in mutable[index + 1 :]:
            if paths_overlap(first, second):
                problems.append(f"write/write overlap: {first} <-> {second}")
    return problems


def same_file(source: Path, target: Path, workflow_md: Path, do_render: bool) -> bool:
    if not target.is_file() or target.is_symlink():
        return False
    wanted = source.read_text(encoding="utf-8")
    if do_render:
        wanted = render(wanted, workflow_md)
    try:
        return target.read_text(encoding="utf-8") == wanted
    except UnicodeDecodeError:
        return False


def same_tree(source: Path, target: Path) -> bool:
    if not target.is_dir() or target.is_symlink():
        return False
    left = {p.relative_to(source): p for p in source.rglob("*")
            if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts}
    right = {p.relative_to(target): p for p in target.rglob("*")
             if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts}
    if set(left) != set(right):
        return False
    return all(left[key].read_bytes() == right[key].read_bytes() for key in left)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    plan, workflow_md, dirs = build_plan(args)

    problems = check_safety(plan)
    if problems:
        print("Refusing to install; resolve these first:")
        for problem in problems:
            print(f"  - {problem}")
        return 2

    conflicts: list[tuple[Path, str]] = []
    reusable: set[Path] = set()

    for source, target, do_render in plan.copies:
        if not target.exists() and not target.is_symlink():
            continue
        if same_file(source, target, workflow_md, do_render):
            reusable.add(target)
        else:
            conflicts.append((target, "file"))
    for source, target in plan.trees:
        if not target.exists() and not target.is_symlink():
            continue
        if same_tree(source, target):
            reusable.add(target)
        else:
            conflicts.append((target, "skill directory"))
    for link, target in plan.links:
        if not link.exists() and not link.is_symlink():
            continue
        if link.is_symlink() and link.resolve(strict=False) == target.resolve(strict=False):
            reusable.add(link)
        elif link.is_symlink():
            conflicts.append((link, "symlink pointing elsewhere"))
        else:
            conflicts.append((link, "REAL directory where a symlink belongs"))
    for path in plan.retire:
        if path.exists() or path.is_symlink():
            conflicts.append((path, "retired: removed, not replaced"))

    for entry, block_source in plan.blocks:
        if not entry.exists():
            continue
        wanted = merged_entry_text(entry.read_text(encoding="utf-8"),
                                   render(read_block(block_source), workflow_md))
        if entry.read_text(encoding="utf-8") == wanted:
            reusable.add(entry)
        else:
            conflicts.append((entry, "entry instructions"))

    if args.dry_run:
        print(f"Dry run against home {args.home}")
        print(f"  WORKFLOW.md -> {workflow_md}")
        for path, kind in conflicts:
            verb = "REMOVE " if kind.startswith("retired") else "REPLACE"
            print(f"  {verb}  {path}  ({kind})")
        for path in sorted(set(plan.targets()) - reusable - {p for p, _ in conflicts}):
            print(f"  CREATE   {path}")
        for path in sorted(reusable):
            print(f"  UNCHANGED {path}")
        if conflicts and not args.upgrade:
            print()
            print("Every REPLACE/REMOVE above needs --upgrade, which backs the path up to")
            print(f"{plan.backup_root} before replacing it.")
        return 0

    if conflicts and not args.upgrade:
        print("Refusing to overwrite existing paths:")
        for path, kind in conflicts:
            print(f"  - {path}  ({kind})")
        print()
        print("Rerun with --upgrade to back each one up before replacing it,")
        print(f"or inspect them first with --dry-run. Backups go to {plan.backup_root}.")
        return 1

    backup_root = plan.backup_root / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    def backup_destination(path: Path) -> Path:
        try:
            relative = path.relative_to(plan.home)
        except ValueError:
            relative = Path(path.as_posix().lstrip("/"))
        return backup_root / relative

    def back_up(path: Path) -> None:
        destination = backup_destination(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(path), str(destination))
        print(f"Backed up {path} -> {destination}")

    for path, _ in conflicts:
        if path in {entry for entry, _ in plan.blocks}:
            destination = backup_destination(path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
            print(f"Backed up {path} -> {destination}")
        else:
            back_up(path)

    for source, target, do_render in plan.copies:
        if target in reusable:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8")
        target.write_text(render(text, workflow_md) if do_render else text, encoding="utf-8")
        shutil.copystat(source, target)
        print(f"Installed {target}")

    for source, target in plan.trees:
        if target in reusable:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target, ignore=IGNORE)
        print(f"Installed {target}")

    for link, target in plan.links:
        if link in reusable:
            continue
        link.parent.mkdir(parents=True, exist_ok=True)
        link.symlink_to(target, target_is_directory=True)
        print(f"Linked {link} -> {target}")

    for entry, block_source in plan.blocks:
        if entry in reusable:
            continue
        entry.parent.mkdir(parents=True, exist_ok=True)
        existing = entry.read_text(encoding="utf-8") if entry.exists() else None
        block = render(read_block(block_source), workflow_md)
        entry.write_text(merged_entry_text(existing, block), encoding="utf-8")
        print(f"Merged managed block into {entry}")

    stale = []
    for source, target, do_render in plan.copies:
        if do_render and TOKEN in target.read_text(encoding="utf-8"):
            stale.append(target)
    for entry, _ in plan.blocks:
        if TOKEN in entry.read_text(encoding="utf-8"):
            stale.append(entry)
    if stale:
        print("Unrendered placeholders remain in:")
        for path in stale:
            print(f"  - {path}")
        return 3

    validator = shlex.join([sys.executable or "python3",
                            str(dirs["workflow"] / "test_global_setup.py"),
                            "--home", str(args.home.expanduser().resolve(strict=False)), "-v"])
    print()
    print(f"Shared workflow: {workflow_md}")
    print(f"Shared skills:   {dirs['shared']}  (Claude reads them through symlinks)")
    print("Next:")
    print(f"  1. Validate with: {validator}")
    print("  2. Restart Codex and start a new Claude Code session; both read")
    print("     instructions, agents and skills at session start.")
    print("  3. In a fresh session of each tool, ask it to list the instruction and")
    print("     skill paths it actually loaded. File checks cannot prove that.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
