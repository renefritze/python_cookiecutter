#!/usr/bin/env python

import os
import subprocess
import sys
from pathlib import Path


def _precommit():
    def _error(e):
        print(e.output.decode())
        log = Path.home() / ".cache" / "pre-commit" / "pre-commit.log"
        try:
            print(log.read_text())
        except FileNotFoundError:
            print(f"pre-commit log not found at {log}")

    try:
        subprocess.check_output(["pre-commit", "--help"])
    except (PermissionError, FileNotFoundError) as e:
        print(e)
        # this means "not-installed" for us
        return 0
    except subprocess.CalledProcessError as e:
        _error(e)
        return -1
    try:
        subprocess.check_output(["pre-commit", "install"])
        subprocess.check_output(["pre-commit", "run", "-a"])
    except subprocess.CalledProcessError as e:
        _error(e)
        return -1
    return 0


def _git_init():
    try:
        subprocess.check_output(["git", "--version"])
    except (PermissionError, FileNotFoundError, subprocess.CalledProcessError):
        return False
    subprocess.check_output(["git", "init"])
    subprocess.check_output(["git", "add", "."])
    if _precommit() == -1:
        _precommit()
    # skip pre-commit hook which prevents committing to main branch for the first commit
    env = os.environ.copy()
    env["SKIP"] = "no-commit-to-branch"
    subprocess.check_output(["git", "commit", "-am", "initial commit"], env=env)


if __name__ == "__main__":
    if "{{ cookiecutter.create_git_repository|lower }}" != "yes":  # noqa: PLR0133
        sys.exit(0)

    _git_init()
