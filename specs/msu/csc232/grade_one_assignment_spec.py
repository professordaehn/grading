from argparse import Namespace
from msu.csc232.exceptions.grading_exceptions import MethodError
from msu.csc232.grade_one_assignment import get_parameters
from msu.csc232.grade_one_assignment import get_repo_url
from nimoy.specification import Specification


class GradeOneAssignmentSpec(Specification):
    """
    A Nimoy spec to test the GradeOneAssignment module.
    """

    def get_parameters_returns_parser_with_five_attributes(self) -> None:
        """
        Feature method to validate that a command-line parser is created
        that has the desired attributes to grade an assignment.
        :return: None
        """
        with given:
            namespace = get_parameters()
        with expect:
            hasattr(namespace, 'category')
            hasattr(namespace, 'number')
            hasattr(namespace, 'username')
            hasattr(namespace, 'title')
            hasattr(namespace, 'method')


    def get_repo_url_formats_ssh_method(self) -> None:
        """
        Feature method to test that get_repo_url method formats the
        proper url for cloning when cloning via ssh.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', number='04', username='username', title='title', method='ssh')
        with when:
            url = get_repo_url(namespace)
        with then:
            url == 'git@github.com:msu-csc232-sp20/lab04-title-username.git'

    def get_repo_url_formats_https_method(self) -> None:
        """
        Feature method to test that get_repo_url method formats the
        proper url for cloning when cloning via https.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', number='04', username='username', title='title', method='https')
        with when:
            url = get_repo_url(namespace)
        with then:
            url == 'https://github.com/msu-csc232-sp20/lab04-title-username.git'

    def get_repo_url_raises_error_for_bad_method(self) -> None:
        """
        Feature method to test that get_repo_url method raises a MethodError
        when an invalid cloning method is given.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', number='04', username='username', title='title', method='bogus')
        with when:
            url = get_repo_url(namespace)
        with then:
            err = thrown(MethodError)

    def get_repo_url_raises_error_for_missing_method(self) -> None:
        """
        Feature method to test that get_repo_url method raises an AttributeError
        when cloning method is missing.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', number='04', username='username', title='title')
        with when:
            url = get_repo_url(namespace)
        with then:
            err = thrown(AttributeError)

    def get_repo_url_raises_error_for_missing_category(self):
        """
        Feature method to test that get_repo_url method raises an AttributeError
        when category is missing.
        :return: None
        """
        with given:
            namespace = Namespace(number='04', username='username', title='title', method='ssh')
        with when:
            url = get_repo_url(namespace)
        with then:
            err = thrown(AttributeError)

    def get_repo_url_raises_error_for_missing_number(self):
        """
        Feature method to test that get_repo_url method raises an AttributeError
        when number is missing.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', username='username', title='title', method='ssh')
        with when:
            url = get_repo_url(namespace)
        with then:
            err = thrown(AttributeError)

    def get_repo_url_raises_error_for_missing_username(self):
        """
        Feature method to test that get_repo_url method raises an AttributeError
        when username is missing.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', number='04', title='title', method='ssh')
        with when:
            url = get_repo_url(namespace)
        with then:
            err = thrown(AttributeError)

    def get_repo_url_raises_error_for_missing_title(self):
        """
        Feature method to test that get_repo_url method raises an AttributeError
        when title is missing.
        :return: None
        """
        with given:
            namespace = Namespace(category='lab', number='04', username='username', method='ssh')
        with when:
            url = get_repo_url(namespace)
        with then:
            err = thrown(AttributeError)
