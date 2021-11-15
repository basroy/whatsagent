import unittest
from typing import List

from report.survey_gen import Choices
from report.text import Text


class TestAuditCriteria(unittest.TestCase):

    def test_answer_planning_goaling_cxtssatr(self):
        test_answer: List = ['NLG_CX_TSS_ATR', 'NLG_GOALING', 'NLG_PLANNING']

        choices = Choices(answer={'AUDIT_CRITERIA': test_answer})
        choices.audit_anaplan_models()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['NLG_PLANNING_AND_GOALING_AND_CXTSSATR']
        )

    def test_answer_sclass_party_container_datahub(self):
        test_answer: List = ['DATA_HUB', 'SCLASS_CONTAINER']

        choices = Choices(answer={'AUDIT_CRITERIA': test_answer})
        choices.audit_anaplan_models()
        print(choices.result_text)
        print(Text.answers[
                  'SCLASS_PARTY_or_SCLASS_CONTAINER_AND_DATAHUB'])
        self.assertEqual(
            choices.result_text,
            '\n' +
            Text.answers[
                'SCLASS_PARTY_or_SCLASS_CONTAINER_AND_DATAHUB'
            ]
        )

    def test_answer_sclass_container(self):
        test_answer: str = 'SCLASS_CONTAINER'

        choices = Choices(answer={'AUDIT_CRITERIA': test_answer})
        choices.audit_anaplan_models()
        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['SCLASS_PARTY_OR_SCLASS_CONTAINER']
        )

    def test_answer_sclass_party(self):
        test_answer: str = 'SCLASS_INVALID_PARTY'

        choices = Choices(answer={'AUDIT_CRITERIA': test_answer})
        choices.audit_anaplan_models()
        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['SCLASS_PARTY_OR_SCLASS_CONTAINER']
        )

    def test_answer_datahub(self):
        test_answer: List = ['DATA_HUB']

        choices = Choices(answer={'AUDIT_CRITERIA': test_answer})
        choices.audit_anaplan_models()

        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['DATAHUB']
        )
