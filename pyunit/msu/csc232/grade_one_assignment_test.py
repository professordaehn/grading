import unittest

# code from module you're testing...
from msu.csc232.exceptions.grading_exceptions import MethodError
from msu.csc232.grade_one_assignment import get_parameters
from msu.csc232.grade_one_assignment import get_repo_url


class MyTestCase(unittest.TestCase):
    """
    PyUnit test ...
    """

    def setUp(self) -> None:
        """
        Call before every test case.
        :return: None
        """
        pass

    def tearDown(self) -> None:
        """
        Call after every test case.
        :return: None
        """
        pass

    def testCaseA(self) -> None:
        """
        Test case A. note that all test method names must begin with 'test.'
        :return:
        """
        namespace = get_parameters()
        self.assertTrue(hasattr(namespace, 'category'), "get_parameters() did not return a namespace with the category "
                                                        "parameter")

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()  # run all tests
