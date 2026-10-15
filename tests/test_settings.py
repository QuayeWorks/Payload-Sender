import json
import tempfile
import unittest
from pathlib import Path

from payload_sender.settings import Profile, Settings, SettingsStore


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.store = SettingsStore(Path(self.temporary.name))

    def tearDown(self):
        self.temporary.cleanup()

    def test_roundtrip_profiles_theme_recents_and_history(self):
        settings = Settings([Profile("Main", "192.168.1.5", 9020, 5), Profile("Other", "::1", 9090, 10)],
                            1, "light", ["/path/file.bin"], [{"status": "Sent", "bytes": 100}])
        self.store.save(settings)
        self.assertEqual(self.store.load(), settings)
        self.assertEqual(list(self.store.directory.glob("*.tmp")), [])

    def test_corrupt_settings_fall_back_with_visible_warning(self):
        self.store.path.write_text("{invalid", encoding="utf-8")
        settings = self.store.load()
        self.assertEqual(settings.profiles, [Profile()])
        self.assertTrue(self.store.warning)

    def test_out_of_range_fields_are_recovered(self):
        self.store.path.write_text(json.dumps({"schema": 1, "active_profile": 999,
                                               "profiles": [{"port": -3, "timeout": 999}], "theme": "invalid"}), encoding="utf-8")
        settings = self.store.load()
        self.assertEqual(settings.active_profile, 0)
        self.assertEqual(settings.profiles[0].port, 9090)
        self.assertEqual(settings.profiles[0].timeout, 10)
        self.assertEqual(settings.theme, "dark")

    def test_failed_save_preserves_previous_settings(self):
        from unittest.mock import patch
        self.store.save(Settings(theme="dark"))
        with patch("payload_sender.settings.os.replace", side_effect=OSError("simulated write failure")):
            with self.assertRaises(OSError):
                self.store.save(Settings(theme="light"))
        self.assertEqual(self.store.load().theme, "dark")
        self.assertEqual(list(self.store.directory.glob("*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
