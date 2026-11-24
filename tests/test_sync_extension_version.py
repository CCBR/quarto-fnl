"""Tests for DESCRIPTION-driven version synchronization."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / ".github/scripts/sync_extension_version.py"
SPEC = importlib.util.spec_from_file_location("sync_extension_version", SCRIPT)
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class SyncExtensionVersionTests(unittest.TestCase):
    """Cover release/development versions, stale manifests, and invalid inputs."""

    def test_release_and_development_versions(self):
        for source, expected in (("1.2.3", "1.2.3"), ("1.2.3.9000", "1.2.3-dev")):
            with self.subTest(source=source):
                self.assertEqual(sync.extension_version(f"Version: {source}\n"), expected)

    def test_invalid_description_versions(self):
        for description in (
            "",
            "Version: \n",
            "Version: 1.0.0\nVersion: 2.0.0\n",
            "Version: 01.0.0\n",
            "Version: 1.0.0.1\n",
            "Version: v1.0.0\n",
        ):
            with self.subTest(description=description):
                with self.assertRaises(ValueError):
                    sync.extension_version(description)

    def test_sync_and_check_both_extensions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            description = root / "DESCRIPTION"
            description.write_text("Package: quarto.fnl\nVersion: 2.3.4\n")
            manifests = []
            for name in sync.EXTENSION_NAMES:
                path = root / "_extensions" / name / "_extension.yml"
                path.parent.mkdir(parents=True)
                path.write_text(f"title: {name}\nversion: 1.0.0\ncontributes:\n  formats: {{}}\n")
                manifests.append(path)

            for version, expected in (("2.3.4", "2.3.4"), ("2.3.4.9000", "2.3.4-dev")):
                description.write_text(f"Package: quarto.fnl\nVersion: {version}\n")
                before = [path.read_text() for path in manifests]
                with self.assertRaisesRegex(ValueError, "fnl/.*fnl-report/"):
                    sync.sync_extensions(root, check=True)
                self.assertEqual([path.read_text() for path in manifests], before)
                sync.sync_extensions(root)
                for name, path in zip(sync.EXTENSION_NAMES, manifests):
                    self.assertEqual(
                        path.read_text(),
                        f"title: {name}\nversion: {expected}\ncontributes:\n  formats: {{}}\n",
                    )
                sync.sync_extensions(root, check=True)

            manifests[1].write_text(manifests[1].read_text().replace("2.3.4-dev", "1.0.0"))
            with self.assertRaisesRegex(ValueError, "fnl-report/"):
                sync.sync_extensions(root, check=True)

    def test_malformed_second_manifest_does_not_modify_first(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "DESCRIPTION").write_text("Version: 2.0.0\n")
            for name in sync.EXTENSION_NAMES:
                (root / "_extensions" / name).mkdir(parents=True)
            first = root / "_extensions/fnl/_extension.yml"
            second = root / "_extensions/fnl-report/_extension.yml"
            first.write_text("version: 1.0.0\n")
            for invalid in ("title: fnl-report\n", "version: 1.0.0\nversion: 2.0.0\n"):
                with self.subTest(invalid=invalid):
                    second.write_text(invalid)
                    with self.assertRaises(ValueError):
                        sync.sync_extensions(root)
                    self.assertEqual(first.read_text(), "version: 1.0.0\n")


if __name__ == "__main__":
    unittest.main()
