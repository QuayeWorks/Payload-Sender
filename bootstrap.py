"""Set up an isolated environment, then launch or build the desktop app."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
PYTHON = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    if sys.version_info < (3, 10):
        print("Install Python 3.10 or newer from https://www.python.org/downloads/.")
        return 1
    try:
        if not PYTHON.is_file():
            print("Creating the app's Python environment…", flush=True)
            run([sys.executable, "-m", "venv", str(VENV)])
        requirements = ROOT / "requirements.txt"
        digest = hashlib.sha256(requirements.read_bytes()).hexdigest()
        marker = VENV / ".installed-requirements"
        installed = marker.read_text(encoding="utf-8").strip() if marker.exists() else ""
        check = subprocess.run([str(PYTHON), "-c", "from PySide6 import QtWidgets"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if installed != digest or check.returncode:
            print("Installing the desktop interface (internet is needed for the first setup)…", flush=True)
            run([str(PYTHON), "-m", "pip", "install", "-r", str(requirements)])
            marker.write_text(digest, encoding="utf-8")
        if "--build" in sys.argv[1:]:
            run([str(PYTHON), "-m", "pip", "install", "PyInstaller>=6.10,<7"])
            run([str(PYTHON), str(ROOT / "tools" / "build.py")])
            return 0
        return subprocess.call([str(PYTHON), str(ROOT / "main.py"), *sys.argv[1:]], cwd=ROOT)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"Setup did not complete: {exc}\nCheck your Python installation and internet connection.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
