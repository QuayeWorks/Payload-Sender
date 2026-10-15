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
