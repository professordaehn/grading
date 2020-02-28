from argparse import Namespace

import mock as mock

from msu.csc232.grade_one_assignment import get_repo_url
from nimoy.specification import Specification


class GradeOneAssignmentSpec(Specification):
    """
    A Nimoy spec to test the GradeOneAssignment module.
    """

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
