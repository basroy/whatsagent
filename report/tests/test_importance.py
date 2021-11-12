import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestImportance(unittest.TestCase):

    def test_answer_low(self):
        test_answer: Dict = {
            'HIGH': [],
            'NOT_HIGH': 'LOW',
        }

        choices = Choices(answer={'IMPORTANCE': test_answer})
        choices.audit_importance()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['LOW_IMPORTANCE']
        )

    def test_answer_medium(self):
        test_answer: Dict = {
            'HIGH': [],
            'NOT_HIGH': 'MEDIUM',
        }

        choices = Choices(answer={'IMPORTANCE': test_answer})
        choices.audit_importance()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['MEDIUM_IMPORTANCE']
        )

    def test_answer_none(self):
        test_answer: Dict = {
            'HIGH': [],
            'NOT_HIGH': 'None',
        }

        choices = Choices(answer={'IMPORTANCE': test_answer})
        choices.audit_importance()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['NONE_IMPORTANCE']
        )

    def test_answer_high_recovery_and_analysis(self):
        test_answer: Dict = {
            'HIGH': ['Recovery', 'Analysis'],
            'NOT_HIGH': '',
        }

        choices = Choices(answer={'IMPORTANCE': test_answer})
        choices.audit_importance()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['HIGH_IMPORTANCE_RECOVERY_AND_ANALYSIS']
        )

    def test_answer_high_dataquality_and_datadependency(self):
        test_answer: Dict = {
            'HIGH': ['Data Quality', 'Data Dependency'],
            'NOT_HIGH': '',
        }

        choices = Choices(answer={'IMPORTANCE': test_answer})
        choices.audit_importance()

        self.assertEqual(
            choices.result_text,
            '\n' +
            Text.answers[
                'HIGH_IMPORTANCE_DATA_QUALITY_AND_DEPENDENCY'
            ]
        )
