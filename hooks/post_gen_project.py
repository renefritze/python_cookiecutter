#!/usr/bin/env python
import os
import subprocess


def _precommit(filepath):
    os.chdir(filepath)
    try:
        subprocess.check_output(['pre-commit', 'install'])
        subprocess.check_output(['pre-commit', 'run', '-a'])
    except subprocess.CalledProcessError as e:
        return


def _git_init(filepath):
    os.chdir(filepath)
    try:
        subprocess.check_output(['git', '--version'])
    except subprocess.CalledProcessError as e:
        return
    subprocess.check_output(['git', 'init'])
    subprocess.check_output(['git', 'add', '.'])
    subprocess.check_output(['git', 'commit', '-m', 'initial commit'])


if __name__ == '__main__':
    if '{{ cookiecutter.create_git_repository|lower }}' != 'yes':
        import sys
        sys.exit(0)
    project_directory = os.path.realpath(os.path.curdir)
    _precommit(project_directory)
    _git_init(project_directory)
