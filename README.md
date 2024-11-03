# Time Zone Teler
An app to announce the current time in multiple time zones for screen reader users

## **IMPORTANT NOTE**
This project is intended to help a friend out to hear the current time in multiple time zones using a single keyboard shortcut. It was developed specifically for them, and is not reflective of best practices/conventions I follow.

## Setup and Quickstart
### Install System Dependencies
Make sure you have the following dependencies installed and available on your system:
* [Git](https://git-scm.com/): any recent version.
	* [GH CLI (the GitHub CLI)](https://cli.github.com/) (optional): any recent version.
* [CPython](https://www.python.org/): version 3.12 or higher.
* [pipx](https://github.com/pypa/pipx): any recent version.
	* Use the `ensurepath` subcommand as described in the installation documentation so you can run `pipx` from anywhere.

### Clone the Repo
With Git:

```shell
git clone https://github.com/leibylucw/time-zone-teller.git
cd time-zone-teller
```

Or with gh:

```shell
gh repo clone leibylucw/time-zone-teller
cd time-zone-teller
```

### Install pre-commit and Git Hooks
This repository requires [pre-commit](https://pre-commit.com/) for managing Git hooks.  Start by installing it with:

```shell
pipx install pre-commit
```

Then install the hooks from the root directory of the repository:

```shell
pre-commit install
```

## Development
### Install uv
The project uses [uv](https://github.com/astral-sh/uv). It manages project dependencies and its own virtual environment. To install, use pipx:

```shell
pipx install uv
```

Then, to install dependencies:

```shell
uv venv
uv sync
```

### Run the App
Finally, to run the main script:

```shell
uv run main
```

## Building
You may compile a binary of the app using [pyinstaller](https://www.pyinstaller.org). It was installed using uv to initialize the project. The project contains a `main.spec` file which defines the build process, so you should only need to run the following command:

```shell
uv run pyinstaller build.spec
```

You should see a resulting executable in `dist/Time Zone Teller.exe`.

## Using the App
Once launching the app, either via an executable or Python, you have two commands available to you:
1. `alt+ctrl+t`: announce the current time in your own time zone, as well as America/New_York, Europe/London, and Asia/Tehran.
2. `alt+ctrl+q`: quit the app.
