"""Build a native folder distribution on the target operating system."""

from importlib.metadata import distribution
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "QuayeWorks-PS4-Payload-Sender"


def main() -> None:
    command = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean", "--onedir",
               "--name", NAME, "--paths", str(ROOT), "--distpath", str(ROOT / "dist"),
               "--workpath", str(ROOT / "build"), "--specpath", str(ROOT)]
    command += ["--add-data", f"{ROOT / 'assets'}:assets"]
    if sys.platform in ("win32", "darwin"):
        command.append("--windowed")
    if sys.platform == "win32":
        command += ["--icon", str(ROOT / "assets" / "app.ico")]
    command.append(str(ROOT / "main.py"))
    subprocess.run(command, cwd=ROOT, check=True)
    output = ROOT / "dist" / NAME
    output.mkdir(parents=True, exist_ok=True)
    for name in ("README.md", "LICENSE", "NOTICE.md"):
        shutil.copy2(ROOT / name, output / name)
    # Record actual dependency metadata and preserve any available license texts.
    dependencies = []
    for package in ("PySide6-Essentials", "shiboken6"):
        dependency = distribution(package)
        dependencies.append({"name": package, "version": dependency.version,
                             "license": dependency.metadata.get("License-Expression") or dependency.metadata.get("License")})
        for item in dependency.files or []:
            is_notice = "licenses" in item.parts or (
                ".dist-info" in str(item) and item.name.lower().startswith(("license", "copying", "notice")))
            if is_notice and dependency.locate_file(item).is_file():
                destination = output / "licenses" / package / item.name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(dependency.locate_file(item), destination)
    (output / "DEPENDENCIES.json").write_text(json.dumps(dependencies, indent=2) + "\n", encoding="utf-8")
    print(f"Built {output}")


if __name__ == "__main__":
    main()
