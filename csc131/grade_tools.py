"""grade_tools.py - Tools for grading assignments.
"""
# Written by Jim Daehn <jdaehn at missouristate.edu>
# Copyright (C) 2018-2019 JRDevelopment

import csv
import os
import subprocess
import sys

EXPECTED_NUM_ARGS = 4
ASSIGNMENT_ARG_INDEX = 1
ASSIGNMENT_NUMBER_ARG_INDEX = 2
USERNAME_ARG_INDEX = 3
COMMAND_LINE_SYNTAX_ERROR_CODE = 2
EXIT_SUCCESS = 0


def get_repos(assignment) -> list:
    """
    Obtain a list of repos to grade.
    :return: A list of repos to grade i s returned.
    """
    github_users = []
    with open('github_users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            github_users.append('git@github.com:msu-csc232-sp19/'+assignment+'-'+row[1]+'.git')

    # repos = ['git@github.com:professordaehn/grading.git']
    # git@github.com:msu-csc232-sp19/lab03-intro-to-dynamic-programming-ncschroeder.git
    return github_users


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


def checkout_develop_branch(repo=None) -> bool:
    """
    Check out the develop branch for the given repo.
    :param repo: the repo in which to check out a develop branch
    :return: True if the repo had a develop branch to checkout, False otherwise.
    """
    return True


def build_test_target(repo=None) -> bool:
    """
    Build the test target on the given repo.
    :param repo: the repo in which to build the test target
    :return: True if a test target was built for the given repo, False otherwise.
    """
    return True


def run_test_target(repo=None) -> bool:
    """
    Run the test target on the repo and generate a grade report
    :param repo: the repo in which to execute the test target
    :return: true if the test target was executed successfully
    to generate a grade report; false otherwise
    """
    return True


def main() -> int:
    """
    Execution entry point for this script.
    :return: EXIT_SUCCESS is returned upon successful execution of this script.
    """
    repos = get_repos('lab03-intro-to-dynamic-programming')
    for repo in repos:
        clone_repo(repo)
        checkout_develop_branch(repo)
        build_test_target(repo)
        run_test_target(repo)


if __name__ == '__main__':
    assert not hasattr(sys.stdout, "getvalue")
    main()
