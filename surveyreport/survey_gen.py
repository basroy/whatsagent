from typing import Dict, List

from .survey_text import SurveyResult


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

    def __init__(self, result_text: str, all_survey_answers: Dict):
        self.result_text = result_text
        self.all_survey_answers = all_survey_answers

    # def environment_to_use_audit(self, all_survey_answers: Dict):
    def environment_to_use_audit(self):

        self.result_text += '\n'
        answer_choice: str = self.all_survey_answers['ENVIRONMENT']

        if answer_choice == 'ETL_LOGS':
            self.result_text = SurveyResult.QUES_ANS_PAIR['ETL_LOG']
            print(f'Environment Result is --> ETL_LOG')
        elif answer_choice == 'ANAPLAN_LOGS':
            self.result_text = SurveyResult.QUES_ANS_PAIR[
                'ANAPLAN_LOG']
            print(f'Environment Result is --> ANAPLN_LOG')
        elif answer_choice == 'ANAPLAN_DATA':
            self.result_text = SurveyResult.QUES_ANS_PAIR[
                'ANAPLAN_DATA']
            print(f'Environment Result is --> ANAPLAN_DATA')
        elif (
                answer_choice == 'SHELL'
                or answer_choice == 'FILES'
        ):
            self.result_text = SurveyResult.QUES_ANS_PAIR[
                'SHELL_OR_FILES']
            print(f'Environment Result is --> SHELL_OR_FILES')
        else:
            self.result_text = ''
        # return self.result_text

    # def audit_type(self, all_survey_answers: Dict):
    def audit_type(self):
        self.result_text += '\n'
        answer_choice: str = self.all_survey_answers['AUDIT_TYPES']
        if (
                answer_choice == 'SCRIPT_LOGS'
                or answer_choice == 'PYTHON_ETL'
        ):
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR['SHELL_PYTHON_OUTPUT']
            )
            print(f'Audit_Type Result is --> SHELL_PYTHON_OUTPUT')
        elif answer_choice == 'BINARY_LOGS' or answer_choice == 'NEW':
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR['BINARY_LOG_AND_OTHERS']
            )
            print(f'Audit_Type Result is --> BINARY_LOG_AND_OTHERS')
        else:
            self.result_text += ' '

        # return self.result_text

    # def audit_anaplan_models(self, all_survey_answers: Dict):
    def audit_anaplan_models(self):

        self.result_text += '\n'
        answer_choices: List = self.all_survey_answers['AUDIT_CRITERIA']

        answer_combination_1: bool = all(
            [
                'CX_TSS_ATR' in answer_choices,
                'SCLASS_CONTAINER' in answer_choices,
                'NLG_PLANNING' in answer_choices
            ]
        )
        answer_combination_2: bool = any(
            [
                'SCLASS_CONTAINER' in answer_choices,
                'NLG_GOALING' in answer_choices
            ]
        )

        answer_combination_3: bool = all(
            [
                'CX_TSS_ATR' in answer_choices,
                any(
                    [
                        'SCLASS_CONTAINER' in answer_choices,
                        'NLG_PLANNING' in answer_choices
                    ]
                )
            ]
        )

        answer_combination_4: bool = all(
            ['DATA_HUB' in answer_choices]
        )

        if answer_combination_1:
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR[
                    'NLG_PLANNING_AND_SCLASS_AND_CXTSSATR'
                ]
            )
            print(f'AUDIT_CRITERIA Result is --> '
                  f'NLG_PLANNING_AND_SCLASS_AND_CXTSSATR')

        elif answer_combination_2:
            self.result_text = (
                SurveyResult.QUES_ANS_PAIR[
                    'NLG_GOALING_AND_SCLASS_CONTAINER'
                ]
            )
            print(f'AUDIT_CRITERIA Result is -->'
                  f' NLG_GOALING_AND_SCLASS_CONTAINER2')
        elif answer_combination_3:
            self.result_text += (
                SurveyResult.QUES_ANS_PAIR[
                    'CXTSSATR_AND_NLG_PLANNING_OR_SCLASS'
                ]
            )
            print(f' For AUDIT_CRITERIA Result is --> '
                  f'CXTSSATR_AND_NLG_PLANNING_OR_SCLASS')
        elif answer_combination_4:
            self.result_text += ''

        else:
            self.result_text += ' '

        # return self.result_text

    # def filesize(self, all_survey_answers: Dict):
    def filesize(self):
        self.result_text += '\n'
        typeArgument: str = type(self.all_survey_answers['FSIZE'])
        if typeArgument == dict:
            answer_choice: Dict = self.all_survey_answers['FSIZE']
            answer_choice_1, answer_choice_2 = (
                # self.all_survey_answers['SIZE'],
                # self.all_survey_answers['UNIT']
                answer_choice['SIZE'],
                answer_choice['UNIT']
            )
        else:
            answer_choice_1 = ''
            answer_choice_2 = ''

        answer_choice_1_1: int = int(answer_choice_1)

        if (
                answer_choice_1_1 > 2
                and answer_choice_2 == 'GB'
        ) or (
                answer_choice_1_1 > 100
                and answer_choice_2 == 'MB'
        ):
            self.result_text += SurveyResult.QUES_ANS_PAIR[
                'LARGE_SIZE_FILE']
            print(f' For filesize Result is --> LARGE_SIZE_FILE')
        elif (
                answer_choice_1_1 < 2
                and answer_choice_2 == 'GB'
        ) or (
                answer_choice_1_1 < 50
                and answer_choice_2 == 'MB'
        ):
            self.result_text += SurveyResult.QUES_ANS_PAIR[
                'SMALL_SIZE_FILE']
            print(f' For filesize Result is --> SMALL_SIZE_FILE')

        else:
            self.result_text += ' '

        # return self.result_text

    # def audit_importance(self, all_survey_answers: Dict):
    def audit_importance(self):
        self.result_text += '\n'
        answer_choice_dict: Dict = self.all_survey_answers['IMPORTANCE']

        key1, list_of_choice1 = answer_choice_dict.keys(), \
                                answer_choice_dict.values()
        print(f' Bash {key1} and {list_of_choice1}')
        for key, list_of_choice in answer_choice_dict.items():
            print(key)
            print(list_of_choice)
            if key == 'LOW':
                self.result_text += (
                    SurveyResult.QUES_ANS_PAIR[
                        'LOW_IMPORTANCE'
                    ]
                )
            elif key == 'MEDIUM':
                self.result_text += (
                    SurveyResult.QUES_ANS_PAIR[
                        'MEDIUM_IMPORTANCE'
                    ]
                )
            elif key == 'HIGH':
                if (
                        'Recovery' in list_of_choice and
                        'Analysis' in list_of_choice
                ):
                    self.result_text += (
                        SurveyResult.QUES_ANS_PAIR[
                            'HIGH_IMPORTANCE_SEL_1'
                        ]
                    )
                print(f'IMPORTANCE Result is --> '
                      f'HIGH_IMPORTANCE_SEL_1')
            elif (
                    'Data Quality' in list_of_choice and
                    'Data Dependency' in list_of_choice
            ):
                self.result_text += (
                    SurveyResult.QUES_ANS_PAIR[
                        'HIGH_IMPORTANCE_SEL_2'
                    ]
                )
                print(f'IMPORTANCE Result is --> '
                      f'HIGH_IMPORTANCE_SEL_1')
            else:
                self.result_text += (
                    SurveyResult.QUES_ANS_PAIR[
                        'NONE_IMPORTANCE'
                    ]
                )

        # return self.result_text


surveyQuestion = Question()
# answerEnvironment = Answers_Environment()
# allAnswers = Answer()
HTML_SURVEY: Dict = {}

Q1_ANSW: str = 'ETL_LOGS'
Q2_ANSW: str = 'SCRIPT_LOGS'
Q3_ANSW: List = ['CX_TSS_ATR', 'SCLASS_INVALID_PARTY', 'NLG_PLANNING']
# Q3_ANSW: List = (
#     ['NLG_PLANNING', '', 'SCLASS_INVALID_PARTY', 'CX_TSS_ATR', '', '']
# )
Q4_ANSW: Dict = {
    'SIZE': 4,
    'UNIT': 'GB'
}

Q5_ANSW: Dict = {
    'HIGH': ['Data Quality', 'Recovery', 'Analysis']
}

HTML_SURVEY: Dict = {
    'ENVIRONMENT': Q1_ANSW,
    'AUDIT_TYPES': Q2_ANSW,
    'AUDIT_CRITERIA': Q3_ANSW,
    'FSIZE': Q4_ANSW,
    'IMPORTANCE': Q5_ANSW
}

surveyresult = SurveyChoices(result_text='', all_survey_answers=HTML_SURVEY)
# report_result: str = surveyresult.survey_choice(all_survey_answers=HTML_SURVEY)
# HTML_SURVEY: Dict = {'ENVIRONMENT': Q1_ANSW, }
surveyresult.environment_to_use_audit()
# surveyresult.environment_to_use_audit(all_survey_answers=HTML_SURVEY)
# HTML_SURVEY: Dict = {'AUDIT_TYPES': Q2_ANSW}
# surveyresult.audit_type(all_survey_answers=HTML_SURVEY)
surveyresult.audit_type()
# HTML_SURVEY: Dict = {'AUDIT_CRITERIA': Q3_ANSW}
# surveyresult.audit_anaplan_models(all_survey_answers=HTML_SURVEY)
surveyresult.audit_anaplan_models()
# HTML_SURVEY: Dict = {'SIZE': Q4_ANSW}
# surveyresult.filesize(all_survey_answers=Q4_ANSW)
surveyresult.filesize()

# HTML_SURVEY: Dict = {'IMPORTANCE': Q5_ANSW}
# print(HTML_SURVEY)
# surveyresult.audit_importance(all_survey_answers=HTML_SURVEY)
surveyresult.audit_importance()

# HTML_SURVEY: Dict = {'IMPORTANCE': Q5_ANSW}
# report_result: str = surveyresult.environment_choice(
#     all_survey_answers=HTML_SURVEY)

print_result: str = surveyresult.result_text
print(f' After the complete survery, the results are ----> \n {print_result}')
