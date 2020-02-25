from nimoy.specification import Specification
import nimoy

class GradeOneAssignmentSpec(Specification):
    """
    A Nimoy spec.
    """

    def my_feature_method(self) -> None:
        with given:
            a = 'The quick brown fox'
        with expect:
            a == 'The quick frown box'

    def _helper_method(self):
        pass
