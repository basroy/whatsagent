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
        print(choices.result_text)

#
# class TestEnvironment(unittest.TestCase):
#     def answer_selected_only_two(self):
#         data: List = ['SCLASS_CONTAINER', 'SCLASS_INVALID_PARTY']
#         result: int = step_one(data)
#         self.assertEqual(result, 2)
#
#     def answer_selected_only_three(self):
#         data: List = ['NLG_CX_TSS_ATR', 'NLG_GOALING', 'NLG_PLANNING']
#         result: int = step_one(data)
#         self.assertEqual(result, 3)
#
#
# if __name__ == __main__:
#     unittest.main()
