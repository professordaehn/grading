import os
import subprocess
from csv import DictReader


def load_users(roster: str) -> list:
    """
    Retrieve a list of GitHub user names from the given roster (in csv format that must have a
    'github_username' column).
    :param roster: the name of the csv file containing roster information
    :return: A list of GitHub user names
    """
    accounts = []
    with open(roster) as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            if len(row['github_username']) > 0:
                accounts.append(row['github_username'])
    return accounts


def grade_all(accounts: list) -> list:
    """
    :param accounts: A list of GitHub user names.
    :return: A list of username whose assignment wasn't graded
    """
    failed_users = []
    for account in accounts:
        cwd = os.path.dirname(os.path.realpath(__file__))
        p = subprocess.run(['python3', f'{cwd}/grade_one_assignment.py',
                                       f'--category=lab',
                                       f'--number=04',
                                       f'--username={account}',
                                       f'--title=intro-to-dynamic-programming'], capture_output=True)
        if p.returncode != 0:
            failed_users.append(account)
    return failed_users


def main() -> None:
    accounts = load_users('classroom_roster.csv')
    failed_results = grade_all(accounts)
    print(failed_results)


if __name__ == '__main__':
    main()
