from typing import Dict, List

# from whatsagent.surveyreport.survey_text import SurveyResult
from surveyreport.survey_text import SurveyResult


class Question:
    Question_types: Dict = {
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


class SurveyChoices:

    def __init__(self, answer):
        self.result_text = ''
        self.answer = answer

    def environment_to_use_audit(self):

        self.result_text += '\n'

        if self.answer['ENVIRONMENT'] == 'ETL_LOGS':
            self.result_text = SurveyResult.QUES_ANS_PAIR['ETL_LOG']

        elif self.answer['ENVIRONMENT'] == 'ANAPLAN_LOGS':
            self.result_text = SurveyResult.QUES_ANS_PAIR[
                'ANAPLAN_LOG']

        elif self.answer['ENVIRONMENT'] == 'ANAPLAN_DATA':
            self.result_text = SurveyResult.QUES_ANS_PAIR[
                'ANAPLAN_DATA']

        elif (
            self.answer['ENVIRONMENT'] == 'SHELL'
            or self.answer['ENVIRONMENT'] == 'FILES'
        ):
            self.result_text = SurveyResult.QUES_ANS_PAIR[
                'SHELL_OR_FILES']

        else:
            self.result_text = ''

    def audit_type(self):
        self.result_text += '\n'

        if (
            self.answer['AUDIT_TYPES'] == 'SCRIPT_LOGS'
            or self.answer['AUDIT_TYPES'] == 'PYTHON_ETL'
        ):
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR['SHELL_PYTHON_OUTPUT']
            )

        elif (
            self.answer['AUDIT_TYPES'] == 'BINARY_LOGS'
            or self.answer['AUDIT_TYPES'] == 'NEW'
        ):
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR['BINARY_LOG_AND_OTHERS']
            )

        else:
            self.result_text += ' '

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

        if NLG_selection:
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR[
                    'NLG_PLANNING_AND_GOALING_AND_CXTSSATR'
                ]
            )

        elif SCLASS_selection:
            self.result_text = (
                SurveyResult.QUES_ANS_PAIR[
                    'SCLASS_PARTY_AND_SCLASS_CONTAINER'
                ]
            )
        elif SCLASS_and_DATAHUB:
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR[
                    'SCLASS_PPARTY_or_SCLASS_CONTAINER_AND_DATAHUB'
                ]
            )

        elif 'DATA_HUB' in self.answer['AUDIT_CRITERIA']:
            self.result_text += SurveyResult.QUES_ANS_PAIR['DATAHUB']
        else:
            self.result_text += ''

            # def filesize(self, all_survey_answers: Dict):

    def filesize(self):
        self.result_text += '\n'
        size_mb_gb: int = self.answer['FSIZE']['SIZE']
        mb_or_gb: int = self.answer['FSIZE']['UNIT']

        if (
            size_mb_gb > 2
            and mb_or_gb == 'GB'
        ) or (
            size_mb_gb > 100
            and mb_or_gb == 'MB'
        ):
            self.result_text += SurveyResult.QUES_ANS_PAIR[
                'LARGE_SIZE_FILE']

        elif (
            size_mb_gb < 2
            and mb_or_gb == 'GB'
        ) or (
            size_mb_gb < 50
            and mb_or_gb == 'MB'
        ):
            self.result_text += SurveyResult.QUES_ANS_PAIR[
                'SMALL_SIZE_FILE']

        else:
            self.result_text += ' '

    def audit_importance(self):
        self.result_text += '\n'

        if 'HIGH' in list(self.answer['IMPORTANCE'].keys()):
            print(list(self.answer['IMPORTANCE']['HIGH']))
            if (
                'Recovery' in self.answer['IMPORTANCE']['HIGH'] and
                'Analysis' in self.answer['IMPORTANCE']['HIGH']
            ):
                self.result_text += (
                    SurveyResult.QUES_ANS_PAIR[
                        'HIGH_IMPORTANCE_RECOVERY_AND_ANALYSIS'
                    ]
                )

            elif (
                'Data Quality' in self.answer['IMPORTANCE']['HIGH'] and
                'Data Dependency' in self.answer['IMPORTANCE']['HIGH']
            ):
                self.result_text += (
                    SurveyResult.QUES_ANS_PAIR[
                        'HIGH_IMPORTANCE_DATA_QUALITY_AND_DEPENDENCY'
                    ]
                )

        elif 'LOW' in list(self.answer['IMPORTANCE'].keys()):
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR[
                    'LOW_IMPORTANCE'
                ]
            )
        elif 'MEDIUM' in list(self.answer['IMPORTANCE'].keys()):
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR[
                    'MEDIUM_IMPORTANCE'
                ]
            )
        else:
            self.result_text += SurveyResult.QUES_ANS_PAIR['NONE_IMPORTANCE']

    def all_survey(self) -> str:

        self.environment_to_use_audit()
        self.audit_type()
        self.audit_anaplan_models()
        self.filesize()
        self.audit_importance()
        return self.result_text


class HtmlSurvey:
    def __init__(self, HTML_SURVEY):
        self.HTML_SURVEY = HTML_SURVEY

    # HTML_SURVEY: Dict = {}

    def constructed_survey(self) -> Dict:
        Q1_ANSW: str = 'ETL_LOGS'
        Q2_ANSW: str = 'SCRIPT_LOGS'
        Q3_ANSW: List = ['NLG_CX_TSS_ATR', 'NLG_GOALING', 'NLG_PLANNING']
        Q4_ANSW: Dict = {
            'SIZE': 4,
            'UNIT': 'GB'
        }
        Q5_ANSW: Dict = {
            'HIGH': ['Data Quality', 'Recovery', 'Analysis']
        }

        self.HTML_SURVEY: Dict = {
            'ENVIRONMENT': Q1_ANSW,
            'AUDIT_TYPES': Q2_ANSW,
            'AUDIT_CRITERIA': Q3_ANSW,
            'FSIZE': Q4_ANSW,
            'IMPORTANCE': Q5_ANSW
        }

        return self.HTML_SURVEY


HTML_SURVEY: Dict = {}
htmlsurvey = HtmlSurvey(HTML_SURVEY=HTML_SURVEY)
HTML_SURVEY = htmlsurvey.constructed_survey()
surveyresult = SurveyChoices(answer=HTML_SURVEY)
print_resultt: str = surveyresult.all_survey()
print(
    f' After the complete survey, the results are ----> \n {print_resultt}')
