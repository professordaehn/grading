"""grade_tools.py - Tools for grading assignments.
"""
# Written by Jim Daehn <jdaehn at missouristate.edu>
# Copyright (C) 2018-2019 JRDevelopment

import csv
import getopt
import os
import subprocess
import sys

EXIT_FAILURE = 2
EXPECTED_NUM_ARGS = 4
ASSIGNMENT_ARG_INDEX = 1
ASSIGNMENT_NUMBER_ARG_INDEX = 2
USERNAME_ARG_INDEX = 3
COMMAND_LINE_SYNTAX_ERROR_CODE = 2
EXIT_SUCCESS = 0
GITHUB_TEAM_PATH = 'git@github.com:msu-csc232-sp19/'
GITHUB_USERNAME_INDEX = 1
REPO_SUFFIX = '.git'
CMAKE_GENERATOR = 'Unix Makefiles'  # or 'Visual Studio 15 2017'?


def get_repos(assignment) -> list:
    """
    Obtain a list of repos to grade.
    :return: A list of repos to grade is returned.
    """
    github_users = []
    with open('github_users.csv', newline='') as csvfile:
        user_names_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in user_names_reader:
            # github_users.append(GITHUB_TEAM_PATH + assignment + '-' + row[GITHUB_USERNAME_INDEX] + REPO_SUFFIX)
            github_users.append(assignment + '-' + row[GITHUB_USERNAME_INDEX])
    return github_users


def print_usage() -> None:
    """
    Print the general usage of this script to the terminal window and exit.
    :return: None
    """
    print()
    print('To grade some assignment (e.g., lab03) with a given title (e.g., intro-to-dynamic-programming) type:')
    print('grade_tools.py -a <assignment> -t <title>')
    print('--or--')
    print('grade_tools.py --assignment <assignment> --title <title>')
    print()
    print('To display this help, use:')
    print('grade_tools.py -h')
    print('--or--')
    print('grade_tools.py --help')
    print()
    print()
    sys.exit(EXIT_FAILURE)


def clone_repo(repo=None) -> bool:
    """
    Clones the given repo into the current directory.
    :param repo: The name of the repository to clone.
    :return: True is returned upon successful clone; False otherwise.
    """

    if repo is None:
        return False
    git_clone_cmd = ["git", "clone", GITHUB_TEAM_PATH + repo + REPO_SUFFIX]
    try:
        current_process = subprocess.run(git_clone_cmd, stdout=subprocess.PIPE, encoding="utf-8")
    except ValueError:
        return False
    print(current_process.stdout)
    return current_process.returncode == 0


def navigate_to(path=None) -> bool:
    if os.path.isdir(path):
        os.chdir(path)
        print("Current path: {}".format(os.getcwd()))
        return True
    else:
        return False


def checkout_develop_branch(repo=None) -> bool:
    """
    Check out the develop branch for the given repo.
    :param repo: the repo in which to check out a develop branch
    :return: True if the repo had a develop branch to checkout, False otherwise.
    """
    if repo is None:
        return False
    git_checkout_cmd = ["git", "checkout", "develop"]
    try:
        current_process = subprocess.run(git_checkout_cmd, stdout=subprocess.PIPE, encoding="utf-8")
    except ValueError:
        return False
    print(current_process.stdout)
    return current_process.returncode == 0


def build_test_target(repo=None) -> bool:
    """
    Build the test target on the given repo.
    :param repo: the repo in which to build the test target
    :return: True if a test target was built for the given repo, False otherwise.
    """
    if not os.path.isdir('generator'):
        os.mkdir('generator')
    navigate_to('generator')
    cmake_cmd = ['cmake', '-G', CMAKE_GENERATOR, '..']
    make_cmd = ['make']
    try:
        cmake_process = subprocess.run(cmake_cmd, stdout=subprocess.PIPE, encoding='utf-8')
        print(cmake_process.stdout)
        make_process = subprocess.run(make_cmd, stdout=subprocess.PIPE, encoding='utf-8')
        print(make_process.stdout)
    except ValueError:
        return False

    print("Navigating back up one directory...")
    navigate_to('../../..')
    return cmake_process.returncode == 0 or make_process.returncode == 0


def run_test_target(assignment=None) -> bool:
    """
    Run the test target on the repo and generate a grade report
    :param assignment: the assignment in which to execute the test target
    :return: true if the test target was executed successfully
    to generate a grade report; false otherwise
    """
    if not os.path.isdir('out'):
        return False
    result = False
    navigate_to('out')
    test_target = './' + assignment + 'Test.exe'
    if os.path.isfile(test_target):
        test_cmd = [test_target]
        try:
            print("Running test target")
            test_target_process = subprocess.run(test_cmd, stdout=subprocess.PIPE, encoding='utf-8')
        except ValueError:
            print(test_target_process.stderr)
        print(test_target_process.stdout)
        result = test_target_process.returncode == 0
    else:
        print('No test target built.')
        print("Navigating back up one directory")
    navigate_to('../../..')
    return result


def main(argv=None) -> int:
    """
    Execution entry point for this script.
    :return: EXIT_SUCCESS is returned upon successful execution of this script.
    """
    if len(argv) == 0:
        print_usage()

    try:
        opts, args = getopt.getopt(argv, "ha:t:", ["help=", "assignment=", "title="])
    except getopt.GetoptError:
        print_usage()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
        elif opt in ("-a", "--assignment"):
            assignment = arg
        elif opt in ("-t", "--title"):
            title = arg

    assignment_repo = assignment + '-' + title
    grading_home = os.getcwd()
    repos = get_repos(assignment_repo)
    for repo in repos:
        clone_repo(repo)
        navigate_to(repo)
        checkout_develop_branch(repo)
        build_test_target(repo)
        run_test_target(assignment)
        navigate_to(grading_home)
    return EXIT_SUCCESS


if __name__ == '__main__':
    assert not hasattr(sys.stdout, "getvalue")
    main(sys.argv[1:])
