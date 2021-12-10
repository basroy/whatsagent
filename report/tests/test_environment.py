import unittest

from report.survey_gen import Choices
from report.text import Text


class TestEnvironment(unittest.TestCase):

    def test_answer_etl_logs(self):
        test_answer: str = 'ETL_LOGS'

        choices = Choices(answer={'ENVIRONMENT': test_answer})
        choices.environment_to_use_audit()

        self.assertEqual(
            choices.result_text,
            Text.answers[test_answer]
        )

    def test_answer_anaplan_logs(self):
        test_answer: str = 'ANAPLAN_LOGS'

        choices = Choices(answer={'ENVIRONMENT': test_answer})
        choices.environment_to_use_audit()

        self.assertEqual(
            choices.result_text,
            Text.answers[test_answer]
        )

    def test_answer_anaplan_data(self):
        test_answer: str = 'ANAPLAN_DATA_QUALITY'

        choices = Choices(answer={'ENVIRONMENT': test_answer})
        choices.environment_to_use_audit()

        self.assertEqual(
            choices.result_text,
            Text.answers[test_answer]
        )

    def test_answer_shell(self):
        test_answer: str = 'SHELL'

        choices = Choices(answer={'ENVIRONMENT': test_answer})
        choices.environment_to_use_audit()

        self.assertEqual(
            choices.result_text,
            Text.answers['SHELL_OR_FILES']
        )

    def test_answer_files(self):
        test_answer: str = 'FILES'

        choices = Choices(answer={'ENVIRONMENT': test_answer})
        choices.environment_to_use_audit()

        self.assertEqual(
            choices.result_text,
            Text.answers['SHELL_OR_FILES']
        )
