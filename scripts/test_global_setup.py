"""Read-only checks for the installed personal AI configuration.

Independent of any repository: it inspects an installed home, not a checkout.
Pass --home to check a relocated or test installation, and --repo to also
confirm the installation still matches this repository's sources.

    python3 test_global_setup.py -v
    python3 test_global_setup.py --home /tmp/testhome --repo . -v

These checks prove files and links are in place. They cannot prove a tool
actually loaded them; do the fresh-session checks in README.md as well.
"""

import argparse
import hashlib
from pathlib import Path
import re
import unittest

import yaml

try:  # Python 3.11+
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - older interpreters
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:
        tomllib = None  # type: ignore[assignment]

SHARED_SKILLS = ('test-driven-development', 'diagnosing-bugs', 'grill-me', 'deslopify',
                 'junior-to-senior', 'last-20-percent')
CODEX_AGENTS = (('terra-worker.toml', 'terra_worker'),
                ('luna-worker.toml', 'luna_worker'),
                ('fresh-reviewer.toml', 'fresh_reviewer'))
RETIRED_CODEX_AGENTS = ('solweaver-reviewer.toml',)
CLAUDE_AGENTS = ('sonnet-worker', 'haiku-worker', 'fresh-reviewer')
TOKEN = '{{WORKFLOW_MD}}'

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--home', type=Path, default=Path.home(),
                    help='Installed home directory to check (default: this user).')
parser.add_argument('--repo', type=Path, default=None,
                    help='Repository checkout to compare the installation against.')
args, unittest_args = parser.parse_known_args()
ROOT = args.home.expanduser().resolve()
REPO = args.repo.expanduser().resolve() if args.repo else None
SHARED = ROOT / '.agents/skills'
WORKFLOW = ROOT / '.config/ai-workflow/WORKFLOW.md'


def frontmatter(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding='utf-8').split('---', 2)[1])


class GlobalSetupTests(unittest.TestCase):
    def test_shared_workflow_is_reachable_from_both_entry_files(self):
        self.assertTrue(WORKFLOW.is_file(), f'missing {WORKFLOW}')
        for relative in ('.codex/AGENTS.md', '.claude/CLAUDE.md'):
            with self.subTest(file=relative):
                text = (ROOT / relative).read_text(encoding='utf-8')
                self.assertIn(str(WORKFLOW), text,
                              'entry file does not point at the shared workflow')
        self.assertFalse((ROOT / '.codex/AGENTS.override.md').exists(),
                         'Global override masks the maintained AGENTS.md; review it explicitly.')

    def test_no_unrendered_placeholders(self):
        installed = [ROOT / '.codex/AGENTS.md', ROOT / '.claude/CLAUDE.md',
                     ROOT / '.codex/skills/goal/SKILL.md', ROOT / '.claude/skills/goal/SKILL.md']
        installed += [ROOT / '.codex/agents' / name for name, _ in CODEX_AGENTS]
        installed += [ROOT / '.claude/agents' / f'{role}.md' for role in CLAUDE_AGENTS]
        for path in installed:
            with self.subTest(file=path.name):
                self.assertNotIn(TOKEN, path.read_text(encoding='utf-8'),
                                 'install.py did not render the workflow path here')

    def test_shared_skill_metadata_and_local_references(self):
        for name in SHARED_SKILLS:
            path = SHARED / name / 'SKILL.md'
            with self.subTest(skill=name):
                content = path.read_text(encoding='utf-8')
                metadata = yaml.safe_load(content.split('---', 2)[1])
                self.assertEqual(metadata['name'], name)
                self.assertTrue(metadata['description'])
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
                    if not target.startswith(('http:', 'https:', '#')):
                        self.assertTrue((path.parent / target.split('#')[0]).exists(), target)

    def test_openai_skill_metadata(self):
        for name in SHARED_SKILLS:
            path = SHARED / name / 'agents/openai.yaml'
            if not path.exists():
                continue
            with self.subTest(skill=name):
                data = yaml.safe_load(path.read_text(encoding='utf-8'))
                self.assertIsInstance(data, dict)
                if 'interface' in data:
                    self.assertIsInstance(data['interface'], dict)
                    for key in ('display_name', 'short_description'):
                        self.assertIsInstance(data['interface'][key], str)
                        self.assertTrue(data['interface'][key].strip())
                if 'policy' in data:
                    self.assertIsInstance(data['policy'], dict)
                    if 'allow_implicit_invocation' in data['policy']:
                        self.assertIsInstance(data['policy']['allow_implicit_invocation'], bool)

    def test_claude_skill_links(self):
        for name in SHARED_SKILLS:
            path = ROOT / '.claude/skills' / name
            with self.subTest(skill=name):
                self.assertTrue(path.is_symlink(),
                                'Claude must read the shared skill, not a copy of it')
                self.assertEqual(path.resolve(strict=True), (SHARED / name).resolve(strict=True))

    def test_goal_integrations(self):
        for tool in ('.codex', '.claude'):
            path = ROOT / tool / 'skills/goal/SKILL.md'
            with self.subTest(tool=tool):
                metadata = frontmatter(path)
                self.assertEqual(metadata['name'], 'goal')
                self.assertTrue(metadata['description'])
                self.assertIn(str(WORKFLOW), path.read_text(encoding='utf-8'))

    def test_claude_agent_definitions(self):
        for role in CLAUDE_AGENTS:
            path = ROOT / '.claude/agents' / f'{role}.md'
            with self.subTest(agent=role):
                data = frontmatter(path)
                self.assertEqual(data['name'], role)
                self.assertIsInstance(data['description'], str)
                self.assertTrue(data['description'].strip())
                self.assertIsInstance(data['model'], str)
                self.assertTrue(data['model'].strip())
                self.assertIsInstance(data['tools'], str)
                tools = {tool.strip() for tool in data['tools'].split(',')}
                self.assertIn('Read', tools)
                if role == 'fresh-reviewer':
                    self.assertLessEqual(tools, {'Read', 'Grep', 'Glob', 'Bash'})

    @unittest.skipIf(tomllib is None, 'needs Python 3.11+ or tomli for TOML checks')
    def test_codex_agent_definitions(self):
        for filename, role in CODEX_AGENTS:
            with self.subTest(agent=role):
                data = tomllib.loads((ROOT / '.codex/agents' / filename).read_text(encoding='utf-8'))
                self.assertEqual(data['name'], role)
                self.assertTrue(data['developer_instructions'])
                if role == 'fresh_reviewer':
                    self.assertEqual(data['sandbox_mode'], 'read-only')

    @unittest.skipIf(tomllib is None, 'needs Python 3.11+ or tomli for TOML checks')
    def test_shared_skills_not_disabled(self):
        path = ROOT / '.codex/config.toml'
        config = tomllib.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
        maintained = {(SHARED / name / 'SKILL.md').resolve() for name in SHARED_SKILLS}
        for entry in config.get('skills', {}).get('config', []):
            if entry.get('enabled', True) is False:
                disabled = Path(entry['path']).expanduser().resolve()
                self.assertNotIn(disabled, maintained,
                                 'A maintained shared skill is disabled globally.')

    def test_retired_definitions_are_gone(self):
        """A role this setup no longer ships must not linger and be offered."""
        for name in RETIRED_CODEX_AGENTS:
            path = ROOT / '.codex/agents' / name
            with self.subTest(agent=name):
                self.assertFalse(path.exists(), f'retired definition still installed: {path}')

    def test_installed_provenance_digests(self):
        for name in SHARED_SKILLS:
            directory = SHARED / name
            provenance = (directory / 'UPSTREAM.md').read_text(encoding='utf-8')
            match = re.search(r'(?:Installed|Packaged) `SKILL\.md` SHA-256: `([a-f0-9]{64})`',
                              provenance)
            with self.subTest(skill=name):
                self.assertIsNotNone(match, 'Missing installed digest')
                self.assertEqual(match[1],
                                 hashlib.sha256((directory / 'SKILL.md').read_bytes()).hexdigest())
                self.assertTrue((directory / 'LICENSE').is_file())


@unittest.skipIf(REPO is None, 'pass --repo to compare the installation with its sources')
class RepositoryParityTests(unittest.TestCase):
    """The installation still matches the repository it came from."""

    def rendered(self, relative: str) -> str:
        return (REPO / relative).read_text(encoding='utf-8').replace(TOKEN, str(WORKFLOW))

    def test_shared_skills_match_repository(self):
        for name in SHARED_SKILLS:
            source = REPO / 'skills/shared' / name
            with self.subTest(skill=name):
                for path in sorted(source.rglob('*')):
                    if not path.is_file() or path.name == '.DS_Store':
                        continue
                    installed = SHARED / name / path.relative_to(source)
                    self.assertTrue(installed.is_file(), installed)
                    self.assertEqual(installed.read_bytes(), path.read_bytes())

    def test_rendered_files_match_repository(self):
        pairs = [('skills/goal/codex/SKILL.md', '.codex/skills/goal/SKILL.md'),
                 ('skills/goal/claude/SKILL.md', '.claude/skills/goal/SKILL.md'),
                 ('ai-workflow/WORKFLOW.md', '.config/ai-workflow/WORKFLOW.md')]
        pairs += [(f'agents/codex/{name}', f'.codex/agents/{name}') for name, _ in CODEX_AGENTS]
        pairs += [(f'agents/claude/{role}.md', f'.claude/agents/{role}.md')
                  for role in CLAUDE_AGENTS]
        for source, installed in pairs:
            with self.subTest(file=installed):
                self.assertEqual((ROOT / installed).read_text(encoding='utf-8'),
                                 self.rendered(source))

    def test_entry_blocks_present(self):
        for source, installed in (('entry/codex-AGENTS.md', '.codex/AGENTS.md'),
                                  ('entry/claude-CLAUDE.md', '.claude/CLAUDE.md')):
            with self.subTest(file=installed):
                body = self.rendered(source).strip('\n')
                self.assertIn(body, (ROOT / installed).read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main(argv=['test_global_setup.py', *unittest_args])
