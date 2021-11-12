import unittest

from report.survey_gen import Choices
from report.text import Text


class TestAuditType(unittest.TestCase):

    def test_answer_script_logs(self):
        test_answer: str = 'SCRIPT_LOGS'

        choices = Choices(answer={'AUDIT_TYPES': test_answer})
        choices.audit_type()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['SHELL_PYTHON_OUTPUT']
        )

    def test_answer_binary_logs(self):
        test_answer: str = 'BINARY_LOGS'

        choices = Choices(answer={'AUDIT_TYPES': test_answer})
        choices.audit_type()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['BINARY_LOG_AND_OTHERS']
        )

    def test_answer_python_etl(self):
        test_answer: str = 'PYTHON_ETL'

        choices = Choices(answer={'AUDIT_TYPES': test_answer})
        choices.audit_type()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['SHELL_PYTHON_OUTPUT']
        )

    def test_answer_new(self):
        test_answer: str = 'NEW'

        choices = Choices(answer={'AUDIT_TYPES': test_answer})
        choices.audit_type()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['BINARY_LOG_AND_OTHERS']
        )
