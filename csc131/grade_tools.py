"""grade_tools.py - Tools for grading assignments.
"""
# Written by Jim Daehn <jdaehn at missouristate.edu>
# Copyright (C) 2018 JRDevelopment

import subprocess
import sys

import os

EXPECTED_NUM_ARGS = 4
ASSIGNMENT_ARG_INDEX = 1
ASSIGNMENT_NUMBER_ARG_INDEX = 2
USERNAME_ARG_INDEX = 3
COMMAND_LINE_SYNTAX_ERROR_CODE = 2
EXIT_SUCCESS = 0


def print_usage() -> None:
    """
    Print the general usage of this script to the terminal window.
    :return: None
    """
    print("Usage:")
    return None


def clone_repo(repo=None) -> bool:
    """
    Clones the given repo into the current directory.
    :param repo: The name of the repository to clone.
    :return: True is returned upon successful clone; False otherwise.
    """
    if repo is None:
        return False
    print("Cloning repo:", repo)
    git_clone_cmd = ["git", "clone", repo]
    current_process = subprocess.run(git_clone_cmd, stdout=subprocess.PIPE, encoding="utf-8")
    try:
        slash_location = repo.index('/') + 1
    except ValueError:
        return False
    return os.path.isdir(repo[slash_location:-4])


def main() -> int:
    """
    Execution entry point for this script.
    :return: EXIT_SUCCESS is returned upon successful execution of this script.
    """
    clone_repo(None)


if __name__ == '__main__':
    assert not hasattr(sys.stdout, "getvalue")
    main()
