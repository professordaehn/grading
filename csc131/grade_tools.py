"""grade_tools.py - Tools for grading assignments.
"""
# Written by Jim Daehn <jdaehn at missouristate.edu>
# Copyright (C) 2018 JRDevelopment

from sys import argv

EXPECTED_NUM_ARGS = 4
ASSIGNMENT_ARG_INDEX = 1
ASSIGNMENT_NUMBER_ARG_INDEX = 2
USERNAME_ARG_INDEX = 3
COMMAND_LINE_SYNTAX_ERROR_CODE = 2


def print_usage() -> None:
    print("Usage:")
    return None


def clone_repo(repo: str) -> None:
    print("Cloning repo:", repo)
    return None


def main() -> int:

    clone_repo()


if __name__ == '__main__':
    if len(argv) == EXPECTED_NUM_ARGS:
        main()
    else:
        print_usage()
