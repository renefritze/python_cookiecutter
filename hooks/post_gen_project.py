#!/usr/bin/env python

import os
import sys
import subprocess


def _precommit():
    def _error(e):
        print(e.output)
        log = os.path.expanduser("~/.cache/pre-commit/pre-commit.log")
        try:
            print(open(log, "rt").read())
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
    subprocess.check_output(["git", "commit", "-am", "initial commit"])


if __name__ == "__main__":
    if "{{ cookiecutter.create_git_repository|lower }}" != "yes":
        sys.exit(0)

    _git_init()
