import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestAuditType(unittest.TestCase):

    def test_answer_script_logs(self):
        Q2_ANSW: str = 'SCRIPT_LOGS'
        answer: Dict = {
            'AUDIT_TYPES': Q2_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_type()
        self.assertEqual(choices.result_text,
                         '\n' + Text.answers['SHELL_PYTHON_OUTPUT'])

    def test_answer_binary_logs(self):
        Q2_ANSW: str = 'BINARY_LOGS'
        answer: Dict = {
            'AUDIT_TYPES': Q2_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_type()
        self.assertEqual(choices.result_text, '\n' +
                         Text.answers['BINARY_LOG_AND_OTHERS'])

    def test_answer_python_etl(self):
        Q2_ANSW: str = 'PYTHON_ETL'
        answer: Dict = {
            'AUDIT_TYPES': Q2_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_type()
        self.assertEqual(choices.result_text, '\n' +
                         Text.answers['SHELL_PYTHON_OUTPUT'])

    def test_answer_new(self):
        Q2_ANSW: str = 'NEW'
        answer: Dict = {
            'AUDIT_TYPES': Q2_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_type()
        # print(choices.result_text)
        self.assertEqual(choices.result_text,
                         '\n' + Text.answers['BINARY_LOG_AND_OTHERS'])
