# Frequently Asked Questions

### Is Python free to use?

Yes. Python is open source and can be downloaded and used without a purchase. Download it from [python.org](https://www.python.org/downloads/) or use your Linux distribution's official package manager.

### Which Python version should I install?

Choose the current stable Python 3 release that supports your operating system and any software you need to use. Check project-specific version requirements when working on an existing codebase.

### Do I need an internet connection?

An internet connection is normally needed to download Python or retrieve packages through a package manager. A network administrator may provide an approved offline installer for restricted computers.

### Is Python already installed on my computer?

Possibly. Run `py --version` on Windows or `python3 --version` on macOS and Linux. If a version is shown, Python is available through that command; check its version against your project requirements.

### Why are the commands different across operating systems?

Windows commonly provides the `py` launcher, while macOS and Linux commonly use `python3` to distinguish Python 3 from other commands. Use the command that succeeded during the verification steps.

### Do I need to install pip separately?

Many Python installers include pip. Check with `py -m pip --version` on Windows or `python3 -m pip --version` on macOS/Linux. Some Linux distributions package pip separately.

### What is a virtual environment?

A virtual environment is an isolated Python environment for a project. It helps keep that project's installed packages separate from other projects and from the operating system's Python.

### Can I remove the Python version that came with my operating system?

No. System tools may depend on it. Install or select another Python version without replacing or deleting the operating-system-managed copy.

### Where should I get help if installation still fails?

Check the [Installation guide's troubleshooting section](Installation.md#troubleshooting), your operating system or Linux distribution documentation, and the official [Python documentation](https://docs.python.org/3/).