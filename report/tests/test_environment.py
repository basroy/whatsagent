import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestEnvironment(unittest.TestCase):

    def test_answer_etl_logs(self):
        Q1_ANSW: str = 'ETL_LOGS'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text + 'aaaa',
                         Text.answers['ETL_LOGS'])

    def test_answer_anaplan_logs(self):
        Q1_ANSW: str = 'ANAPLAN_LOGS'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text, Text.answers['ANAPLAN_LOGS'])

    def test_answer_anaplan_data(self):
        Q1_ANSW: str = 'ANAPLAN_DATA_QUALITY'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text,
                         Text.answers['ANAPLAN_DATA_QUALITY'])

    def test_answer_shell(self):
        Q1_ANSW: str = 'SHELL'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text, Text.answers['SHELL_OR_FILES'])

    def test_answer_files(self):
        Q1_ANSW: str = 'FILES'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text, Text.answers['SHELL_OR_FILES'])

    def test_answer_python(self):
        Q1_ANSW: str = 'SHELL_PYTHON_OUTPUT'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text,
                         Text.answers['SHELL_PYTHON_OUTPUT'])

    def test_answer_binary(self):
        Q1_ANSW: str = 'BINARY_LOG_AND_OTHERS'
        answer: Dict = {
            'ENVIRONMENT': Q1_ANSW
        }

        choices = Choices(answer=answer)
        choices.environment_to_use_audit()
        self.assertEqual(choices.result_text,
                         Text.answers['BINARY_LOG_AND_OTHERS'])

# if __name__ == __main__:
#     unittest.main()
