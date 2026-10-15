"""Versioned, atomic local preferences; no account or network service required."""

from __future__ import annotations

import json
import os
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path


def default_config_dir() -> Path:
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA", str(Path.home()))) / "QuayeWorks" / "PS4PayloadSender"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "QuayeWorks" / "PS4PayloadSender"
    return Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))) / "quayeworks" / "ps4-payload-sender"


@dataclass
class Profile:
    name: str = "My PS4"
    host: str = ""
    port: int = 9090
    timeout: float = 10.0


@dataclass
class Settings:
    profiles: list[Profile] = field(default_factory=lambda: [Profile()])
    active_profile: int = 0
    theme: str = "dark"
    recent_files: list[str] = field(default_factory=list)
    history: list[dict] = field(default_factory=list)


class SettingsStore:
    def __init__(self, directory: Path | None = None):
        self.directory = directory or default_config_dir()
        self.path = self.directory / "settings.json"
        self.warning = ""

    def load(self) -> Settings:
        if not self.path.exists():
            return Settings()
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("schema") != 1:
                raise ValueError("Unsupported settings format")
            profiles = []
            for item in data.get("profiles", [])[:50]:
                if not isinstance(item, dict):
                    continue
                name = str(item.get("name", "My PS4"))[:80].strip() or "My PS4"
                port = int(item.get("port", 9090))
                timeout = float(item.get("timeout", 10))
                profiles.append(Profile(name, str(item.get("host", ""))[:128],
                                        port if 1 <= port <= 65535 else 9090,
                                        timeout if 0.5 <= timeout <= 120 else 10))
            profiles = profiles or [Profile()]
            return Settings(
                profiles=profiles,
                active_profile=max(0, min(int(data.get("active_profile", 0)), len(profiles) - 1)),
                theme="light" if data.get("theme") == "light" else "dark",
                recent_files=[p for p in data.get("recent_files", []) if isinstance(p, str)][:8],
                history=[h for h in data.get("history", []) if isinstance(h, dict)][:30],
            )
        except (OSError, ValueError, TypeError, AttributeError, OverflowError) as exc:
            self.warning = f"Saved settings could not be loaded; defaults are in use ({exc})."
            return Settings()

    def save(self, settings: Settings) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        data = {"schema": 1, **asdict(settings)}
        temporary = None
        try:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=self.directory,
                                             prefix="settings-", suffix=".tmp", delete=False) as stream:
                temporary = Path(stream.name)
                json.dump(data, stream, indent=2, ensure_ascii=False, allow_nan=False)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, self.path)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
