import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestImportance(unittest.TestCase):

    # def test_answer_low(self):
    #     Q5_ANSW: Dict = {
    #         'NOT_HIGH': ['LOW']
    #     }
    #     answer: Dict = {
    #         'IMPORTANCE': Q5_ANSW
    #     }
    #
    #     choices = Choices(answer=answer)
    #
    #     choices.audit_importance()
    #     self.assertEqual(choices.result_text,
    #                      '\n' +
    #                      Text.answers['LOW_IMPORTANCE'])
    #
    # def test_answer_medium(self):
    #     Q5_ANSW: Dict = {
    #         'NOT_HIGH': ['MEDIUM']
    #     }
    #     answer: Dict = {
    #         'IMPORTANCE': Q5_ANSW
    #     }
    #
    #     choices = Choices(answer=answer)
    #
    #     choices.audit_importance()
    #     self.assertEqual(choices.result_text,
    #                      '\n' +
    #                      Text.answers['MEDIUM_IMPORTANCE'])
    #
    # def test_answer_none(self):
    #     Q5_ANSW: Dict = {
    #         'NOT_HIGH': ['None']
    #     }
    #     answer: Dict = {
    #         'IMPORTANCE': Q5_ANSW
    #     }
    #     choices = Choices(answer=answer)
    #     choices.audit_importance()
    #     self.assertEqual(choices.result_text,
    #                      '\n' +
    #                      Text.answers['NONE_IMPORTANCE'])

    def test_answer_high_recovery_and_analysis(self):
        Q5_ANSW: Dict = {
            'HIGH': ['Recovery', 'Analysis']
        }
        answer: Dict = {
            'IMPORTANCE': Q5_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_importance()
        self.assertEqual(choices.result_text,
                         '\n' +
                         Text.answers['HIGH_IMPORTANCE_RECOVERY_AND_ANALYSIS'])

    def test_answer_high_dataquality_and_datadependency(self):
        Q5_ANSW: Dict = {
            'HIGH': ['Data Quality', 'Data Dependency']
        }
        answer: Dict = {
            'IMPORTANCE': Q5_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_importance()
        self.assertEqual(
            choices.result_text,
            '\n' +
            Text.answers[
                'HIGH_IMPORTANCE_DATA_QUALITY_AND_DEPENDENCY'
            ]
        )
