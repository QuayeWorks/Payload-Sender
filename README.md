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
