# Notices

This independently written Python application recreates the raw TCP sender workflow of the supplied C# project. The supplied project credits valentinbreiz and HIASQ. Original reference: https://github.com/valentinbreiz/PS4-Payload-Sender

The MIT license in this project covers the newly written application source, tests, documentation, and locally drawn interface assets. It does not relicense the referenced C# project, Qt, Python, or any console payload.

The desktop UI depends on PySide6-Essentials and shiboken6 from The Qt Company. The tested packages declare `LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only` in their metadata. They and their bundled third-party components retain their own licensing. The build script records dependency metadata and copies available dependency license texts into the distribution's `licenses` directory. The tested wheels do not ship separate license-text files, so the official license references below remain relevant for redistribution.

Python and PyInstaller retain their own licenses. Official references:

- https://doc.qt.io/qtforpython-6/licenses.html
- https://docs.python.org/3/license.html
- https://pyinstaller.org/en/stable/license.html
