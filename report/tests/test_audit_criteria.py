import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestAuditCriteria(unittest.TestCase):

    def test_answer_planning_goaling_cxtssatr(self):
        Q3_ANSW: List = ['NLG_CX_TSS_ATR', 'NLG_GOALING', 'NLG_PLANNING']
        answer: Dict = {
            'AUDIT_TYPES': Q3_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_anaplan_models()
        self.assertEqual(choices.result_text,
                         '\n' +
                         Text.answers['NLG_PLANNING_AND_GOALING_AND_CXTSSATR'])

    def test_answer_sclass_party_container_datahub(self):
        Q3_ANSW: List = [
            'SCLASS_INVALID_PARTY', 'SCLASS_CONTAINER', 'DATA_HUB'
        ]
        answer: Dict = {
            'AUDIT_TYPES': Q3_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_anaplan_models()
        self.assertEqual(
            choices.result_text,
            '\n' +
            Text.answers[
                'SCLASS_PARTY_or_SCLASS_CONTAINER_AND_DATAHUB'
            ]
        )

    def test_answer_sclass_party_container(self):
        Q3_ANSW: List = ['SCLASS_INVALID_PARTY', 'SCLASS_CONTAINER']
        answer: Dict = {
            'AUDIT_TYPES': Q3_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_anaplan_models()
        self.assertEqual(
            choices.result_text,
            '\n' + Text.answers['SCLASS_PARTY_AND_SCLASS_CONTAINER']
        )

    def test_answer_datahub(self):
        Q3_ANSW: List = ['DATA_HUB']
        answer: Dict = {
            'AUDIT_TYPES': Q3_ANSW
        }

        choices = Choices(answer=answer)
        choices.audit_anaplan_models()
        self.assertEqual(choices.result_text, '\n' + Text.answers['DATAHUB'])
