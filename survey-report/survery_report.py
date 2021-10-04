from typing import Dict, List

from lorem_text import Survey_Result, Dicts_Answer


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


class AnswersEnvironment:
    environment: Dict = {
        'ETL_LOGS': (
            'Informatica logs, which are in binary format, to look for '
            'failed executions, and to compare source and target counts of '
            'the ETL.'
        ),
        'ANAPLAN_LOGS': (
            'For batch-processed jobs, any errored Anaplan api '
            'executions.'
        ),
        'ANAPLAN_DATA': (
            'This will allow for comparison of data cells '
            'between one or more modules or lists'
        ),
        'SHELL': 'Check for permission on executables.',
        'FILES': (
            'Audit the latsst timestamp and size of csv or txt files, '
            'for batch-processed or streaming data.'
        )
    }


class Answers_Audit_Types:
    Audit_Type: Dict = {
        'SCRIPT_LOGS': (
            'Shell scripts that write standard output to text log '
            'files with .log extension.'
        ),
        'BINARY_LOGS': 'Informatica session logs with .bin extension.',
        'PYTHON_ETL': 'Execute specific python apis for data audit.',
        'NEW': 'Audits unidentified and need to be coded.'
    }


class Answers_Anaplan:
    Modules: Dict = {
        'NLG_PLANNING': 'Q1 and Q2 Final Goals of specific PEC and L2 Node',
        'NLG_GOALING': (
            'Q1 and Q2 Final Goals of specific PEC and Node at any level'
        ),
        'SCLASS_INVALID_PARTY': (
            'Count of Invalid Parties compared to Booked Parties'
        ),
        'CX_TSS_ATR': 'Q1 and Q2 Annualized for Current_Year.',
        'SCLASS_CONTAINER': 'The Container refresh on a daily schedule',
        'DATA_HUB': 'SHARE and SAVM refreshed on daily schedule'
    }


class Answers_Size:
    pass


class Answers_Importance:
    Importance: Dict = {
        'HIGH': 'Must not skip any day.',
        'MEDIUM': 'The data gets refreshed on next cycle.',
        'LOW': 'Good to have audits',
        'IF HIGH': [
            'Data Quality', 'Recovery', 'Analysis',
            'Data Dependency', 'Reporting'
        ]
    }


class Survey_Choices:
    result_text: str = ''

    def validate_answer_selection_in_dictionary(
            self, all_survey_answers: Dict) -> bool:
        for key, answer_choice in all_survey_answers.items():
            if (
                    key == 'ENVIRONMENT'
                    and answer_choice in Dicts_Answer.environment
            ):
                return_status: bool = True
            elif {
                key == 'AUDIT_TYPES'
                and answer_choice in Dicts_Answer.audit_type
            }:
                return_status: bool = True

            elif (
                    key == 'AUDIT_CRITERIA'
                    and answer_choice in Dicts_Answer.audit_criteria
            ):
                return_status: bool = True
            elif key == 'SIZE':
                return_status: bool = True

            elif (
                    key == 'IMPORTANCE'
                    and answer_choice in Dicts_Answer.importance
            ):
                return_status: bool = True
            else:
                return_status: bool = False
        return return_status

    def environment_choice(self, all_survey_answers: Dict) -> str:

        is_valid_answer: bool = self.validate_answer_selection_in_dictionary(
            all_survey_answers
        )
        print(is_valid_answer)
        if is_valid_answer:
            self.result_text += '\n'
            answer_choice: str = all_survey_answers['ENVIRONMENT']

            if answer_choice == 'ETL_LOGS':
                self.result_text = Survey_Result.QUES_ANS_PAIR['ETL_LOG']
                print(f'Environment Result is --> ETL_LOG')
            elif answer_choice == 'ANAPLAN_LOGS':
                self.result_text = Survey_Result.QUES_ANS_PAIR[
                    'ANAPLAN_LOG']
                print(f'Environment Result is --> ANAPLN_LOG')
            elif answer_choice == 'ANAPLAN_DATA':
                self.result_text = Survey_Result.QUES_ANS_PAIR[
                    'ANAPLAN_DATA']
                print(f'Environment Result is --> ANAPLAN_DATA')
            elif (
                    answer_choice == 'SHELL'
                    or answer_choice == 'FILES'
            ):
                self.result_text = Survey_Result.QUES_ANS_PAIR[
                    'SHELL_OR_FILES']
                print(f'Environment Result is --> SHELL_OR_FILES')
        else:
            self.result_text = ''
        return self.result_text

    def audittype_choice(self, all_survey_answers: Dict) -> str:
        is_valid_answer: bool = self.validate_answer_selection_in_dictionary(
            all_survey_answers
        )
        if is_valid_answer:
            self.result_text += '\n'
            answer_choice: str = all_survey_answers['AUDIT_TYPES']
            if (
                    answer_choice == 'SCRIPT_LOGS'
                    or answer_choice == 'PYTHON_ETL'
            ):
                self.result_text += (
                    Survey_Result.QUES_ANS_PAIR['SHELL_PYTHON_OUTPUT']
                )
                print(f'Audit_Type Result is --> SHELL_PYTHON_OUTPUT')
            elif answer_choice == 'BINARY_LOGS' or answer_choice == 'NEW':
                self.result_text += (
                    Survey_Result.QUES_ANS_PAIR['BINARY_LOG_AND_OTHERS']
                )
                print(f'Audit_Type Result is --> BINARY_LOG_AND_OTHERS')
        else:
            self.result_text += ' '

        return self.result_text

    def auditcriteria_choice(self, all_survey_answers: Dict) -> str:
        is_valid_answer: bool = self.validate_answer_selection_in_dictionary(
            all_survey_answers
        )
        if is_valid_answer:
            self.result_text += '\n'
            # answer_choice = all_survey_answers['AUDIT_CRITERIA']
            nlg_planning: str = ''
            nlg_goaling: str = ''
            sclass_invalid_party: str = ''
            sclass_container: str = ''
            cx_tss_atr: str = ''
            data_hub: str = ''
            answer_choices: List = all_survey_answers['AUDIT_CRITERIA']

            for answer_choice in answer_choices:
                if 'NLG_PLANNING' in answer_choice:
                    nlg_planning: str = 'NLG_PLANNING'

                elif 'NLG_GOALING' in answer_choice:
                    nlg_goaling: str = 'NLG_GOALING'
                elif 'SCLASS_INVALID_PARTY' in answer_choice:
                    sclass_invalid_party: str = 'SCLASS_INVALID_PARTY'
                elif 'SCLASS_CONTAINER' in answer_choice:
                    sclass_container: str = 'SCLASS_CONTAINER'
                elif 'CX_TSS_ATR' in answer_choice:
                    cx_tss_atr: str = 'CX_TSS_ATR'
                elif 'DATA_HUB' in answer_choice:
                    data_hub: str = 'DATA_HUB'

            answer_combination_1: bool = all(
                [cx_tss_atr, nlg_planning, sclass_invalid_party])
            answer_combination_2: bool = any(
                [nlg_goaling, sclass_container])
            answer_combination_3: bool = all([
                cx_tss_atr, any([nlg_planning, sclass_invalid_party]
                                )])
            answer_combination_4: bool = all(data_hub)

            if answer_combination_1:
                self.result_text += (
                    Survey_Result.QUES_ANS_PAIR[
                        'NLG_PLANNING_AND_SCLASS_AND_CXTSSATR'
                    ]
                )
                print(f'AUDIT_CRITERIA Result is --> '
                      f'NLG_PLANNING_AND_SCLASS_AND_CXTSSATR')

            elif answer_combination_2:
                self.result_text = (
                    Survey_Result.QUES_ANS_PAIR[
                        'NLG_GOALING_AND_SCLASS_CONTAINER'
                    ]
                )
                print(f'AUDIT_CRITERIA Result is -->'
                      f' NLG_GOALING_AND_SCLASS_CONTAINER2')
            elif answer_combination_3:
                self.result_text += (
                    Survey_Result.QUES_ANS_PAIR[
                        'CXTSSATR_AND_NLG_PLANNING_OR_SCLASS'
                    ]
                )
                print(f' For AUDIT_CRITERIA Result is --> '
                      f'CXTSSATR_AND_NLG_PLANNING_OR_SCLASS')
            elif answer_combination_4:
                self.result_text += ''

        else:
            self.result_text += ' '

        return self.result_text

    def filesize_choice(self, all_survey_answers: Dict) -> str:
        is_valid_answer: bool = self.validate_answer_selection_in_dictionary(
            all_survey_answers
        )
        print(all_survey_answers)
        if is_valid_answer:
            self.result_text += '\n'
            answer_choice_1, answer_choice_2 = (
                all_survey_answers['SIZE'], all_survey_answers['UNIT']
            )
            answer_choice_1_1: int = int(answer_choice_1)

            if (
                    answer_choice_1_1 > 2
                    and answer_choice_2 == 'GB'
            ) or (
                    answer_choice_1_1 > 100
                    and answer_choice_2 == 'MB'
            ):
                self.result_text += Survey_Result.QUES_ANS_PAIR[
                    'LARGE_SIZE_FILE']
                print(f' For filesize Result is --> LARGE_SIZE_FILE')
            elif (
                    answer_choice_1_1 < 2
                    and answer_choice_2 == 'GB'
            ) or (
                    answer_choice_1_1 < 50
                    and answer_choice_2 == 'MB'
            ):
                self.result_text += Survey_Result.QUES_ANS_PAIR[
                    'SMALL_SIZE_FILE']
            print(f' For filesize Result is --> SMALL_SIZE_FILE')

        else:
            self.result_text += ' '

        return self.result_text

    def importance_choice(self, all_survey_answers: Dict) -> str:
        is_valid_answer: bool = self.validate_answer_selection_in_dictionary(
            all_survey_answers
        )
        if is_valid_answer:
            self.result_text += '\n'
            answer_choice_dict: Dict = all_survey_answers['IMPORTANCE']
            key1, list_of_choice1 = answer_choice_dict.keys(), \
                                    answer_choice_dict.values()
            print(f' Bash {key1} and {list_of_choice1}')
            for key, list_of_choice in answer_choice_dict.items():
                print(key)
                print(list_of_choice)
                if key == 'LOW':
                    self.result_text += (
                        Survey_Result.QUES_ANS_PAIR[
                            'LOW_IMPORTANCE'
                        ]
                    )
                elif key == 'MEDIUM':
                    self.result_text += (
                        Survey_Result.QUES_ANS_PAIR[
                            'MEDIUM_IMPORTANCE'
                        ]
                    )
                elif key == 'HIGH':
                    if (
                            'Recovery' in list_of_choice and
                            'Analysis' in list_of_choice
                    ):
                        self.result_text += (
                            Survey_Result.QUES_ANS_PAIR[
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
                        Survey_Result.QUES_ANS_PAIR[
                            'HIGH_IMPORTANCE_SEL_2'
                        ]
                    )
                    print(f'IMPORTANCE Result is --> '
                          f'HIGH_IMPORTANCE_SEL_1')
                else:
                    self.result_text += (
                        Survey_Result.QUES_ANS_PAIR[
                            'NONE_IMPORTANCE'
                        ]
                    )

        return self.result_text


surveyQuestion = Question()
# answerEnvironment = Answers_Environment()
allAnswers = Dicts_Answer()
# HTML_SURVEY: Dict = {}

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
#
# HTML_SURVEY: Dict = {
#     'ENVIRONMENT': Q1_ANSW,
#     'AUDIT_TYPES': Q2_ANSW,
#     'AUDIT_CRITERIA': Q3_ANSW,
#     'SIZE': Q4_ANSW,
#     'IMPORTANCE': Q5_ANSW
# }

surveyresult = Survey_Choices()
# report_result: str = surveyresult.survey_choice(all_survey_answers=HTML_SURVEY)
HTML_SURVEY: Dict = {'ENVIRONMENT': Q1_ANSW, }
surveyresult.environment_choice(all_survey_answers=HTML_SURVEY)
HTML_SURVEY: Dict = {'AUDIT_TYPES': Q2_ANSW}
surveyresult.audittype_choice(all_survey_answers=HTML_SURVEY)
HTML_SURVEY: Dict = {'AUDIT_CRITERIA': Q3_ANSW}
surveyresult.auditcriteria_choice(all_survey_answers=HTML_SURVEY)
# HTML_SURVEY: Dict = {'SIZE': Q4_ANSW}
surveyresult.filesize_choice(all_survey_answers=Q4_ANSW)

HTML_SURVEY: Dict = {'IMPORTANCE': Q5_ANSW}
# print(HTML_SURVEY)
surveyresult.importance_choice(all_survey_answers=HTML_SURVEY)

# HTML_SURVEY: Dict = {'IMPORTANCE': Q5_ANSW}
# report_result: str = surveyresult.environment_choice(
#     all_survey_answers=HTML_SURVEY)

# survey_result()
print_result: str = surveyresult.result_text
print(f' After the complete survery, the results are ----> \n {print_result}')
# surveyresult.survey_result(result=print_result)
