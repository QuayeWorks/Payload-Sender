# Complete project contents — QuayeWorks PS4 Payload Sender v1.0.0

Every text file is reproduced below in full. Binary assets are inventoried by byte count and SHA-256; their original bytes are included in the ZIP. This generated listing excludes itself.

## File inventory

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| .gitignore | 46 | `3a209ae003b71628e71981f6a00296c644864ee203d362e1b1e6cdd1e3170886` |
| Build_Windows.bat | 407 | `a7bfccf685751b2065e3d02c03f8fc8a3317906ca4e2328f09af0db5e5c332c6` |
| CONTENTS.json | 5436 | `c3cda82b646f81380eb54780dd21cd98dc3cb8b65a7c4b8ab3fc952748feaa0a` |
| LICENSE | 1067 | `da4b3c7eea95d1a5d37d5015e3bfe44c1252ee7af28a414cfb4730493c295b9d` |
| NOTICE.md | 1204 | `a678c8c39d5521b0af29ea38a4aff6c12921a1c1f7f9eb018d81a0d9b1f6bb85` |
| README.md | 8021 | `4eb5c60235d55ea57deedd35db4d1c4294a0631bc11e85033470aef75cfafcee` |
| Start_Windows.bat | 269 | `bfac4f00bf3df47c92fd085a525c4a928a77df32a03ab7760ff1b098dd324c94` |
| VALIDATION.md | 3836 | `2348ec0a13d2b187e6d4516c947f98ac02a57a25aaef5cf074b70da79fa3e1d9` |
| assets/app.ico | 24398 | `2a90314db7f53db57970caa10c9075a7d9e2abeb055d8ae5a694553335f561b0` |
| assets/app.png | 6167 | `0ef3d20fbd1b59928d1802446fac00b1f97ba0ecf59d298bb48717179da0d1e8` |
| assets/chevron-dark.png | 560 | `94d7510d1754b01d16dc8ed063a2d855fbb881044ac2ad7895a27b0efe4158be` |
| assets/chevron-light.png | 487 | `51fcbb5269f652b12cb83bf492755a3f2e989bb58c3dc9cb9775f42856a3ed86` |
| assets/up-dark.png | 552 | `8633f5194693eea09eaafbaa99a0d9d5ec378546bc507efb06d242a8ef346633` |
| assets/up-light.png | 496 | `1ef780bbddcad2a03e68fe59929b1fa9e7c2ec2c800f4e69540672465b76567f` |
| bootstrap.py | 2018 | `b5f47c976301e6657275e22fb85ab7a5c63ecae999dc7f43d84597dc046710d5` |
| main.py | 93 | `d1776a9dee522647322cf324ce15735b9d696193ffd0f64b2c3937981db689cd` |
| payload_sender/__init__.py | 60 | `40444fcf4040870ae241c0786802758346c667ea1705fb962437e307135d6e94` |
| payload_sender/__main__.py | 48 | `a67c172046323b0efcafe92cb83abc266d5dd4bc931d9312cde1b7bed50643db` |
| payload_sender/app.py | 3439 | `44fc9b3311f5dfdffcdcbce10d7d0a999c6963ef1bc7a8fd83ecf1ca5af61b27` |
| payload_sender/core.py | 10268 | `88171f67ce497b27a91078331218242e1185b35602f6f82ab8ce19abd10f723c` |
| payload_sender/gui.py | 33734 | `8bba24546bf765a2e22594207484dbc8b7c0b4f0f9ba52cc3b186a01ef27309d` |
| payload_sender/settings.py | 3640 | `3cca84567e81f1d4bc58b41db272b1686adc469eb8b9094979d19ccf262dcc5a` |
| payload_sender/theme.py | 10769 | `1fcd48f7b0bf9452600f79436ddb849fca1093a9e6ed6a10187120694c3e9ece` |
| payload_sender/workers.py | 1329 | `165de75bd48b36c611dd20e2deb7499778c0d7e9d625a6ef3910f8653334cd43` |
| requirements.txt | 27 | `e16dff7f823f0121441ae1e78e9b50b706a2635dfbbe7244e03d4395a11c067c` |
| screenshots/dark.png | 112169 | `1d5a8c4f42efca0a907346ed244862554cd57015ae0ddd98a1406dbb41c0bf6a` |
| screenshots/history.png | 120443 | `3913d4cc0e619de15dc783fca79823b463530301f6a0cd1914d535f595cc6087` |
| screenshots/light.png | 111801 | `c638e0f2d26813d71ec439320f20d6651fa9effb4d1734eb7b95ec1a988489cf` |
| screenshots/loopback-transfer.png | 134350 | `03e74a702d01d08c38b25ae68735c059274e62b022cff4627ab6d8df296d9c8f` |
| tests/__init__.py | 47 | `50b72835956b9932a1265b35315e8114b3ea577d8b5b7b813c891c5cf71b1104` |
| tests/support.py | 1856 | `6094ed872d76467605cbfc91470e3541ff5c7a5d6f93e7ccc96a661f53e5db4e` |
| tests/test_core.py | 10165 | `8c5b7d43e45c9bb5336cd03edea3fa0085355febef98d48de1e9ae1060925a3d` |
| tests/test_gui.py | 8147 | `dd9c0672d8e6501dab4a45e09e2e2cf1a0310f62b3c53d1d5b8136719142b8c3` |
| tests/test_settings.py | 2136 | `fcee993aabf17f2a94a320ac10cce7c2d4642d5006332f0c7df4855b4366a879` |
| tools/build.py | 2140 | `5309b5095268c51fba063d70654727b64ccb29a9378e5173c5e6b88d2570bd0e` |

## Complete text files

### .gitignore

````text
.venv/
__pycache__/
*.pyc
build/
dist/
*.spec
````

### Build_Windows.bat

````bat
@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 bootstrap.py --build
) else (
    python bootstrap.py --build
)
if errorlevel 1 (
    echo.
    echo Build failed. Read the message above.
) else (
    echo.
    echo The executable is in dist\QuayeWorks-PS4-Payload-Sender\.
    echo Keep the whole folder together when moving the app.
)
pause
endlocal
````

### CONTENTS.json

````json
{
  "project": "QuayeWorks PS4 Payload Sender",
  "version": "1.0.0",
  "tests_passed": 30,
  "note": "Hashes cover source and assets; this manifest and the generated complete-source listing exclude themselves.",
  "files": [
    {
      "path": ".gitignore",
      "bytes": 46,
      "sha256": "3a209ae003b71628e71981f6a00296c644864ee203d362e1b1e6cdd1e3170886"
    },
    {
      "path": "Build_Windows.bat",
      "bytes": 407,
      "sha256": "a7bfccf685751b2065e3d02c03f8fc8a3317906ca4e2328f09af0db5e5c332c6"
    },
    {
      "path": "LICENSE",
      "bytes": 1067,
      "sha256": "da4b3c7eea95d1a5d37d5015e3bfe44c1252ee7af28a414cfb4730493c295b9d"
    },
    {
      "path": "NOTICE.md",
      "bytes": 1204,
      "sha256": "a678c8c39d5521b0af29ea38a4aff6c12921a1c1f7f9eb018d81a0d9b1f6bb85"
    },
    {
      "path": "README.md",
      "bytes": 8021,
      "sha256": "4eb5c60235d55ea57deedd35db4d1c4294a0631bc11e85033470aef75cfafcee"
    },
    {
      "path": "Start_Windows.bat",
      "bytes": 269,
      "sha256": "bfac4f00bf3df47c92fd085a525c4a928a77df32a03ab7760ff1b098dd324c94"
    },
    {
      "path": "VALIDATION.md",
      "bytes": 3836,
      "sha256": "2348ec0a13d2b187e6d4516c947f98ac02a57a25aaef5cf074b70da79fa3e1d9"
    },
    {
      "path": "assets/app.ico",
      "bytes": 24398,
      "sha256": "2a90314db7f53db57970caa10c9075a7d9e2abeb055d8ae5a694553335f561b0"
    },
    {
      "path": "assets/app.png",
      "bytes": 6167,
      "sha256": "0ef3d20fbd1b59928d1802446fac00b1f97ba0ecf59d298bb48717179da0d1e8"
    },
    {
      "path": "assets/chevron-dark.png",
      "bytes": 560,
      "sha256": "94d7510d1754b01d16dc8ed063a2d855fbb881044ac2ad7895a27b0efe4158be"
    },
    {
      "path": "assets/chevron-light.png",
      "bytes": 487,
      "sha256": "51fcbb5269f652b12cb83bf492755a3f2e989bb58c3dc9cb9775f42856a3ed86"
    },
    {
      "path": "assets/up-dark.png",
      "bytes": 552,
      "sha256": "8633f5194693eea09eaafbaa99a0d9d5ec378546bc507efb06d242a8ef346633"
    },
    {
      "path": "assets/up-light.png",
      "bytes": 496,
      "sha256": "1ef780bbddcad2a03e68fe59929b1fa9e7c2ec2c800f4e69540672465b76567f"
    },
    {
      "path": "bootstrap.py",
      "bytes": 2018,
      "sha256": "b5f47c976301e6657275e22fb85ab7a5c63ecae999dc7f43d84597dc046710d5"
    },
    {
      "path": "main.py",
      "bytes": 93,
      "sha256": "d1776a9dee522647322cf324ce15735b9d696193ffd0f64b2c3937981db689cd"
    },
    {
      "path": "payload_sender/__init__.py",
      "bytes": 60,
      "sha256": "40444fcf4040870ae241c0786802758346c667ea1705fb962437e307135d6e94"
    },
    {
      "path": "payload_sender/__main__.py",
      "bytes": 48,
      "sha256": "a67c172046323b0efcafe92cb83abc266d5dd4bc931d9312cde1b7bed50643db"
    },
    {
      "path": "payload_sender/app.py",
      "bytes": 3439,
      "sha256": "44fc9b3311f5dfdffcdcbce10d7d0a999c6963ef1bc7a8fd83ecf1ca5af61b27"
    },
    {
      "path": "payload_sender/core.py",
      "bytes": 10268,
      "sha256": "88171f67ce497b27a91078331218242e1185b35602f6f82ab8ce19abd10f723c"
    },
    {
      "path": "payload_sender/gui.py",
      "bytes": 33734,
      "sha256": "8bba24546bf765a2e22594207484dbc8b7c0b4f0f9ba52cc3b186a01ef27309d"
    },
    {
      "path": "payload_sender/settings.py",
      "bytes": 3640,
      "sha256": "3cca84567e81f1d4bc58b41db272b1686adc469eb8b9094979d19ccf262dcc5a"
    },
    {
      "path": "payload_sender/theme.py",
      "bytes": 10769,
      "sha256": "1fcd48f7b0bf9452600f79436ddb849fca1093a9e6ed6a10187120694c3e9ece"
    },
    {
      "path": "payload_sender/workers.py",
      "bytes": 1329,
      "sha256": "165de75bd48b36c611dd20e2deb7499778c0d7e9d625a6ef3910f8653334cd43"
    },
    {
      "path": "requirements.txt",
      "bytes": 27,
      "sha256": "e16dff7f823f0121441ae1e78e9b50b706a2635dfbbe7244e03d4395a11c067c"
    },
    {
      "path": "screenshots/dark.png",
      "bytes": 112169,
      "sha256": "1d5a8c4f42efca0a907346ed244862554cd57015ae0ddd98a1406dbb41c0bf6a"
    },
    {
      "path": "screenshots/history.png",
      "bytes": 120443,
      "sha256": "3913d4cc0e619de15dc783fca79823b463530301f6a0cd1914d535f595cc6087"
    },
    {
      "path": "screenshots/light.png",
      "bytes": 111801,
      "sha256": "c638e0f2d26813d71ec439320f20d6651fa9effb4d1734eb7b95ec1a988489cf"
    },
    {
      "path": "screenshots/loopback-transfer.png",
      "bytes": 134350,
      "sha256": "03e74a702d01d08c38b25ae68735c059274e62b022cff4627ab6d8df296d9c8f"
    },
    {
      "path": "tests/__init__.py",
      "bytes": 47,
      "sha256": "50b72835956b9932a1265b35315e8114b3ea577d8b5b7b813c891c5cf71b1104"
    },
    {
      "path": "tests/support.py",
      "bytes": 1856,
      "sha256": "6094ed872d76467605cbfc91470e3541ff5c7a5d6f93e7ccc96a661f53e5db4e"
    },
    {
      "path": "tests/test_core.py",
      "bytes": 10165,
      "sha256": "8c5b7d43e45c9bb5336cd03edea3fa0085355febef98d48de1e9ae1060925a3d"
    },
    {
      "path": "tests/test_gui.py",
      "bytes": 8147,
      "sha256": "dd9c0672d8e6501dab4a45e09e2e2cf1a0310f62b3c53d1d5b8136719142b8c3"
    },
    {
      "path": "tests/test_settings.py",
      "bytes": 2136,
      "sha256": "fcee993aabf17f2a94a320ac10cce7c2d4642d5006332f0c7df4855b4366a879"
    },
    {
      "path": "tools/build.py",
      "bytes": 2140,
      "sha256": "5309b5095268c51fba063d70654727b64ccb29a9378e5173c5e6b88d2570bd0e"
    }
  ]
}
````

### LICENSE

````text
MIT License

Copyright (c) 2026 QuayeWorks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

### NOTICE.md

````markdown
# Notices

This independently written Python application recreates the raw TCP sender workflow of the supplied C# project. The supplied project credits valentinbreiz and HIASQ. Original reference: https://github.com/valentinbreiz/PS4-Payload-Sender

The MIT license in this project covers the newly written application source, tests, documentation, and locally drawn interface assets. It does not relicense the referenced C# project, Qt, Python, or any console payload.

The desktop UI depends on PySide6-Essentials and shiboken6 from The Qt Company. The tested packages declare `LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only` in their metadata. They and their bundled third-party components retain their own licensing. The build script records dependency metadata and copies available dependency license texts into the distribution's `licenses` directory. The tested wheels do not ship separate license-text files, so the official license references below remain relevant for redistribution.

Python and PyInstaller retain their own licenses. Official references:

- https://doc.qt.io/qtforpython-6/licenses.html
- https://docs.python.org/3/license.html
- https://pyinstaller.org/en/stable/license.html
````

### README.md

````markdown
# QuayeWorks PS4 Payload Sender

A complete Python rewrite of the attached C# sender, with a native Qt desktop interface and the same raw TCP payload protocol.

![Dark desktop interface](screenshots/dark.png)

## Start on Windows

1. Install **Python 3.10 or newer** from [python.org](https://www.python.org/downloads/). Enable **Add Python to PATH** during installation.
2. Extract the entire project ZIP into a writable folder.
3. Double-click **Start_Windows.bat**.

The launcher creates a local `.venv` and installs the pinned Qt dependency on first use. That first setup needs internet access. Later launches reuse the environment.

The ZIP contains the complete Python source and launch scripts. It does **not** contain a prebuilt Windows executable.

## Send a payload

1. Enable the BIN loader on your PS4. Connect the PC and PS4 to the same network.
2. Enter the PS4's IP address and the port shown by your loader. The **GoldHEN BIN Loader** preset uses **9090**, as documented by [GoldHEN](https://github.com/GoldHEN/GoldHEN#features).
3. Browse or drag in one `.bin` or `.elf` file that your loader and console firmware support.
4. Click **Send payload**, then verify the result on the console.

Each Send opens one fresh TCP connection and transmits the file bytes, without a header or filename. The write side is shut down after transmission to signal EOF. A separate connection test is unnecessary; a probe can consume a connection on a one-shot loader.

**Transfer complete means the sender submitted all bytes to TCP.** The raw loader protocol does not provide a payload-execution acknowledgement or a remote checksum. Console execution and firmware compatibility require verification on the PS4.

The 9020 preset is an editable raw TCP alternative. Use it only if your loader actually listens on that port. `.elf` is an accepted file extension, not a promise that every BIN loader can execute ELF files.

## Improvements

| Area | Attached C# sender | Python rewrite |
| --- | --- | --- |
| Interface | Fixed WinForms window; main handlers unwired in the supplied designer | Resizable native Qt UI, dark/light themes, smaller-window scrolling |
| Connection | Manual connect before sending | Connect automatically on each explicit Send |
| Responsiveness | File send and connect run on the UI thread | Background inspection and transfer workers |
| Transfer feedback | Success/error message boxes | Progress, byte count, speed, elapsed time, and inline errors |
| Timeout | Send/receive timeout set, but blocking Connect has no explicit deadline | Cancellable connect deadline and send-stall timeout |
| Files | Browse for one BIN file | Browse, drag-and-drop, BIN/ELF selection, eight recent files |
| Integrity | No displayed file checksum | Local SHA-256; verified snapshot prevents source edits changing transmitted bytes |
| Preferences | Hardcoded initial address and port | Up to 50 saved console profiles and persistent theme |
| Diagnostics | Generic dialogs | Session log, clipboard/export, and last 30 transfer outcomes |
| Automation | GUI only | Standard-library CLI with optional JSON output |

Cancellation checks run during preparation, connection waits, and send waits. Partial socket writes are handled explicitly. Payloads over 8 MiB spill their transfer snapshot to a temporary file rather than loading the whole payload into memory. Temporary snapshots close on success, cancellation, or failure.

The app does not automatically retry a payload: a retry after a partial send could submit it twice. Check the console and reset/re-enable the loader if necessary before manually sending again.

## Shortcuts

| Shortcut | Action |
| --- | --- |
| Ctrl+O | Browse for a payload |
| Ctrl+Enter | Send the selected payload |
| Esc | Cancel the current operation |
| Ctrl+L | Clear the current session log |

## Linux and macOS

```bash
python3 bootstrap.py
```

The Python code and Qt UI support these platforms. The automated tests and visual checks in this delivery ran on Linux; Windows and macOS have not been hardware-tested here. Linux desktop systems may need their normal Qt/XCB system libraries.

To use an existing Python environment:

```bash
python -m pip install -r requirements.txt
python main.py
```

## Command line

The CLI uses only the Python standard library; Qt is not required.

```bash
python main.py --cli --host 192.168.1.100 --port 9090 payload.bin
python main.py --cli --json --host 192.168.1.100 --timeout 10 payload.bin
python -m payload_sender --version
```

Pass a literal IPv4 or IPv6 address. DNS hostnames are deliberately excluded so a resolver cannot hold up cancellation. Press Ctrl+C to cancel. Exit codes are `0` for all bytes submitted, `1` for a transfer error, `2` for invalid CLI usage, and `130` for cancellation. JSON success includes `execution_confirmed: false`; failures include the phase and submitted byte count.

You can also preselect a file in the GUI:

```bash
python main.py payload.bin --host 192.168.1.100 --port 9090
```

## Build a Windows executable

On Windows, double-click **Build_Windows.bat**. It installs PyInstaller in the app's environment and creates:

```text
dist/QuayeWorks-PS4-Payload-Sender/QuayeWorks-PS4-Payload-Sender.exe
```

Keep the **whole distribution folder** together when moving it to another PC. It includes Python, Qt, assets, dependency metadata, and notices; the receiving PC does not need Python installed.

Build on the target operating system. [PyInstaller is not a cross-compiler](https://pyinstaller.org/en/stable/operating-mode.html), so this Linux session does not produce a Windows EXE. The build command is provided; a Windows build and launch remain to be verified.

## Settings and logs

Profiles, theme, recent-file paths, and transfer history are saved locally in `settings.json`:

| Platform | Folder |
| --- | --- |
| Windows | `%APPDATA%\QuayeWorks\PS4PayloadSender` |
| macOS | `~/Library/Application Support/QuayeWorks/PS4PayloadSender` |
| Linux | `$XDG_CONFIG_HOME/quayeworks/ps4-payload-sender`, or `~/.config/quayeworks/ps4-payload-sender` |

Use `--config-dir PATH` to select another desktop settings folder. Writes are atomic; unreadable/corrupt settings fall back to defaults with a log message. The session log retains up to 500 lines in memory; use **Export log** to save it. **Clear** clears the session log, not the saved transfer history. No account, telemetry, discovery scan, or background console connection is used.

## Troubleshooting

| Message or behavior | What to check |
| --- | --- |
| Send button disabled | Select a readable, nonempty payload and enter a valid literal IP address |
| Connection refused | BIN loader enabled; correct IP and loader port |
| Connection timed out | PS4 reachable on the same network; correct IP; firewall/network isolation |
| Transfer stalled or partially canceled | Check the console and reset the loader before manually resending |
| File changed | Select it again so its current content is inspected |
| All bytes sent, but no console result | Correct payload for the firmware and loader; execution cannot be confirmed by this protocol |

## Tests and source

```bash
python -m unittest discover -v
```

Transport/settings tests require only standard Python. GUI tests require `requirements.txt` and use Qt's offscreen platform. `VALIDATION.md` records the actual delivery checks and remaining hardware limits.

The archive includes all application code, tests, icons, launch/build scripts, screenshots, and `COMPLETE_PROJECT_CONTENTS.md`. That Markdown file reproduces every text source file in full and inventories binary assets by size and SHA-256.

## Credits

Recreated from the functionality of the supplied `PS4-Payload-Sender-main.zip`. Original sender: **valentinbreiz**. Supplied C# fork credits **HIASQ**. The Python implementation is a fresh rewrite; it does not include the old executables, C# source, or console payload binaries.

See `LICENSE` for the new Python code and `NOTICE.md` for dependency notices.
````

### Start_Windows.bat

````bat
@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 bootstrap.py %*
) else (
    python bootstrap.py %*
)
if errorlevel 1 (
    echo.
    echo The application could not start. Read the message above.
    pause
)
endlocal
````

### VALIDATION.md

````markdown
# Delivery validation — v1.0.0

## Result

**30 automated tests passed.** The Python desktop app and raw TCP transport were verified on this host. No PS4 hardware connection was made.

Test environment: Linux x86-64, Python 3.12.14, PySide6-Essentials 6.12.0, Qt offscreen platform. Native packaging used PyInstaller 6.22.3.

## Automated checks

| Area | Checks |
| --- | --- |
| Raw TCP transport | Exact binary bytes and EOF, partial writes, IPv4/IPv6 loopback, snapshot spilling to disk |
| Payload integrity | SHA-256, immutable transmission after source edits, stale selected-file rejection before connection |
| Input validation | Missing/empty/unsupported files, BIN/ELF extensions, invalid address/port/timeout |
| Connection lifecycle | Refusal diagnostics, pending-connect cancellation, connect deadline, socket cleanup |
| Cancellation and stalls | Cancellation before connection and during send, exact partial byte counts, stalled receiver timeout |
| CLI | Real JSON success through loopback, execution-confirmation field false, nonzero error exit |
| Desktop workflow | Actual file inspection/send/history, control states, drag-and-drop, unsupported file feedback |
| Desktop responsiveness | UI timer continues during a stalled transfer, cancellation works, window close safely cancels the worker |
| Desktop preferences | Theme persistence, loader/port synchronization, profile saving, checksum/log clipboard |
| Layout | Numeric input text has usable space; small windows scroll; clear-file resets metrics |
| Settings | Roundtrip, corrupt-file recovery, range recovery, failed atomic replacement preserves prior preferences |

The 30-test suite completed in 1.437 seconds. After replacing a deprecated Qt drag-event constructor with its current equivalent, the affected drag-and-drop test passed again. Source compilation and CLI help/version checks also passed.

## Native packaging smoke test

`tools/build.py` successfully created a Linux folder distribution. The resulting executable passed:

- Version output (`1.0.0`).
- An exact 1 MiB binary transfer to a local TCP receiver through its bundled CLI.
- Offscreen GUI startup with the bundled Qt libraries and icon assets.

The Linux packaging log reported that this host lacks the XCB cursor system library (`libxcb-cursor.so.0`). This did not affect offscreen checks. A Linux desktop launch with the XCB platform remains dependent on the host's normal Qt/XCB system packages. This is not a Windows dependency.

The source ZIP excludes this host's Linux build output and downloaded runtime packages. Windows launch/build scripts are included. A Windows EXE must be built and verified on Windows.

## Visual inspection

The actual application was rendered and inspected in dark and light themes at 1120×940, plus a smaller 980×720 layout with scrolling. File controls, SHA-256 display, transfer metrics, session log, and history were inspected.

Included screenshots:

- `screenshots/dark.png`: actual empty app, dark theme.
- `screenshots/light.png`: actual empty app, light theme.
- `screenshots/loopback-transfer.png`: an actual 256 KiB transfer of synthetic test bytes to `127.0.0.1`.
- `screenshots/history.png`: that local test transfer in history.

The loopback screenshots demonstrate the interface and sender behavior. They do not demonstrate a console payload running or a PS4 transfer speed. No executable console payload is included.

## Remaining verification

- Launch the source app or build the EXE on the user's Windows PC.
- Enable the actual PS4 BIN loader, enter its IP/port, send a compatible payload, and confirm console execution.

The application uses the same raw file-byte TCP protocol as the attached C# sender. Loader/firmware compatibility and console execution are not established by host simulation or a completed socket send.
````

### bootstrap.py

````python
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
````

### main.py

````python
from payload_sender.app import main

if __name__ == "__main__":
    raise SystemExit(main())
````

### payload_sender/__init__.py

````python
"""QuayeWorks PS4 Payload Sender."""

__version__ = "1.0.0"
````

### payload_sender/__main__.py

````python
from .app import main

raise SystemExit(main())
````

### payload_sender/app.py

````python
"""Desktop and command-line entry points. CLI use needs only standard Python."""

from __future__ import annotations

import argparse
import json
import signal
import sys
import time
from pathlib import Path
from threading import Event

from . import __version__
from .core import Endpoint, OperationCancelled, TransferError, format_bytes, transfer_payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="QuayeWorks PS4 Payload Sender")
    parser.add_argument("payload", nargs="?", type=Path, help="A .bin or .elf payload")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--cli", action="store_true", help="Send without the desktop interface")
    parser.add_argument("--host", help="Console IPv4 or IPv6 address (required for CLI)")
    parser.add_argument("--port", type=int, default=9090, help="Loader port (default: 9090)")
    parser.add_argument("--timeout", type=float, default=10, help="Connect/stall timeout in seconds")
    parser.add_argument("--json", action="store_true", help="CLI: print a machine-readable result")
    parser.add_argument("--config-dir", type=Path, help="Override the desktop settings directory")
    args = parser.parse_args(argv)
    if args.cli:
        if args.payload is None or not args.host:
            parser.error("--cli requires --host and a payload path")
        cancel = Event()
        previous = signal.signal(signal.SIGINT, lambda *_: cancel.set())
        last = 0.0

        def progress(event):
            nonlocal last
            now = time.monotonic()
            if not args.json and (now - last > 0.1 or event.phase == "complete"):
                print(f"\r{event.phase.title():12} {format_bytes(event.completed)} / "
                      f"{format_bytes(event.total)}          ", end="", file=sys.stderr, flush=True)
                last = now

        try:
            result = transfer_payload(args.payload, Endpoint(args.host, args.port, args.timeout), cancel, progress)
            data = {"status": "sent", "destination": result.endpoint.display, "bytes_sent": result.bytes_sent,
                    "sha256": result.payload.sha256, "seconds": round(result.elapsed, 6),
                    "execution_confirmed": False}
            print(json.dumps(data) if args.json else
                  f"\nSent {format_bytes(result.bytes_sent)} to {result.endpoint.display}. "
                  "Verify payload execution on the console.")
            return 0
        except TransferError as exc:
            data = {"status": "canceled" if isinstance(exc, OperationCancelled) else "error",
                    "message": str(exc), "phase": exc.phase, "bytes_sent": exc.bytes_sent}
            print(json.dumps(data) if args.json else f"\n{exc}",
                  file=sys.stdout if args.json else sys.stderr)
            return 130 if isinstance(exc, OperationCancelled) else 1
        finally:
            signal.signal(signal.SIGINT, previous)
    if args.json:
        parser.error("--json is available only with --cli")
    try:
        from .gui import run_gui
    except ImportError as exc:
        print(f"The desktop interface needs PySide6-Essentials. Run Start_Windows.bat or "
              f"python bootstrap.py to set it up.\nDetails: {exc}", file=sys.stderr)
        return 1
    return run_gui(args.config_dir, args.payload, args.host, args.port, args.timeout)
````

### payload_sender/core.py

````python
"""Cancellable raw-TCP transfer. This module has no GUI dependencies."""

from __future__ import annotations

import errno
import hashlib
import ipaddress
import os
import select
import socket
import stat
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from threading import Event
from typing import BinaryIO, Callable

CHUNK_SIZE = 64 * 1024
SPOOL_MEMORY_LIMIT = 8 * 1024 * 1024
SUPPORTED_SUFFIXES = {".bin", ".elf"}


class TransferError(Exception):
    def __init__(self, message: str, phase: str = "preparing", bytes_sent: int = 0):
        super().__init__(message)
        self.phase = phase
        self.bytes_sent = bytes_sent


class OperationCancelled(TransferError):
    pass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int = 9090
    timeout: float = 10.0

    def validate(self) -> "Endpoint":
        try:
            address = ipaddress.ip_address(self.host.strip())
        except ValueError as exc:
            raise TransferError("Enter the console's IPv4 or IPv6 address, such as 192.168.1.100.") from exc
        if isinstance(self.port, bool) or not isinstance(self.port, int) or not 1 <= self.port <= 65535:
            raise TransferError("The port must be a number between 1 and 65535.")
        if not 0.5 <= self.timeout <= 120:
            raise TransferError("The timeout must be between 0.5 and 120 seconds.")
        return Endpoint(str(address), self.port, float(self.timeout))

    @property
    def display(self) -> str:
        host = f"[{self.host}]" if ":" in self.host else self.host
        return f"{host}:{self.port}"


@dataclass(frozen=True)
class PayloadInfo:
    path: Path
    size: int
    sha256: str
    modified_ns: int


@dataclass(frozen=True)
class TransferUpdate:
    phase: str
    completed: int
    total: int
    elapsed: float = 0.0


@dataclass(frozen=True)
class TransferResult:
    payload: PayloadInfo
    endpoint: Endpoint
    bytes_sent: int
    elapsed: float

    @property
    def speed(self) -> float:
        return self.bytes_sent / max(self.elapsed, 0.000001)


UpdateCallback = Callable[[TransferUpdate], None]


def format_bytes(value: float) -> str:
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if abs(value) < 1024 or unit == "TiB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.2f} {unit}"
        value /= 1024
    return "0 B"


def _check_cancel(cancel: Event, phase: str, sent: int = 0) -> None:
    if cancel.is_set():
        message = "Canceled before any payload bytes were sent."
        if sent:
            message = f"Canceled after {format_bytes(sent)} were submitted to TCP. Check the console before resending."
        raise OperationCancelled(message, phase, sent)


def _read_payload(
    path: Path, cancel: Event, update: UpdateCallback, snapshot: BinaryIO | None = None
) -> PayloadInfo:
    path = path.expanduser().resolve()
    if path.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise TransferError("Choose a .bin or .elf payload supported by your console's loader.")
    if not path.is_file():
        raise TransferError("The selected payload must be an existing regular file.")
    _check_cancel(cancel, "preparing")
    with path.open("rb") as source:
        before = os.fstat(source.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise TransferError("The selected payload must be a regular file.")
        if before.st_size == 0:
            raise TransferError("The selected payload is empty.")
        digest = hashlib.sha256()
        read = 0
        last_update = 0.0
        update(TransferUpdate("preparing", 0, before.st_size))
        while chunk := source.read(CHUNK_SIZE):
            _check_cancel(cancel, "preparing")
            digest.update(chunk)
            if snapshot is not None:
                snapshot.write(chunk)
            read += len(chunk)
            now = time.monotonic()
            if now - last_update >= 0.05:
                update(TransferUpdate("preparing", read, before.st_size))
                last_update = now
        after = os.fstat(source.fileno())
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns) or read != before.st_size:
            raise TransferError("The payload changed while it was being read. Select it again.")
    _check_cancel(cancel, "preparing")
    update(TransferUpdate("preparing", read, read))
    return PayloadInfo(path, read, digest.hexdigest(), after.st_mtime_ns)


def inspect_payload(
    path: Path | str, cancel: Event | None = None, update: UpdateCallback | None = None
) -> PayloadInfo:
    try:
        return _read_payload(Path(path), cancel or Event(), update or (lambda event: None))
    except (OSError, ValueError) as exc:
        raise TransferError(f"Cannot read the payload: {exc}") from exc


def _connect(endpoint: Endpoint, cancel: Event) -> socket.socket:
    family = socket.AF_INET6 if ":" in endpoint.host else socket.AF_INET
    sock = socket.socket(family, socket.SOCK_STREAM)
    try:
        sock.setblocking(False)
        # Literal addresses avoid an unbounded DNS lookup and keep cancellation responsive.
        result = sock.connect_ex((endpoint.host, endpoint.port))
        pending = {errno.EINPROGRESS, errno.EWOULDBLOCK, errno.EALREADY, 10035, 10036, 10037}
        if result not in pending | {0, errno.EISCONN}:
            raise OSError(result, os.strerror(result))
        deadline = time.monotonic() + endpoint.timeout
        while result not in (0, errno.EISCONN):
            _check_cancel(cancel, "connecting")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("Connection timed out")
            _, writable, exceptional = select.select([], [sock], [sock], min(0.1, remaining))
            if writable or exceptional:
                result = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
                if result:
                    raise OSError(result, os.strerror(result))
        _check_cancel(cancel, "connecting")
        return sock
    except BaseException:
        sock.close()
        raise


def transfer_payload(
    path: Path | str,
    endpoint: Endpoint,
    cancel: Event | None = None,
    update: UpdateCallback | None = None,
    expected: PayloadInfo | None = None,
) -> TransferResult:
    """Send the exact file bytes and EOF, with no header, retry, or execution claim.

    A bounded-memory snapshot guarantees that the displayed/verified hash describes
    the bytes transmitted, even if the original file is edited during a transfer.
    The timeout applies to connecting and to each period without send progress.
    """
    endpoint = endpoint.validate()
    cancel = cancel or Event()
    update = update or (lambda event: None)
    sent = 0
    phase = "preparing"
    try:
        with tempfile.SpooledTemporaryFile(max_size=SPOOL_MEMORY_LIMIT, mode="w+b") as snapshot:
            info = _read_payload(Path(path), cancel, update, snapshot)
            if expected is not None and (info.path, info.size, info.sha256) != (
                expected.path, expected.size, expected.sha256
            ):
                raise TransferError("The selected file changed. Select it again before sending.")
            snapshot.seek(0)
            phase = "connecting"
            update(TransferUpdate(phase, 0, info.size))
            with _connect(endpoint, cancel) as sock:
                phase = "sending"
                started = last_activity = time.monotonic()
                last_update = 0.0
                update(TransferUpdate(phase, 0, info.size))
                while chunk := snapshot.read(CHUNK_SIZE):
                    view = memoryview(chunk)
                    while view:
                        _check_cancel(cancel, phase, sent)
                        remaining = endpoint.timeout - (time.monotonic() - last_activity)
                        if remaining <= 0:
                            raise TimeoutError("The receiver stopped accepting data")
                        _, writable, exceptional = select.select([], [sock], [sock], min(0.1, remaining))
                        if exceptional:
                            raise ConnectionError("The receiver closed the connection")
                        if not writable:
                            continue
                        try:
                            count = sock.send(view)
                        except (BlockingIOError, InterruptedError):
                            continue
                        if count == 0:
                            raise ConnectionError("The receiver closed the connection")
                        view = view[count:]
                        sent += count
                        last_activity = time.monotonic()
                        if last_activity - last_update >= 0.05:
                            update(TransferUpdate(phase, sent, info.size, last_activity - started))
                            last_update = last_activity
                _check_cancel(cancel, phase, sent)
                # EOF is how raw loaders learn that the payload is complete.
                sock.shutdown(socket.SHUT_WR)
                elapsed = max(time.monotonic() - started, 0.000001)
                update(TransferUpdate("complete", sent, info.size, elapsed))
                return TransferResult(info, endpoint, sent, elapsed)
    except TransferError:
        raise
    except TimeoutError as exc:
        detail = "Check the IP, loader port, and whether the BIN loader is enabled."
        if phase == "sending":
            detail = "The transfer stalled. Check the console before manually resending."
        raise TransferError(f"{exc}. {detail}", phase, sent) from exc
    except ConnectionRefusedError as exc:
        raise TransferError(
            f"{endpoint.display} refused the connection. Enable the BIN loader and check its port.", phase, sent
        ) from exc
    except (OSError, ValueError) as exc:
        message = f"Transfer failed during {phase}: {exc}"
        if sent:
            message += f". {format_bytes(sent)} were submitted to TCP; check the console before resending."
        raise TransferError(message, phase, sent) from exc
````

### payload_sender/gui.py

````python
"""Native desktop UI; all file inspection and networking run outside the UI thread."""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt, QTimer, Signal, Slot
from PySide6.QtGui import QCloseEvent, QDragEnterEvent, QDropEvent, QFont, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox, QFileDialog, QFrame,
    QHBoxLayout, QHeaderView, QInputDialog, QLabel, QLineEdit, QMainWindow, QMenu,
    QMessageBox, QPlainTextEdit, QProgressBar, QPushButton, QScrollArea, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget,
)

from . import __version__
from .core import Endpoint, OperationCancelled, PayloadInfo, TransferError, TransferResult, TransferUpdate, format_bytes
from .settings import Profile, SettingsStore
from .theme import apply_theme, colors, make_icon
from .workers import PayloadWorker


def label(text: str, role: str = "", name: str = "") -> QLabel:
    widget = QLabel(text)
    widget.setTextFormat(Qt.TextFormat.PlainText)
    if role:
        widget.setProperty("role", role)
    if name:
        widget.setObjectName(name)
    return widget


def button(text: str, name: str = "") -> QPushButton:
    widget = QPushButton(text)
    widget.setCursor(Qt.CursorShape.PointingHandCursor)
    if name:
        widget.setObjectName(name)
    return widget


def rule() -> QFrame:
    widget = QFrame()
    widget.setObjectName("Rule")
    widget.setFixedHeight(1)
    return widget


class DropArea(QFrame):
    selected = Signal(object)

    def __init__(self):
        super().__init__()
        self.setObjectName("DropArea")
        self.setAcceptDrops(True)
        self.setProperty("dragging", False)
        self.setMinimumHeight(152)

    def _highlight(self, active: bool):
        self.setProperty("dragging", active)
        self.style().unpolish(self)
        self.style().polish(self)

    def dragEnterEvent(self, event: QDragEnterEvent):
        urls = event.mimeData().urls()
        if self.isEnabled() and len(urls) == 1 and urls[0].isLocalFile():
            self._highlight(True)
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self._highlight(False)
        event.accept()

    def dropEvent(self, event: QDropEvent):
        self._highlight(False)
        urls = event.mimeData().urls()
        if self.isEnabled() and len(urls) == 1 and urls[0].isLocalFile():
            self.selected.emit(Path(urls[0].toLocalFile()))
            event.acceptProposedAction()


class ContentRoot(QWidget):
    def heightForWidth(self, width: int) -> int:
        # Scroll only when the actual minimum layout no longer fits the window.
        return self.layout().minimumHeightForWidth(width)


class MainWindow(QMainWindow):
    def __init__(self, store: SettingsStore | None = None):
        super().__init__()
        self.store = store or SettingsStore()
        self.settings = self.store.load()
        self.payload: PayloadInfo | None = None
        self.worker: PayloadWorker | None = None
        self.job_kind = ""
        self.pending_path: Path | None = None
        self.last_phase = ""
        self.closing = False
        self.log_lines: list[str] = []
        self.setWindowTitle(f"QuayeWorks · PS4 Payload Sender {__version__}")
        self.resize(1120, 940)
        self.setMinimumSize(980, 720)
        self._build()
        self._load_profiles()
        self._apply_theme()
        self._refresh_history()
        self._refresh()
        self._log("READY", "Choose a payload and enter your console's IP address.")
        if self.store.warning:
            self._log("SETTINGS", self.store.warning)
        for sequence, handler in [("Ctrl+O", self.browse), ("Ctrl+Return", self.start_send),
                                  ("Escape", self.cancel_job), ("Ctrl+L", self.clear_log)]:
            shortcut = QShortcut(QKeySequence(sequence), self)
            shortcut.activated.connect(handler)

    def _build(self):
        root = ContentRoot()
        root.setObjectName("Root")
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setWidget(root)
        self.setCentralWidget(scroll)
        outer = QVBoxLayout(root)
        outer.setContentsMargins(28, 22, 28, 18)
        outer.setSpacing(20)

        top = QHBoxLayout()
        tile = label("QW", name="BrandTile")
        tile.setFixedSize(44, 44)
        tile.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top.addWidget(tile)
        brand = QVBoxLayout()
        brand.setSpacing(2)
        brand.addWidget(label("QuayeWorks", name="Brand"))
        brand.addWidget(label("CONSOLE TOOLS", "eyebrow"))
        top.addLayout(brand)
        top.addStretch()
        self.theme_button = button("Light mode")
        self.theme_button.clicked.connect(self.toggle_theme)
        self.help_button = button("Quick start")
        self.help_button.clicked.connect(self.show_help)
        top.addWidget(self.theme_button)
        top.addWidget(self.help_button)
        outer.addLayout(top)

        heading = QHBoxLayout()
        titles = QVBoxLayout()
        titles.setSpacing(5)
        titles.addWidget(label("PS4 Payload Sender", name="PageTitle"))
        titles.addWidget(label("Your payload. Your console. One clean transfer.", "muted"))
        heading.addLayout(titles)
        heading.addStretch()
        self.status = label("●  IDLE", name="Status")
        self.status.setProperty("state", "idle")
        heading.addWidget(self.status, alignment=Qt.AlignmentFlag.AlignVCenter)
        outer.addLayout(heading)

        body = QHBoxLayout()
        body.setSpacing(20)
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(286)
        side = QVBoxLayout(sidebar)
        side.setContentsMargins(20, 20, 20, 18)
        side.setSpacing(8)
        side.addWidget(label("01  /  DESTINATION", "eyebrow"))
        side.addWidget(label("Your console", "heading"))
        side.addSpacing(4)
        side.addWidget(label("SAVED PROFILE", "eyebrow"))
        self.profile_combo = QComboBox()
        self.profile_combo.setAccessibleName("Console profile")
        self.profile_combo.setMinimumContentsLength(12)
        self.profile_combo.currentIndexChanged.connect(self.profile_changed)
        side.addWidget(self.profile_combo)
        profile_actions = QHBoxLayout()
        profile_actions.setSpacing(4)
        self.save_profile_button = button("Save", "Link")
        self.add_profile_button = button("Add", "Link")
        self.delete_profile_button = button("Delete", "Link")
        self.save_profile_button.clicked.connect(self.save_profile)
        self.add_profile_button.clicked.connect(self.add_profile)
        self.delete_profile_button.clicked.connect(self.delete_profile)
        for item in (self.save_profile_button, self.add_profile_button, self.delete_profile_button):
            profile_actions.addWidget(item)
        profile_actions.addStretch()
        side.addLayout(profile_actions)
        side.addWidget(rule())
        side.addWidget(label("CONSOLE IP ADDRESS", "eyebrow"))
        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("192.168.1.100")
        self.host_input.setAccessibleName("Console IP address")
        self.host_input.setMaxLength(128)
        self.host_input.textChanged.connect(self._refresh)
        side.addWidget(self.host_input)
        side.addWidget(label("LOADER", "eyebrow"))
        self.loader_combo = QComboBox()
        self.loader_combo.addItems(["GoldHEN BIN Loader", "Raw TCP · port 9020", "Custom port"])
        self.loader_combo.setAccessibleName("Loader preset")
        self.loader_combo.currentIndexChanged.connect(self.loader_changed)
        side.addWidget(self.loader_combo)
        limits = QHBoxLayout()
        for title, widget in [("PORT", QSpinBox()), ("TIMEOUT", QDoubleSpinBox())]:
            column = QVBoxLayout()
            column.setSpacing(7)
            column.addWidget(label(title, "eyebrow"))
            column.addWidget(widget)
            limits.addLayout(column)
            if title == "PORT":
                self.port_input = widget
                widget.setRange(1, 65535)
                widget.setValue(9090)
                widget.setAccessibleName("Loader port")
                widget.valueChanged.connect(self.port_changed)
            else:
                self.timeout_input = widget
                widget.setRange(0.5, 120)
                widget.setDecimals(1)
                widget.setSingleStep(0.5)
                widget.setSuffix(" s")
                widget.setValue(10)
                widget.setAccessibleName("Connect and stall timeout")
        side.addLayout(limits)
        side.addStretch(1)
        hint = QFrame()
        hint.setObjectName("Hint")
        hints = QVBoxLayout(hint)
        hints.setContentsMargins(12, 10, 12, 10)
        text = label("Enable your PS4's BIN loader.\nKeep both devices on the same network.", "muted")
        text.setWordWrap(True)
        hints.addWidget(text)
        side.addWidget(hint)
        body.addWidget(sidebar)

        right = QVBoxLayout()
        right.setSpacing(16)
        payload_panel = QFrame()
        payload_panel.setObjectName("Panel")
        payload_layout = QVBoxLayout(payload_panel)
        payload_layout.setContentsMargins(22, 20, 22, 20)
        payload_layout.setSpacing(14)
        payload_heading = QHBoxLayout()
        payload_heading.addWidget(label("02  /  PAYLOAD", "eyebrow"))
        payload_heading.addStretch()
        payload_heading.addWidget(label("BIN  /  ELF", "eyebrow"))
        payload_layout.addLayout(payload_heading)
        self.drop_area = DropArea()
        self.drop_area.selected.connect(self.select_file)
        drop = QVBoxLayout(self.drop_area)
        drop.setContentsMargins(18, 18, 18, 18)
        drop.setSpacing(8)
        file_row = QHBoxLayout()
        file_row.setSpacing(16)
        self.file_symbol = label("", name="FileSymbol")
        self.file_symbol.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_symbol.setFixedSize(56, 60)
        file_row.addWidget(self.file_symbol)
        names = QVBoxLayout()
        names.setSpacing(5)
        self.file_name = label("Drop a payload here", name="FileName")
        self.file_name.setWordWrap(True)
        self.file_name.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        self.file_detail = label("Choose a .bin or .elf file to get started.", "muted")
        self.file_detail.setWordWrap(True)
        names.addWidget(self.file_name)
        names.addWidget(self.file_detail)
        file_row.addLayout(names, 1)
        drop.addLayout(file_row)
        browse_row = QHBoxLayout()
        self.browse_button = button("Browse files")
        self.browse_button.clicked.connect(self.browse)
        self.recent_button = button("Recent files", "Link")
        self.recent_button.clicked.connect(self.show_recent)
        self.clear_file_button = button("Remove", "Link")
        self.clear_file_button.clicked.connect(self.clear_file)
        browse_row.addWidget(self.browse_button)
        browse_row.addWidget(self.recent_button)
        browse_row.addStretch()
        browse_row.addWidget(self.clear_file_button)
        drop.addLayout(browse_row)
        payload_layout.addWidget(self.drop_area)
        hash_row = QHBoxLayout()
        hash_row.addWidget(label("SHA-256", "eyebrow"))
        self.hash_label = label("Calculated locally when you select a file", "muted")
        self.hash_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.hash_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        hash_row.addWidget(self.hash_label, 1)
        self.copy_hash_button = button("Copy", "Link")
        self.copy_hash_button.clicked.connect(self.copy_hash)
        hash_row.addWidget(self.copy_hash_button)
        payload_layout.addLayout(hash_row)
        right.addWidget(payload_panel)

        transfer_panel = QFrame()
        transfer_panel.setObjectName("Panel")
        transfer = QVBoxLayout(transfer_panel)
        transfer.setContentsMargins(22, 20, 22, 20)
        transfer.setSpacing(12)
        transfer.addWidget(label("03  /  TRANSFER", "eyebrow"))
        transfer_row = QHBoxLayout()
        self.stage_label = label("Ready when you are", name="Stage")
        self.percent_label = label("0%", name="Percent")
        transfer_row.addWidget(self.stage_label)
        transfer_row.addStretch()
        transfer_row.addWidget(self.percent_label)
        transfer.addLayout(transfer_row)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 1000)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setAccessibleName("Payload transfer progress")
        transfer.addWidget(self.progress_bar)
        stats = QHBoxLayout()
        self.bytes_label = label("0 B / 0 B", "muted")
        self.speed_label = label("— / s", "muted")
        self.elapsed_label = label("0.0 s", "muted")
        stats.addWidget(self.bytes_label)
        stats.addStretch()
        stats.addWidget(self.speed_label)
        stats.addSpacing(20)
        stats.addWidget(self.elapsed_label)
        transfer.addLayout(stats)
        self.feedback = label("A connection opens when you send.", name="Feedback")
        self.feedback.setWordWrap(True)
        self.feedback.setMinimumHeight(31)
        transfer.addWidget(self.feedback)
        actions = QHBoxLayout()
        self.send_button = button("Send payload", "Primary")
        self.send_button.clicked.connect(self.start_send)
        self.cancel_button = button("Cancel", "Danger")
        self.cancel_button.clicked.connect(self.cancel_job)
        actions.addWidget(self.send_button, 1)
        actions.addWidget(self.cancel_button)
        transfer.addLayout(actions)
        right.addWidget(transfer_panel)
        body.addLayout(right, 1)
        outer.addLayout(body)

        activity_panel = QFrame()
        activity_panel.setObjectName("Panel")
        activity = QVBoxLayout(activity_panel)
        activity.setContentsMargins(16, 10, 16, 14)
        activity.setSpacing(8)
        tabs_row = QHBoxLayout()
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBar().setDrawBase(False)
        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)
        self.log_view.setMaximumBlockCount(500)
        self.log_view.setAccessibleName("Activity log")
        self.history_table = QTableWidget(0, 5)
        self.history_table.setHorizontalHeaderLabels(["PAYLOAD", "DESTINATION", "SIZE", "RESULT", "TIME"])
        self.history_table.verticalHeader().hide()
        self.history_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.history_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.history_table.setShowGrid(False)
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tabs.addTab(self.log_view, "Activity")
        self.tabs.addTab(self.history_table, "Transfer history")
        tabs_row.addWidget(label("SESSION", "eyebrow"))
        tabs_row.addStretch()
        self.copy_log_button = button("Copy log", "Link")
        self.export_button = button("Export log", "Link")
        self.clear_log_button = button("Clear", "Link")
        self.copy_log_button.clicked.connect(self.copy_log)
        self.export_button.clicked.connect(self.export_log)
        self.clear_log_button.clicked.connect(self.clear_log)
        for item in (self.copy_log_button, self.export_button, self.clear_log_button):
            tabs_row.addWidget(item)
        activity.addLayout(tabs_row)
        activity.addWidget(self.tabs)
        activity_panel.setMinimumHeight(160)
        outer.addWidget(activity_panel, 1)
        footer = QHBoxLayout()
        footer.addWidget(label("LOCAL TCP  ·  NO ACCOUNT REQUIRED", "eyebrow"))
        footer.addStretch()
        footer.addWidget(label(f"PYTHON + QT  /  v{__version__}", "eyebrow"))
        outer.addLayout(footer)

    def _apply_theme(self):
        apply_theme(QApplication.instance(), self.settings.theme)
        c = colors(self.settings.theme)
        self.setWindowIcon(make_icon("brand", c["accent"], 64))
        self.file_symbol.setPixmap(make_icon("file", c["accent"], 32).pixmap(32, 32))
        self.send_button.setIcon(make_icon("send", c["accent_text"]))
        self.browse_button.setIcon(make_icon("folder", c["text"]))
        self.theme_button.setIcon(make_icon("theme", c["muted"]))
        self.theme_button.setText("Dark mode" if self.settings.theme == "light" else "Light mode")
        self.cancel_button.setIcon(make_icon("close", c["danger"], 16))

    def toggle_theme(self):
        self.settings.theme = "light" if self.settings.theme == "dark" else "dark"
        self._apply_theme()
        self._persist()

    def _persist(self):
        try:
            self.store.save(self.settings)
        except (OSError, ValueError) as exc:
            self._log("SETTINGS", f"Preferences could not be saved: {exc}")

    def _load_profiles(self):
        self.profile_combo.blockSignals(True)
        self.profile_combo.clear()
        self.profile_combo.addItems([p.name for p in self.settings.profiles])
        self.profile_combo.setCurrentIndex(self.settings.active_profile)
        self.profile_combo.blockSignals(False)
        self.profile_changed(self.settings.active_profile)

    def profile_changed(self, index: int):
        if not 0 <= index < len(self.settings.profiles):
            return
        self.settings.active_profile = index
        profile = self.settings.profiles[index]
        self.host_input.setText(profile.host)
        self.port_input.setValue(profile.port)
        self.port_changed(profile.port)
        self.timeout_input.setValue(profile.timeout)
        self._refresh()

    def loader_changed(self, index: int):
        if index in (0, 1):
            self.port_input.setValue(9090 if index == 0 else 9020)

    def port_changed(self, value: int):
        self.loader_combo.blockSignals(True)
        self.loader_combo.setCurrentIndex(0 if value == 9090 else 1 if value == 9020 else 2)
        self.loader_combo.blockSignals(False)

    def _endpoint(self) -> Endpoint:
        return Endpoint(self.host_input.text(), self.port_input.value(), self.timeout_input.value()).validate()

    def save_profile(self):
        if self.worker:
            return
        try:
            endpoint = self._endpoint()
        except TransferError as exc:
            self._feedback(str(exc), "error")
            return
        self._save_endpoint(endpoint)
        self._log("PROFILE", f"Saved {self.profile_combo.currentText()} · {endpoint.display}")
        self._feedback("Console profile saved.")

    def _save_endpoint(self, endpoint: Endpoint):
        profile = self.settings.profiles[self.settings.active_profile]
        profile.host, profile.port, profile.timeout = endpoint.host, endpoint.port, endpoint.timeout
        self._persist()

    def add_profile(self):
        if self.worker or len(self.settings.profiles) >= 50:
            return
        name, accepted = QInputDialog.getText(self, "Add console", "Profile name:", text="Another PS4")
        if accepted and name.strip():
            self.settings.profiles.append(Profile(name.strip()[:80]))
            self.settings.active_profile = len(self.settings.profiles) - 1
            self._load_profiles()
            self._persist()

    def delete_profile(self):
        if self.worker or len(self.settings.profiles) <= 1:
            return
        self.settings.profiles.pop(self.settings.active_profile)
        self.settings.active_profile = 0
        self._load_profiles()
        self._persist()

    def _refresh(self, *_):
        busy = self.worker is not None
        for widget in (self.host_input, self.port_input, self.timeout_input, self.profile_combo,
                       self.loader_combo, self.save_profile_button, self.add_profile_button):
            widget.setEnabled(not busy)
        self.delete_profile_button.setEnabled(not busy and len(self.settings.profiles) > 1)
        self.drop_area.setEnabled(not busy)
        self.clear_file_button.setEnabled(not busy and self.payload is not None)
        self.copy_hash_button.setEnabled(self.payload is not None)
        self.recent_button.setEnabled(not busy and bool(self.settings.recent_files))
        self.cancel_button.setEnabled(busy and not self.worker.cancel_event.is_set())
        try:
            self._endpoint()
            valid = True
        except TransferError:
            valid = False
        self.send_button.setEnabled(not busy and valid and self.payload is not None)
        self.send_button.setToolTip("Send the selected file (Ctrl+Enter)" if valid else "Enter a valid console IP address first")
        if not busy:
            self.send_button.setText("Send payload")

    def _badge(self, state: str, text: str):
        self.status.setText("●  " + text.upper())
        self.status.setProperty("state", state)
        self.status.style().unpolish(self.status)
        self.status.style().polish(self.status)

    def _feedback(self, text: str, state: str = ""):
        self.feedback.setText(text)
        self.feedback.setProperty("state", state)
        self.feedback.style().unpolish(self.feedback)
        self.feedback.style().polish(self.feedback)

    def _log(self, level: str, text: str):
        line = f"{datetime.now():%H:%M:%S}  {level:<8} {text}"
        self.log_lines.append(line)
        self.log_lines = self.log_lines[-500:]
        self.log_view.appendPlainText(line)

    def browse(self):
        if self.worker:
            return
        directory = str(self.payload.path.parent) if self.payload else ""
        path, _ = QFileDialog.getOpenFileName(self, "Choose a PS4 payload", directory,
                                            "Payloads (*.bin *.BIN *.elf *.ELF)")
        if path:
            self.select_file(Path(path))

    @Slot(object)
    def select_file(self, path: Path):
        if self.worker:
            return
        self.payload = None
        self.pending_path = Path(path)
        self.file_name.setText(self.pending_path.name)
        self.file_detail.setText("Inspecting file and calculating SHA-256…")
        self.hash_label.setText("Calculating…")
        self._feedback("Reading your file locally.")
        self._start_worker(PayloadWorker(self.pending_path, parent=self), "inspect")

    def _start_worker(self, worker: PayloadWorker, kind: str):
        self.worker = worker
        self.job_kind = kind
        self.last_phase = ""
        self.progress_bar.setValue(0)
        self.percent_label.setText("0%")
        self.elapsed_label.setText("0.0 s")
        self.speed_label.setText("— / s")
        worker.progress.connect(self.progress_changed)
        worker.inspected.connect(self.inspection_finished)
        worker.transferred.connect(self.transfer_finished)
        worker.failed.connect(self.job_failed)
        worker.finished.connect(self.worker_stopped)
        self._refresh()
        worker.start()

    @Slot(object)
    def inspection_finished(self, info: PayloadInfo):
        self.payload = info
        self.file_name.setText(info.path.name)
        self.file_name.setToolTip(str(info.path))
        self.file_detail.setText(f"{format_bytes(info.size)}  ·  {info.path.suffix[1:].upper()} payload")
        self.hash_label.setText(info.sha256[:24] + "…")
        self.hash_label.setToolTip(info.sha256)
        self.progress_bar.setValue(0)
        self.percent_label.setText("0%")
        self.bytes_label.setText(f"0 B / {format_bytes(info.size)}")
        self.stage_label.setText("Ready to send")
        self._badge("ready", "Payload ready")
        self._feedback("Payload inspected. Enable your loader, then send.")
        path = str(info.path)
        self.settings.recent_files = [path] + [p for p in self.settings.recent_files if p != path][:7]
        self._persist()
        self._log("FILE", f"{info.path.name} · {format_bytes(info.size)} · SHA-256 {info.sha256}")

    def start_send(self):
        if self.worker or self.payload is None:
            return
        try:
            endpoint = self._endpoint()
        except TransferError as exc:
            self._feedback(str(exc), "error")
            return
        self._save_endpoint(endpoint)
        self._feedback(f"Sending to {endpoint.display}.")
        self._log("SEND", f"{self.payload.path.name} → {endpoint.display}")
        self._start_worker(PayloadWorker(self.payload.path, endpoint, self.payload, self), "send")
        self.send_button.setText("Sending…")

    @Slot(object)
    def progress_changed(self, event: TransferUpdate):
        if event.phase != self.last_phase:
            self.last_phase = event.phase
            titles = {"preparing": "Inspecting payload" if self.job_kind == "inspect" else "Preparing verified payload",
                      "connecting": "Connecting to your console", "sending": "Sending payload", "complete": "Transfer complete"}
            self.stage_label.setText(titles.get(event.phase, event.phase))
            self._badge("complete" if event.phase == "complete" else "busy", event.phase)
            if event.phase == "connecting":
                self._log("CONNECT", "Opening the payload connection.")
            elif event.phase == "sending":
                self._log("CONNECTED", "Console accepted the TCP connection. Streaming payload bytes.")
        fraction = min(1.0, event.completed / max(event.total, 1))
        self.progress_bar.setValue(round(fraction * 1000))
        self.percent_label.setText(f"{fraction:.0%}")
        self.bytes_label.setText(f"{format_bytes(event.completed)} / {format_bytes(event.total)}")
        if event.phase in ("sending", "complete"):
            self.elapsed_label.setText(f"{event.elapsed:.1f} s")
            if event.elapsed > 0:
                self.speed_label.setText(f"{format_bytes(event.completed / event.elapsed)} / s")

    @Slot(object)
    def transfer_finished(self, result: TransferResult):
        self._badge("complete", "Transfer complete")
        self.stage_label.setText("Transfer complete")
        self._feedback("All payload bytes sent. Verify execution on your PS4.", "complete")
        self._log("SENT", f"{format_bytes(result.bytes_sent)} → {result.endpoint.display} · {result.elapsed:.3f} s")
        self._log("NOTE", "The loader does not provide an execution acknowledgement.")
        self._record_history("Sent", result.endpoint, result.bytes_sent)

    @Slot(object)
    def job_failed(self, error: TransferError):
        canceled = isinstance(error, OperationCancelled)
        self._badge("idle" if canceled else "error", "Canceled" if canceled else "Needs attention")
        if self.job_kind == "inspect":
            self.stage_label.setText("Inspection canceled" if canceled else "File not ready")
        else:
            self.stage_label.setText("Transfer canceled" if canceled else "Transfer interrupted")
        self._feedback(str(error), "" if canceled else "error")
        self._log("CANCELED" if canceled else "ERROR", str(error))
        if self.job_kind == "inspect":
            self.file_detail.setText("File not ready. Choose a valid payload.")
            self.hash_label.setText("Not available")
        elif self.worker and self.worker.endpoint:
            self._record_history("Canceled" if canceled else "Failed", self.worker.endpoint, error.bytes_sent)

    @Slot()
    def worker_stopped(self):
        worker = self.worker
        self.worker = None
        self.job_kind = ""
        if worker:
            worker.deleteLater()
        self._refresh()
        if self.closing:
            self.close()

    def cancel_job(self):
        if self.worker and not self.worker.cancel_event.is_set():
            self.worker.cancel()
            self._feedback("Canceling the current operation…")
            self._refresh()

    def clear_file(self):
        if self.worker:
            return
        self.payload = None
        self.file_name.setText("Drop a payload here")
        self.file_detail.setText("Choose a .bin or .elf file to get started.")
        self.hash_label.setText("Calculated locally when you select a file")
        self.hash_label.setToolTip("")
        self.progress_bar.setValue(0)
        self.percent_label.setText("0%")
        self.bytes_label.setText("0 B / 0 B")
        self.speed_label.setText("— / s")
        self.elapsed_label.setText("0.0 s")
        self.stage_label.setText("Ready when you are")
        self._badge("idle", "Idle")
        self._feedback("A connection opens when you send.")
        self._refresh()

    def show_recent(self):
        if self.worker:
            return
        menu = QMenu(self)
        for path in self.settings.recent_files:
            action = menu.addAction(Path(path).name)
            action.setToolTip(path)
            action.setEnabled(Path(path).is_file())
            action.triggered.connect(lambda checked=False, p=path: self.select_file(Path(p)))
        menu.exec(self.recent_button.mapToGlobal(self.recent_button.rect().bottomLeft()))

    def copy_hash(self):
        if self.payload:
            QApplication.clipboard().setText(self.payload.sha256)
            self._feedback("Full SHA-256 copied to the clipboard.")

    def copy_log(self):
        QApplication.clipboard().setText("\n".join(self.log_lines))
        self._feedback("Session log copied to the clipboard.")

    def clear_log(self):
        self.log_lines.clear()
        self.log_view.clear()

    def export_log(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export session log",
                                            f"payload-sender-{datetime.now():%Y%m%d-%H%M%S}.log", "Log files (*.log)")
        if path:
            try:
                Path(path).write_text("\n".join(self.log_lines) + "\n", encoding="utf-8")
                self._feedback("Session log exported.")
            except OSError as exc:
                self._feedback(f"Could not export the log: {exc}", "error")

    def _record_history(self, status: str, endpoint: Endpoint, submitted: int):
        self.settings.history.insert(0, {"file": self.payload.path.name if self.payload else "Unknown",
                                       "destination": endpoint.display, "bytes": submitted, "status": status,
                                       "time": datetime.now().astimezone().isoformat(timespec="seconds"),
                                       "sha256": self.payload.sha256 if self.payload else ""})
        self.settings.history = self.settings.history[:30]
        self._refresh_history()
        self._persist()

    def _refresh_history(self):
        self.history_table.setRowCount(len(self.settings.history))
        for row, item in enumerate(self.settings.history):
            try:
                size = format_bytes(max(0, int(item.get("bytes", 0))))
            except (ValueError, TypeError, OverflowError):
                size = "—"
            values = [item.get("file", ""), item.get("destination", ""), size,
                      item.get("status", ""), str(item.get("time", "")).replace("T", " ")]
            for column, value in enumerate(values):
                cell = QTableWidgetItem(str(value))
                cell.setToolTip(str(value))
                self.history_table.setItem(row, column, cell)

    def show_help(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Quick start")
        dialog.setTextFormat(Qt.TextFormat.PlainText)
        dialog.setText("1. Enable your PS4's BIN loader.\n\n"
                       "2. Enter the console's IP address and the loader's port. GoldHEN uses 9090.\n\n"
                       "3. Browse or drop a .bin/.elf payload supported by that loader.\n\n"
                       "4. Click Send payload and verify execution on the console.\n\n"
                       "A fresh TCP connection is opened for each send. There is no execution acknowledgement. "
                       "After a partial transfer, check/restart your loader before manually resending.\n\n"
                       "Shortcuts: Ctrl+O browse · Ctrl+Enter send · Esc cancel · Ctrl+L clear log")
        dialog.exec()

    def closeEvent(self, event: QCloseEvent):
        if self.worker:
            self.closing = True
            self.cancel_job()
            event.ignore()
        else:
            self._persist()
            event.accept()


def run_gui(config_dir: Path | None = None, payload: Path | None = None,
            host: str | None = None, port: int = 9090, timeout: float = 10) -> int:
    app = QApplication([sys.argv[0]])
    app.setApplicationName("QuayeWorks PS4 Payload Sender")
    app.setOrganizationName("QuayeWorks")
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 10))
    window = MainWindow(SettingsStore(config_dir))
    if host:
        window.host_input.setText(host)
        window.port_input.setValue(max(1, min(65535, port)))
        window.timeout_input.setValue(timeout)
    window.show()
    if payload:
        QTimer.singleShot(0, lambda: window.select_file(payload))
    return app.exec()
````

### payload_sender/settings.py

````python
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
````

### payload_sender/theme.py

````python
"""Two complete desktop themes and small, locally drawn interface icons."""

from pathlib import Path

from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QIcon, QPainter, QPainterPath, QPalette, QPen, QPixmap

DARK = dict(bg="#0B111B", panel="#121C2A", sidebar="#0F1825", inset="#0C1420",
            line="#29374A", text="#EBF1F8", muted="#94A6BD", accent="#80E7C1",
            accent_hover="#A5F0D6", accent_text="#10291F", danger="#FF9DAB", hover="#1D2C40")
LIGHT = dict(bg="#F0F4F8", panel="#FFFFFF", sidebar="#E6EDF4", inset="#F4F7FA",
             line="#CAD5E1", text="#15263A", muted="#566A80", accent="#137D5A",
             accent_hover="#0F694C", accent_text="#FFFFFF", danger="#B32947", hover="#E6EEF5")


def colors(theme: str) -> dict:
    return LIGHT if theme == "light" else DARK


def apply_theme(app, theme: str) -> None:
    c = colors(theme)
    assets = Path(__file__).resolve().parents[1] / "assets"
    c = {**c, "arrow": (assets / f"chevron-{theme}.png").as_posix(),
         "up_arrow": (assets / f"up-{theme}.png").as_posix()}
    palette = QPalette()
    for role, value in [(QPalette.ColorRole.Window, c["bg"]),
                        (QPalette.ColorRole.WindowText, c["text"]),
                        (QPalette.ColorRole.Base, c["inset"]),
                        (QPalette.ColorRole.AlternateBase, c["panel"]),
                        (QPalette.ColorRole.Text, c["text"]),
                        (QPalette.ColorRole.Button, c["panel"]),
                        (QPalette.ColorRole.ButtonText, c["text"]),
                        (QPalette.ColorRole.Highlight, c["accent"]),
                        (QPalette.ColorRole.HighlightedText, c["accent_text"]),
                        (QPalette.ColorRole.PlaceholderText, c["muted"]),
                        (QPalette.ColorRole.ToolTipBase, c["panel"]),
                        (QPalette.ColorRole.ToolTipText, c["text"])]:
        palette.setColor(role, QColor(value))
    app.setPalette(palette)
    app.setStyleSheet("""
        QWidget { color: %(text)s; font-family: "Segoe UI", "DejaVu Sans", sans-serif; font-size: 13px; }
        QMainWindow, QWidget#Root { background: %(bg)s; }
        QLabel { background: transparent; border: none; }
        QLabel[role="muted"] { color: %(muted)s; }
        QLabel[role="eyebrow"] { color: %(muted)s; font-size: 10px; font-weight: 700; letter-spacing: 1px; }
        QLabel[role="heading"] { font-size: 18px; font-weight: 600; }
        QLabel#PageTitle { font-size: 30px; font-weight: 700; }
        QLabel#Brand { font-size: 17px; font-weight: 700; }
        QLabel#BrandTile { background: %(accent)s; color: %(accent_text)s; font-size: 18px;
                           font-weight: 800; border-radius: 11px; }
        QLabel#Status { background: %(panel)s; border: 1px solid %(line)s; border-radius: 13px; padding: 5px 12px;
                        font-size: 11px; font-weight: 600; color: %(muted)s; }
        QLabel#Status[state="ready"], QLabel#Status[state="complete"] { color: %(accent)s; border-color: %(accent)s; }
        QLabel#Status[state="error"] { color: %(danger)s; border-color: %(danger)s; }
        QLabel#FileName { font-size: 20px; font-weight: 600; }
        QLabel#FileSymbol { background: %(hover)s; border-radius: 16px; }
        QLabel#Stage { font-size: 16px; font-weight: 600; }
        QLabel#Percent { font-size: 24px; font-weight: 700; color: %(accent)s; }
        QLabel#Feedback { font-size: 12px; color: %(muted)s; }
        QLabel#Feedback[state="error"] { color: %(danger)s; }
        QLabel#Feedback[state="complete"] { color: %(accent)s; }
        QFrame#Panel { background: %(panel)s; border: 1px solid %(line)s; border-radius: 16px; }
        QFrame#Sidebar { background: %(sidebar)s; border: 1px solid %(line)s; border-radius: 16px; }
        QFrame#DropArea { background: %(inset)s; border: 1px dashed %(line)s; border-radius: 12px; }
        QFrame#DropArea[dragging="true"] { border: 2px dashed %(accent)s; background: %(hover)s; }
        QFrame#Rule { background: %(line)s; border: none; max-height: 1px; }
        QFrame#Hint { background: %(inset)s; border-radius: 10px; }
        QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
            background: %(inset)s; border: 1px solid %(line)s; border-radius: 8px;
            padding: 10px; selection-background-color: %(accent)s; selection-color: %(accent_text)s;
            min-height: 18px;
        }
        QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus { border-color: %(accent)s; }
        QLineEdit:disabled, QComboBox:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled { color: %(muted)s; }
        QComboBox::drop-down { border: none; width: 23px; }
        QComboBox::down-arrow { image: url("%(arrow)s"); width: 12px; height: 8px; }
        QComboBox QAbstractItemView { background: %(panel)s; border: 1px solid %(line)s;
                                    selection-background-color: %(hover)s; padding: 6px; }
        QSpinBox::up-button, QDoubleSpinBox::up-button, QSpinBox::down-button, QDoubleSpinBox::down-button {
            width: 16px; border: none; background: %(hover)s;
        }
        QSpinBox QLineEdit, QDoubleSpinBox QLineEdit {
            background: transparent; border: none; padding: 0px; padding-left: 10px; padding-right: 4px;
            min-height: 0px;
        }
        QSpinBox::up-arrow, QDoubleSpinBox::up-arrow { image: url("%(up_arrow)s"); width: 8px; height: 5px; }
        QSpinBox::down-arrow, QDoubleSpinBox::down-arrow { image: url("%(arrow)s"); width: 8px; height: 5px; }
        QPushButton, QToolButton {
            background: %(panel)s; border: 1px solid %(line)s; border-radius: 8px;
            padding: 9px 13px; font-weight: 600; min-height: 18px;
        }
        QPushButton:hover, QToolButton:hover { background: %(hover)s; border-color: %(muted)s; }
        QPushButton:focus, QToolButton:focus { border: 1px solid %(accent)s; }
        QPushButton:disabled, QToolButton:disabled { color: %(muted)s; background: %(inset)s; }
        QPushButton#Primary { background: %(accent)s; color: %(accent_text)s; border: none;
                              padding: 13px 20px; font-size: 14px; }
        QPushButton#Primary:hover { background: %(accent_hover)s; }
        QPushButton#Primary:disabled { background: %(hover)s; color: %(muted)s; }
        QPushButton#Link { background: transparent; border: none; padding: 4px 6px; font-size: 12px; }
        QPushButton#Link:hover { color: %(accent)s; }
        QPushButton#Danger { color: %(danger)s; }
        QPushButton#Danger:disabled { color: %(muted)s; }
        QProgressBar { background: %(inset)s; border: none; border-radius: 4px; height: 7px; max-height: 7px; }
        QProgressBar::chunk { background: %(accent)s; border-radius: 4px; }
        QTabWidget::pane { border: none; }
        QTabBar::tab { background: transparent; color: %(muted)s; padding: 8px 13px;
                      border-bottom: 2px solid transparent; font-weight: 600; }
        QTabBar::tab:selected { color: %(text)s; border-bottom: 2px solid %(accent)s; }
        QPlainTextEdit { background: %(inset)s; border: 1px solid %(line)s; border-radius: 8px;
                         padding: 9px; font-family: "Cascadia Code", "DejaVu Sans Mono", monospace; font-size: 11px; }
        QTableWidget { background: %(inset)s; border: 1px solid %(line)s; border-radius: 8px;
                       gridline-color: %(line)s; font-size: 11px; selection-background-color: %(hover)s; }
        QHeaderView::section { background: %(panel)s; color: %(muted)s; border: none;
                              padding: 7px 8px; font-size: 10px; font-weight: 600; }
        QScrollBar:vertical { background: transparent; width: 7px; margin: 2px; }
        QScrollBar::handle:vertical { background: %(line)s; border-radius: 3px; min-height: 18px; }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }
        QMenu { background: %(panel)s; border: 1px solid %(line)s; padding: 5px; }
        QMenu::item { padding: 8px 18px; }
        QMenu::item:selected { background: %(hover)s; }
        QToolTip { background: %(panel)s; color: %(text)s; border: 1px solid %(line)s; padding: 6px; }
        QMessageBox, QInputDialog, QFileDialog { background: %(bg)s; }
    """ % c)


def make_icon(name: str, color: str, size: int = 20) -> QIcon:
    pixmap = QPixmap(size * 2, size * 2)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.scale(size / 12, size / 12)  # Draw on a 24-unit canvas at 2x resolution.
    painter.setPen(QPen(QColor(color), 1.7, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    if name == "send":
        path = QPainterPath(QPointF(3, 3))
        for point in [(21, 12), (3, 21), (7, 12), (3, 3)]:
            path.lineTo(*point)
        painter.drawPath(path)
        painter.drawLine(QPointF(7, 12), QPointF(21, 12))
    elif name == "file":
        path = QPainterPath(QPointF(6, 2))
        for point in [(14, 2), (19, 7), (19, 22), (5, 22), (5, 2), (6, 2)]:
            path.lineTo(*point)
        painter.drawPath(path)
        painter.drawLine(QPointF(14, 2), QPointF(14, 7))
        painter.drawLine(QPointF(14, 7), QPointF(19, 7))
        painter.drawLine(QPointF(9, 12), QPointF(15, 12))
        painter.drawLine(QPointF(9, 16), QPointF(15, 16))
    elif name == "folder":
        path = QPainterPath(QPointF(3, 6))
        for point in [(10, 6), (12, 9), (21, 9), (21, 20), (3, 20), (3, 6)]:
            path.lineTo(*point)
        painter.drawPath(path)
    elif name == "theme":
        painter.drawEllipse(QRectF(6, 6, 12, 12))
        for a, b in [((12, 1), (12, 3)), ((12, 21), (12, 23)), ((1, 12), (3, 12)),
                     ((21, 12), (23, 12)), ((4, 4), (5.5, 5.5)), ((18.5, 18.5), (20, 20)),
                     ((4, 20), (5.5, 18.5)), ((18.5, 5.5), (20, 4))]:
            painter.drawLine(QPointF(*a), QPointF(*b))
    elif name == "close":
        painter.drawLine(QPointF(6, 6), QPointF(18, 18))
        painter.drawLine(QPointF(18, 6), QPointF(6, 18))
    elif name == "check":
        painter.drawLine(QPointF(4, 12), QPointF(9, 17))
        painter.drawLine(QPointF(9, 17), QPointF(20, 6))
    else:
        painter.drawRoundedRect(QRectF(2, 2, 20, 20), 5, 5)
        painter.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        painter.drawText(QRectF(2, 2, 20, 20), Qt.AlignmentFlag.AlignCenter, "Q")
    painter.end()
    pixmap.setDevicePixelRatio(2)
    return QIcon(pixmap)
````

### payload_sender/workers.py

````python
"""Qt workers communicate only through queued signals."""

from pathlib import Path
from threading import Event

from PySide6.QtCore import QThread, Signal

from .core import Endpoint, PayloadInfo, TransferError, inspect_payload, transfer_payload


class PayloadWorker(QThread):
    progress = Signal(object)
    inspected = Signal(object)
    transferred = Signal(object)
    failed = Signal(object)

    def __init__(self, path: Path, endpoint: Endpoint | None = None,
                 expected: PayloadInfo | None = None, parent=None):
        super().__init__(parent)
        self.path = path
        self.endpoint = endpoint
        self.expected = expected
        self.cancel_event = Event()

    def cancel(self) -> None:
        self.cancel_event.set()

    def run(self) -> None:
        try:
            if self.endpoint is None:
                self.inspected.emit(inspect_payload(self.path, self.cancel_event, self.progress.emit))
            else:
                self.transferred.emit(transfer_payload(self.path, self.endpoint, self.cancel_event,
                                                       self.progress.emit, self.expected))
        except TransferError as exc:
            self.failed.emit(exc)
        except Exception as exc:
            self.failed.emit(TransferError(f"Unexpected error: {exc}"))
````

### requirements.txt

````text
PySide6-Essentials==6.12.0
````

### tests/__init__.py

````python
"""Run with python -m unittest discover -v."""
````

### tests/support.py

````python
"""Loopback receivers for transport and GUI integration tests."""

import socket
from threading import Event, Thread


class Receiver:
    def __init__(self, stall: bool = False, ipv6: bool = False):
        self.listener = socket.socket(socket.AF_INET6 if ipv6 else socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if stall:
            self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
        self.host = "::1" if ipv6 else "127.0.0.1"
        self.listener.bind((self.host, 0))
        self.listener.listen(1)
        self.listener.settimeout(3)
        self.port = self.listener.getsockname()[1]
        self.data = bytearray()
        self.accepted = Event()
        self.done = Event()
        self.stop = Event()
        self.stall = stall
        self.error = None
        self.connection = None
        self.thread = Thread(target=self._run, daemon=True)

    def _run(self):
        try:
            with self.listener.accept()[0] as connection:
                self.connection = connection
                self.accepted.set()
                if self.stall:
                    self.stop.wait(4)
                else:
                    connection.settimeout(3)
                    while chunk := connection.recv(65536):
                        self.data.extend(chunk)
        except OSError as exc:
            if not self.stop.is_set():
                self.error = exc
        finally:
            self.done.set()

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, *_):
        self.stop.set()
        if self.connection:
            try:
                self.connection.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
        self.listener.close()
        self.thread.join(4)
````

### tests/test_core.py

````python
from __future__ import annotations

import hashlib
import json
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from threading import Event
from unittest.mock import patch

from payload_sender import core
from payload_sender.core import Endpoint, OperationCancelled, TransferError, inspect_payload, transfer_payload
from tests.support import Receiver


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary.name) / "payload.bin"
        self.data = bytes(range(256)) * 4097
        self.path.write_bytes(self.data)

    def tearDown(self):
        self.temporary.cleanup()

    def test_delivers_exact_binary_bytes_and_eof_without_headers(self):
        events = []
        with Receiver() as receiver:
            result = transfer_payload(self.path, Endpoint(receiver.host, receiver.port), update=events.append)
            self.assertTrue(receiver.done.wait(3))
            self.assertIsNone(receiver.error)
            self.assertEqual(bytes(receiver.data), self.data)
            self.assertEqual(result.bytes_sent, len(self.data))
            self.assertEqual(result.payload.sha256, hashlib.sha256(self.data).hexdigest())
            self.assertGreater(result.elapsed, 0)
            self.assertEqual(events[-1].phase, "complete")

    def test_handles_partial_socket_writes(self):
        original_connect = core._connect

        class LimitedSocket:
            def __init__(self, sock):
                self.sock = sock

            def __getattr__(self, name):
                return getattr(self.sock, name)

            def __enter__(self):
                return self

            def __exit__(self, *_):
                self.sock.close()

            def send(self, data):
                return self.sock.send(data[:997])

        with Receiver() as receiver, patch.object(core, "_connect", side_effect=lambda *a: LimitedSocket(original_connect(*a))):
            transfer_payload(self.path, Endpoint(receiver.host, receiver.port))
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)

    def test_snapshot_still_sends_verified_content_when_source_is_edited(self):
        info = inspect_payload(self.path)

        def change_source(event):
            if event.phase == "connecting":
                self.path.write_bytes(b"Edited after preparation")

        with Receiver() as receiver:
            result = transfer_payload(self.path, Endpoint(receiver.host, receiver.port),
                                      update=change_source, expected=info)
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)
            self.assertEqual(result.payload.sha256, info.sha256)

    def test_changed_selected_payload_is_rejected_before_connecting(self):
        info = inspect_payload(self.path)
        self.path.write_bytes(b"changed")
        with patch.object(core, "_connect") as connect:
            with self.assertRaisesRegex(TransferError, "changed"):
                transfer_payload(self.path, Endpoint("127.0.0.1", 9090), expected=info)
            connect.assert_not_called()

    def test_empty_missing_and_wrong_extension_never_connect(self):
        empty = self.path.with_name("empty.bin")
        empty.write_bytes(b"")
        text = self.path.with_suffix(".txt")
        text.write_bytes(b"data")
        missing = self.path.with_name("missing.bin")
        for path in (empty, text, missing):
            with self.subTest(path=path), patch.object(core, "_connect") as connect:
                with self.assertRaises(TransferError):
                    transfer_payload(path, Endpoint("127.0.0.1"))
                connect.assert_not_called()

    def test_elf_and_uppercase_bin_are_accepted(self):
        for suffix in (".elf", ".BIN"):
            path = self.path.with_suffix(suffix)
            path.write_bytes(b"\x00\x01\x02")
            self.assertEqual(inspect_payload(path).size, 3)

    def test_invalid_endpoints_fail_before_connecting(self):
        for endpoint in (Endpoint("not-an-ip"), Endpoint(""), Endpoint("127.0.0.1", 0),
                         Endpoint("127.0.0.1", 65536), Endpoint("127.0.0.1", True),
                         Endpoint("127.0.0.1", timeout=0), Endpoint("127.0.0.1", timeout=float("nan"))):
            with self.subTest(endpoint=endpoint), patch.object(core, "_connect") as connect:
                with self.assertRaises(TransferError):
                    transfer_payload(self.path, endpoint)
                connect.assert_not_called()

    def test_pre_cancellation_never_connects(self):
        cancel = Event()
        cancel.set()
        with patch.object(core, "_connect") as connect:
            with self.assertRaises(OperationCancelled) as caught:
                transfer_payload(self.path, Endpoint("127.0.0.1"), cancel)
            self.assertEqual(caught.exception.bytes_sent, 0)
            connect.assert_not_called()

    def test_cancel_during_send_reports_exact_submitted_bytes(self):
        cancel = Event()

        def progress(event):
            if event.phase == "sending" and event.completed > 0:
                cancel.set()

        with Receiver() as receiver:
            with self.assertRaises(OperationCancelled) as caught:
                transfer_payload(self.path, Endpoint(receiver.host, receiver.port), cancel, progress)
            self.assertTrue(receiver.done.wait(3))
            self.assertGreater(caught.exception.bytes_sent, 0)
            self.assertLess(caught.exception.bytes_sent, len(self.data))
            self.assertEqual(len(receiver.data), caught.exception.bytes_sent)

    def test_stalled_receiver_times_out_and_records_partial_transfer(self):
        self.path.write_bytes(b"x" * (16 * 1024 * 1024))
        with Receiver(stall=True) as receiver:
            started = time.monotonic()
            with self.assertRaises(TransferError) as caught:
                transfer_payload(self.path, Endpoint(receiver.host, receiver.port, 0.5))
            self.assertEqual(caught.exception.phase, "sending")
            self.assertGreater(caught.exception.bytes_sent, 0)
            self.assertLess(caught.exception.bytes_sent, self.path.stat().st_size)
            self.assertLess(time.monotonic() - started, 3)
            self.assertIn("stalled", str(caught.exception))

    def test_connection_refusal_has_actionable_error(self):
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            port = listener.getsockname()[1]
            with self.assertRaisesRegex(TransferError, "Enable the BIN loader") as caught:
                transfer_payload(self.path, Endpoint("127.0.0.1", port, 0.5))
            self.assertEqual(caught.exception.phase, "connecting")
            self.assertEqual(caught.exception.bytes_sent, 0)

    def test_cancellation_during_pending_connection_closes_socket(self):
        cancel = Event()
        from unittest.mock import Mock
        pending = Mock()
        pending.connect_ex.return_value = core.errno.EINPROGRESS

        def pending_select(*_):
            cancel.set()
            return [], [], []

        with patch.object(core.socket, "socket", return_value=pending), patch.object(core.select, "select", side_effect=pending_select):
            with self.assertRaises(OperationCancelled) as caught:
                core._connect(Endpoint("127.0.0.1", 9090, 0.5), cancel)
        self.assertEqual(caught.exception.phase, "connecting")
        pending.close.assert_called_once()

    def test_pending_connection_timeout_closes_socket(self):
        from unittest.mock import Mock
        pending = Mock()
        pending.connect_ex.return_value = core.errno.EINPROGRESS
        with patch.object(core.socket, "socket", return_value=pending), patch.object(core.time, "monotonic", side_effect=[0, 1]):
            with self.assertRaises(TimeoutError):
                core._connect(Endpoint("127.0.0.1", 9090, 0.5), Event())
        pending.close.assert_called_once()

    def test_ipv6_loopback_when_supported(self):
        try:
            receiver = Receiver(ipv6=True)
        except OSError:
            self.skipTest("IPv6 loopback is unavailable")
        with receiver:
            transfer_payload(self.path, Endpoint(receiver.host, receiver.port))
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)

    def test_large_snapshot_spills_to_disk_and_remains_exact(self):
        original_limit = core.SPOOL_MEMORY_LIMIT
        with Receiver() as receiver, patch.object(core, "SPOOL_MEMORY_LIMIT", 64):
            transfer_payload(self.path, Endpoint(receiver.host, receiver.port))
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)
        self.assertEqual(core.SPOOL_MEMORY_LIMIT, original_limit)

    def test_cli_json_success(self):
        with Receiver() as receiver:
            result = subprocess.run([sys.executable, "-m", "payload_sender", "--cli", "--json",
                                     "--host", receiver.host, "--port", str(receiver.port), str(self.path)],
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            output = json.loads(result.stdout)
            self.assertEqual(output["status"], "sent")
            self.assertFalse(output["execution_confirmed"])
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)

    def test_cli_json_failure_has_nonzero_exit_and_no_bytes(self):
        result = subprocess.run([sys.executable, "-m", "payload_sender", "--cli", "--json",
                                 "--host", "invalid", str(self.path)], capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["bytes_sent"], 0)


if __name__ == "__main__":
    unittest.main()
````

### tests/test_gui.py

````python
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import tempfile
import time
import unittest
from pathlib import Path

try:
    from PySide6.QtCore import QMimeData, QPointF, QTimer, QUrl, Qt
    from PySide6.QtGui import QDragEnterEvent, QDropEvent
    from PySide6.QtWidgets import QApplication
    from payload_sender.gui import MainWindow
    from payload_sender.settings import SettingsStore
    QT_AVAILABLE = True
except ImportError:
    QT_AVAILABLE = False

from tests.support import Receiver


@unittest.skipUnless(QT_AVAILABLE, "Install requirements.txt to run GUI tests")
class GuiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.app.setStyle("Fusion")

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.directory = Path(self.temporary.name)
        self.path = self.directory / "test-payload.bin"
        self.data = bytes(range(256)) * 1024
        self.path.write_bytes(self.data)
        self.window = MainWindow(SettingsStore(self.directory / "config"))
        self.window.show()
        self.app.processEvents()

    def tearDown(self):
        self.window.close()
        self.wait_for(lambda: self.window.worker is None)
        self.window.close()
        self.app.processEvents()
        self.temporary.cleanup()

    def wait_for(self, condition, timeout=4):
        deadline = time.monotonic() + timeout
        while not condition() and time.monotonic() < deadline:
            self.app.processEvents()
            time.sleep(0.005)
        self.app.processEvents()
        self.assertTrue(condition(), "UI operation did not complete")

    def select(self):
        self.window.select_file(self.path)
        self.wait_for(lambda: self.window.worker is None)

    def test_real_selection_send_history_and_return_to_ready(self):
        self.assertFalse(self.window.send_button.isEnabled())
        self.select()
        self.assertIsNotNone(self.window.payload)
        self.assertFalse(self.window.send_button.isEnabled())
        with Receiver() as receiver:
            self.window.host_input.setText(receiver.host)
            self.window.port_input.setValue(receiver.port)
            self.assertTrue(self.window.send_button.isEnabled())
            self.window.start_send()
            self.assertFalse(self.window.host_input.isEnabled())
            self.assertFalse(self.window.send_button.isEnabled())
            self.wait_for(lambda: self.window.worker is None)
            self.assertTrue(receiver.done.wait(3))
            self.assertEqual(bytes(receiver.data), self.data)
        self.assertEqual(self.window.progress_bar.value(), 1000)
        self.assertEqual(self.window.settings.history[0]["status"], "Sent")
        self.assertTrue(self.window.send_button.isEnabled())
        self.assertFalse(self.window.cancel_button.isEnabled())

    def test_stalled_transfer_keeps_ui_responsive_and_cancels(self):
        self.path.write_bytes(b"x" * (16 * 1024 * 1024))
        self.select()
        ticks = []
        timer = QTimer(self.window)
        timer.setInterval(10)
        timer.timeout.connect(lambda: ticks.append(1))
        with Receiver(stall=True) as receiver:
            self.window.host_input.setText(receiver.host)
            self.window.port_input.setValue(receiver.port)
            self.window.start_send()
            timer.start()
            self.wait_for(lambda: receiver.accepted.is_set() and len(ticks) >= 5)
            self.assertIsNotNone(self.window.worker)
            self.window.cancel_job()
            self.wait_for(lambda: self.window.worker is None)
            timer.stop()
        self.assertEqual(self.window.settings.history[0]["status"], "Canceled")
        self.assertIn("Canceled", self.window.stage_label.text().title())

    def test_closing_cancels_worker_without_destroying_running_thread(self):
        self.path.write_bytes(b"x" * (16 * 1024 * 1024))
        self.select()
        with Receiver(stall=True) as receiver:
            self.window.host_input.setText(receiver.host)
            self.window.port_input.setValue(receiver.port)
            self.window.start_send()
            self.wait_for(receiver.accepted.is_set)
            self.window.close()
            self.wait_for(lambda: self.window.worker is None and not self.window.isVisible())

    def test_refused_connection_reports_error_and_restores_controls(self):
        import socket
        self.select()
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            self.window.host_input.setText("127.0.0.1")
            self.window.port_input.setValue(listener.getsockname()[1])
            self.window.start_send()
            self.wait_for(lambda: self.window.worker is None)
        self.assertEqual(self.window.settings.history[0]["status"], "Failed")
        self.assertIn("refused", self.window.feedback.text())
        self.assertTrue(self.window.send_button.isEnabled())

    def test_theme_port_profile_and_clipboard_controls(self):
        self.window.toggle_theme()
        self.assertEqual(self.window.settings.theme, "light")
        self.assertEqual(self.window.store.load().theme, "light")
        self.window.loader_combo.setCurrentIndex(1)
        self.assertEqual(self.window.port_input.value(), 9020)
        self.window.port_input.setValue(9500)
        self.assertEqual(self.window.loader_combo.currentIndex(), 2)
        self.window.host_input.setText("127.0.0.1")
        self.window.save_profile()
        self.assertEqual(self.window.store.load().profiles[0].port, 9500)
        self.select()
        self.window.copy_hash()
        self.assertEqual(self.app.clipboard().text(), self.window.payload.sha256)
        self.window.copy_log()
        self.assertIn("SHA-256", self.app.clipboard().text())

    def test_clear_payload_resets_transfer_metrics_and_disables_send(self):
        self.select()
        self.window.host_input.setText("127.0.0.1")
        self.assertTrue(self.window.send_button.isEnabled())
        self.window.clear_file()
        self.assertIsNone(self.window.payload)
        self.assertFalse(self.window.send_button.isEnabled())
        self.assertEqual(self.window.progress_bar.value(), 0)
        self.assertEqual(self.window.bytes_label.text(), "0 B / 0 B")

    def test_drag_and_drop_selects_payload(self):
        mime = QMimeData()
        mime.setUrls([QUrl.fromLocalFile(str(self.path))])
        enter = QDragEnterEvent(QPointF(10, 10), Qt.DropAction.CopyAction, mime,
                               Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
        self.app.sendEvent(self.window.drop_area, enter)
        self.assertTrue(enter.isAccepted())
        drop = QDropEvent(QPointF(10, 10), Qt.DropAction.CopyAction, mime,
                          Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
        self.app.sendEvent(self.window.drop_area, drop)
        self.wait_for(lambda: self.window.worker is None)
        self.assertEqual(self.window.payload.path, self.path)
        self.assertFalse(self.window.drop_area.property("dragging"))

    def test_unsupported_dropped_file_displays_validation_error(self):
        invalid = self.path.with_suffix(".txt")
        invalid.write_bytes(b"not a payload")
        self.window.select_file(invalid)
        self.wait_for(lambda: self.window.worker is None)
        self.assertIsNone(self.window.payload)
        self.assertIn(".bin or .elf", self.window.feedback.text())
        self.assertEqual(self.window.stage_label.text(), "File not ready")

    def test_small_window_scrolls_and_numeric_fields_remain_visible(self):
        self.assertEqual(self.window.centralWidget().verticalScrollBar().maximum(), 0)
        self.assertGreater(self.window.port_input.lineEdit().width(), 50)
        self.assertGreater(self.window.timeout_input.lineEdit().width(), 50)
        self.window.resize(980, 720)
        self.app.processEvents()
        self.assertGreater(self.window.centralWidget().verticalScrollBar().maximum(), 0)


if __name__ == "__main__":
    unittest.main()
````

### tests/test_settings.py

````python
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
````

### tools/build.py

````python
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
````

