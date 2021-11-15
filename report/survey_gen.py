from typing import Dict, List

from report.text import Text


class Question:
    types: Dict = {
        'ENVIRONMENT': (
            'Is the auditing for real-time streaming data, batch procesing, '
            'or data auditing?'
        ),
        'AUDIT_TYPES': 'Will the audit be for different data or log files?',
        'AUDIT_CRITERIA': (
            'Would you like to analyze on a daily basis or weekly or hourly, '
            'would this also involve corrective actions , or would the audit'
            ' be displayed or emailed?'
        ),
        'SIZE': 'What is typical audit size?',

        'IMPORTANCE': 'Do the audits help the organization?'
    }


class Choices:

    def __init__(self, answer):
        self.result_text = ''
        self.answer = answer
        self.text = Text()

    def environment_to_use_audit(self):

        self.result_text += '\n'

        if (
            self.answer['ENVIRONMENT'] == 'SHELL'
            or self.answer['ENVIRONMENT'] == 'FILES'
        ):
            self.result_text = self.text.answers[
                'SHELL_OR_FILES']
        else:
            self.result_text = self.text.answers[self.answer['ENVIRONMENT']]

    def audit_type(self):
        self.result_text += '\n'

        if (
            self.answer['AUDIT_TYPES'] == 'SCRIPT_LOGS'
            or self.answer['AUDIT_TYPES'] == 'PYTHON_ETL'
        ):
            self.result_text += (
                self.text.answers['SHELL_PYTHON_OUTPUT']
            )

        elif (
            self.answer['AUDIT_TYPES'] == 'BINARY_LOGS'
            or self.answer['AUDIT_TYPES'] == 'NEW'
        ):
            self.result_text += (
                self.text.answers['BINARY_LOG_AND_OTHERS']
            )

    def audit_anaplan_models(self):

        self.result_text += '\n'

        NLG_selection: bool = all(
            [
                'NLG_CX_TSS_ATR' in self.answer['AUDIT_CRITERIA'],
                'NLG_GOALING' in self.answer['AUDIT_CRITERIA'],
                'NLG_PLANNING' in self.answer['AUDIT_CRITERIA']
            ]
        )
        SCLASS_selection: bool = any(
            [
                'SCLASS_CONTAINER' in self.answer['AUDIT_CRITERIA'],
                'SCLASS_INVALID_PARTY' in self.answer['AUDIT_CRITERIA']
            ]
        )

        SCLASS_and_DATAHUB: bool = all(
            [
                'DATA_HUB' in self.answer['AUDIT_CRITERIA'],
                any(
                    [
                        'SCLASS_CONTAINER' in self.answer['AUDIT_CRITERIA'],
                        'SCLASS_INVALID_PARTY' in self.answer['AUDIT_CRITERIA']
                    ]
                )
            ]
        )

        DATAHUB: bool = all(
            [
                'DATA_HUB' in self.answer['AUDIT_CRITERIA']
            ]
        )

        if NLG_selection:
            self.result_text += (
                self.text.answers['NLG_PLANNING_AND_GOALING_AND_CXTSSATR']
            )
        elif SCLASS_and_DATAHUB:
            self.result_text += (
                self.text.answers[
                    'SCLASS_PARTY_or_SCLASS_CONTAINER_AND_DATAHUB'
                ]
            )

        # elif SCLASS_selection and DATAHUB:
        #     self.result_text += (
        #         self.text.answers[
        #             'SCLASS_PARTY_or_SCLASS_CONTAINER_AND_DATAHUB'
        #         ]
        #     )
        elif SCLASS_selection:
            self.result_text += (
                self.text.answers['SCLASS_PARTY_OR_SCLASS_CONTAINER']
            )


        elif 'DATA_HUB' in self.answer['AUDIT_CRITERIA']:
            self.result_text += self.text.answers['DATAHUB']

    def filesize(self):
        self.result_text += '\n'

        if self.answer['FSIZE']['UNIT'] == 'GB':
            gb_to_mb: float = round(self.answer['FSIZE']['SIZE'] * 1024, 2)

        else:
            gb_to_mb: float = round(self.answer['FSIZE']['SIZE'], 2)

        if (
            self.answer['FSIZE']['SIZE'] > 2
            and self.answer['FSIZE']['UNIT'] == 'GB'
        ) or (
            self.answer['FSIZE']['SIZE'] > 100
            and self.answer['FSIZE']['UNIT'] == 'MB'
        ):
            self.result_text += self.text.large_size_in_megabytes(
                gb_size=gb_to_mb
            )

        elif (
            self.answer['FSIZE']['SIZE'] < 2
            and self.answer['FSIZE']['UNIT'] == 'GB'
        ) or (
            self.answer['FSIZE']['SIZE'] < 50
            and self.answer['FSIZE']['UNIT'] == 'MB'
        ):
            self.result_text += self.text.small_size_in_megabytes(
                gb_size=gb_to_mb
            )

        else:
            self.result_text += ' Filesize is too large to handle '

    def audit_importance(self):
        self.result_text += '\n'

        if (
            'Recovery' in self.answer['IMPORTANCE']['HIGH'] and
            'Analysis' in self.answer['IMPORTANCE']['HIGH']
        ):
            self.result_text += (
                self.text.answers['HIGH_IMPORTANCE_RECOVERY_AND_ANALYSIS']
            )

        elif (
            'Data Quality' in self.answer['IMPORTANCE']['HIGH'] and
            'Data Dependency' in self.answer['IMPORTANCE']['HIGH']
        ):
            self.result_text += (
                self.text.answers[
                    'HIGH_IMPORTANCE_DATA_QUALITY_AND_DEPENDENCY'
                ]
            )

        elif 'LOW' == self.answer['IMPORTANCE']['NOT_HIGH']:
            self.result_text += (
                self.text.answers[
                    'LOW_IMPORTANCE'
                ]
            )
        elif 'MEDIUM' == self.answer['IMPORTANCE']['NOT_HIGH']:
            self.result_text += (
                self.text.answers[
                    'MEDIUM_IMPORTANCE'
                ]
            )
        elif 'NONE_IMPORTANCE' == self.answer['IMPORTANCE']['NOT_HIGH']:
            self.result_text += (
                self.text.answers[
                    'NONE_IMPORTANCE'
                ]
            )
        else:
            self.result_text += ''

    def get_result_text(self) -> str:

        self.environment_to_use_audit()
        self.audit_type()
        self.audit_anaplan_models()
        self.filesize()
        self.audit_importance()
        return self.result_text


class HtmlSurvey:

    def get(self) -> Dict:
        Q1_ANSW: str = 'ETL_LOGS'
        Q2_ANSW: str = 'SCRIPT_LOGS'
        Q3_ANSW: List = ['DATA_HUB', 'SCLASS_CONTAINER']
        # ['NLG_CX_TSS_ATR', 'NLG_GOALING', 'NLG_PLANNING']
        Q4_ANSW: Dict = {
            'SIZE': 4,
            'UNIT': 'GB'
        }
        Q5_ANSW: Dict = {
            'HIGH': ['Data Quality', 'Recovery', 'Analysis']
            # 'NOT_HIGH': 'LOW'
        }

        self.answer: Dict = {
            'ENVIRONMENT': Q1_ANSW,
            'AUDIT_TYPES': Q2_ANSW,
            'AUDIT_CRITERIA': Q3_ANSW,
            'FSIZE': Q4_ANSW,
            'IMPORTANCE': Q5_ANSW
        }

        return self.answer


htmlsurvey = HtmlSurvey()
answer = htmlsurvey.get()
surveyresult = Choices(answer=answer)
print_resultt: str = surveyresult.get_result_text()
# print(
#     f' After the complete survey, the results are ----> \n {print_resultt}')
