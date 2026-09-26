# Python Installation Guide

## Before you begin

Use the official [Python downloads page](https://www.python.org/downloads/) for Windows and macOS. On Linux, prefer the package manager for your distribution. Check that your operating system is supported by the Python release you choose. Do not uninstall or replace the operating system's own Python installation.

## Installation steps

### Windows

1. Open [python.org/downloads](https://www.python.org/downloads/) and select the current stable Python 3 release for Windows.
2. Download the recommended Windows installer or Python install manager offered on the page, then open it.
3. Follow the installer prompts. If using the traditional installer, enable **Add python.exe to PATH** when offered. If Windows asks whether to install for all users, choose the option allowed by your account or organization.
4. Finish the installation. If the installer asks to disable the Windows path-length limit, accept only if permitted on your computer; it is optional for getting started.
5. Close and reopen PowerShell or Command Prompt so it reads the updated environment.

### macOS

1. Open [python.org/downloads](https://www.python.org/downloads/) and select the current stable Python 3 release for macOS.
2. Download the macOS installer package (`.pkg`) and open it.
3. Follow the installer prompts and enter your macOS password if requested.
4. Close and reopen Terminal before verification.

macOS may include a system-managed Python or development tools. Leave those files in place; use the newly installed Python command shown in the verification steps.

### Linux

Python 3 is often already installed. First try `python3 --version`. If Python is missing, use your distribution's package manager. Examples:

**Ubuntu or Debian:**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Fedora:**

```bash
sudo dnf install python3 python3-pip
```

**Arch Linux:**

```bash
sudo pacman -S python python-pip
```

Package names can vary by release. Consult your distribution's documentation if a command is unavailable. Avoid replacing the distribution-managed Python with a manually compiled installation.

## Verification steps

Open a new terminal and run the command for your platform. A version number should be printed; the exact number depends on the release you installed.

**Windows PowerShell or Command Prompt:**

```powershell
py --version
```

If the `py` launcher is unavailable, try:

```powershell
python --version
```

**macOS or Linux:**

```bash
python3 --version
```

Check that pip, Python's package installer, is available:

```text
Windows:  py -m pip --version
macOS:    python3 -m pip --version
Linux:    python3 -m pip --version
```

The output should include a pip version and a path associated with the selected Python installation. If it does not, see [Troubleshooting](#troubleshooting).

### Optional: verify with a virtual environment

A virtual environment keeps packages for one project separate from system Python and other projects.

**Windows:**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe --version
```

**macOS or Linux:**

```bash
python3 -m venv .venv
.venv/bin/python --version
```

If creation succeeds and the final command prints a Python version, the environment is ready. Activation is optional; use `.venv`'s Python directly as shown above or follow the Python documentation for activation instructions.

## Troubleshooting

### `python` or `python3` is not recognized / command not found

- Open a new terminal after installation and retry.
- On Windows, try `py --version`; the launcher may be available even when `python` is not on PATH.
- On macOS and Linux, try `python3 --version`.
- If neither works, rerun the official installer and check its command-line or PATH options. On a managed device, ask your administrator before changing PATH.

### The wrong Python version runs

- Check which command you ran and compare it with the path shown by `py -0p` on Windows or `which python3` on macOS/Linux.
- Use the intended interpreter explicitly (`py -3` on Windows or the full path to `python3` elsewhere).
- Do not remove an operating-system-managed Python to resolve a version conflict.

### `No module named pip` appears

- Run `py -m ensurepip --upgrade` on Windows, or `python3 -m ensurepip --upgrade` where supported.
- Some Linux distributions package pip separately; install it through the distribution's package manager.
- Prefer `python -m pip` (or `python3 -m pip`) so pip targets the same interpreter you use to run programs.

### Linux reports an externally managed environment

This is a protection applied by some distributions. Do not force a system-wide pip install. Create a virtual environment with `python3 -m venv .venv`, then install packages using `.venv/bin/python -m pip`. Install `python3-venv` with your package manager if the `venv` module is missing.

### Installation is blocked or permission is denied

Use an account with installation permission, select a per-user installation if the installer offers one, or contact your device administrator. Avoid downloading installers from unofficial mirrors.

## Conclusion

Python is installed when the version and pip checks succeed. Keep the operating system's Python intact, use the interpreter command appropriate to your platform, and use virtual environments for project dependencies.

## Official references

- [Python downloads](https://www.python.org/downloads/)
- [Python documentation: Using Python on Windows](https://docs.python.org/3/using/windows.html)
- [Python documentation: Using Python on macOS](https://docs.python.org/3/using/mac.html)
- [Python documentation: Using Python on Unix platforms](https://docs.python.org/3/using/unix.html)