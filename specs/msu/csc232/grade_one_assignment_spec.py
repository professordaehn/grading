from nimoy.specification import Specification
from unittest import mock
from msu.csc232.grade_one_assignment import get_repo_url


class GradeOneAssignmentSpec(Specification):
    """
    A Nimoy spec.
    """

    def get_repo_url_formats_ssh_method(self) -> None:
        with given:
            mock_namespace = mock.Mock()
        with when:
            mock_namespace.category() >> 'lab'
            mock_namespace.number() >> '04'
            mock_namespace.username() >> 'username'
            mock_namespace.title() >> 'title'
            mock_namespace.method() >> 'ssh'
            url = get_repo_url(mock_namespace)
        with then:
            1 * mock_namespace.category()
            1 * mock_namespace.number()
            1 * mock_namespace.username()
            1 * mock_namespace.title()
            1 * mock_namespace.method()
            url == 'git@github.com:msu-csc232-sp20/lab04-title-username.git'
