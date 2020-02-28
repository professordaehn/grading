import unittest
import os
import subprocess

from src.msu.csc131 import grade_tools
from sys import stdout


class MyTestCase(unittest.TestCase):
    """
    Unit test cases for grade_tools module.
    """
    REAL_REPO = "git@github.com:msu-csc131/lab01-msu-csc-sdent.git"
    BOGUS_REPO = "I'm not really a repo"
    CLONED_REPO = "lab01-msu-csc-sdent"

    def tearDown(self):
        """
        TODO: Figure out how to delete the cloned directory
        :return:
        """
        if os.path.isdir(self.CLONED_REPO):
            rmdir_cmd = ["rm", "-rf", self.CLONED_REPO]
            p = subprocess.run(rmdir_cmd, stdout=subprocess.PIPE, encoding="utf-8")
            print("p.check_returncode() =", p.check_returncode())

    def test_clone_repo_returns_false_for_none(self):
        """
        Validate that clone_repo() returns False when repo is None
        :return: None
        """
        self.assertFalse(grade_tools.clone_repo(None))

    def test_clone_repo_returns_false_for_bogus_repo(self):
        """
        Validate the clone_repo() returns False when a repo doesn't exist.
        :return: None
        """
        self.assertFalse(grade_tools.clone_repo(self.BOGUS_REPO))

    def test_clone_repo_returns_true_upon_success(self):
        """
        Validate the clone_repo() returns True when it successfully clones a repo.
        git@github.com:msu-csc131/lab01-msu-csc-sdent.git
        git@github.com:msu-csc131/hw-01-file-concordance-msu-csc-sdent.git
        :return: None
        """
        self.assertTrue(grade_tools.clone_repo(self.REAL_REPO))


if __name__ == '__main__':
    assert not hasattr(stdout, "getvalue")
    unittest.main(module=__name__, buffer=True, exit=False)
