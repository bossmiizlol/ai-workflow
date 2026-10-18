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

SHARED_SKILLS = ('test-driven-development', 'diagnosing-bugs', 'grill-me', 'deslopify',
                 'junior-to-senior', 'last-20-percent', 'handoff',
                 'improve-codebase-architecture')
RETIRED_PATHS = ('.claude/skills/goal', '.claude/agents')
TOKEN = '{{WORKFLOW_MD}}'
DIR_TOKEN = '{{WORKFLOW_DIR}}'

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
ENTRY = ROOT / '.claude/CLAUDE.md'


def frontmatter(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding='utf-8').split('---', 2)[1])


class GlobalSetupTests(unittest.TestCase):
    def test_shared_workflow_is_reachable_from_the_entry_file(self):
        self.assertTrue(WORKFLOW.is_file(), f'missing {WORKFLOW}')
        self.assertIn(str(WORKFLOW), ENTRY.read_text(encoding='utf-8'),
                      'entry file does not point at the shared workflow')

    def test_no_unrendered_placeholders(self):
        text = ENTRY.read_text(encoding='utf-8')
        for token in (TOKEN, DIR_TOKEN):
            self.assertNotIn(token, text, 'install.py did not render the workflow path here')

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

    def test_claude_skill_links(self):
        for name in SHARED_SKILLS:
            path = ROOT / '.claude/skills' / name
            with self.subTest(skill=name):
                self.assertTrue(path.is_symlink(),
                                'Claude must read the shared skill, not a copy of it')
                self.assertEqual(path.resolve(strict=True), (SHARED / name).resolve(strict=True))

    def test_explicit_only_skills(self):
        for name in ('handoff', 'improve-codebase-architecture'):
            with self.subTest(skill=name):
                directory = SHARED / name
                self.assertIs(frontmatter(directory / 'SKILL.md')['disable-model-invocation'], True)

    def test_retired_definitions_are_gone(self):
        """A skill or role this setup no longer ships must not linger and be offered."""
        for relative in RETIRED_PATHS:
            path = ROOT / relative
            with self.subTest(path=relative):
                self.assertFalse(path.exists() or path.is_symlink(),
                                 f'retired definition still installed: {path}')

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
        return ((REPO / relative).read_text(encoding='utf-8')
                .replace(TOKEN, str(WORKFLOW)).replace(DIR_TOKEN, str(WORKFLOW.parent)))

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
        pairs = [('ai-workflow/WORKFLOW.md', '.config/ai-workflow/WORKFLOW.md'),
                 ('ai-workflow/pstack-compatibility.md',
                  '.config/ai-workflow/pstack-compatibility.md')]
        for source, installed in pairs:
            with self.subTest(file=installed):
                self.assertEqual((ROOT / installed).read_text(encoding='utf-8'),
                                 self.rendered(source))

    def test_entry_block_present(self):
        body = self.rendered('entry/claude-CLAUDE.md').strip('\n')
        self.assertIn(body, ENTRY.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main(argv=['test_global_setup.py', *unittest_args])
