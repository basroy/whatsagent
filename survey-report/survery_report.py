from typing import Dict, List


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

        'IMPORTANCE': (
            'How does the audits help the organization?'
        )
    }


class Answers_Environment:
    Environment: Dict = {
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
        'IF HIGH': 'Frequency, daily, weekly, hourly......'
    }


class Survey_Result:
    QUES_ANS_PAIR: Dict = {
        'Q1_A1': (
            'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur '
            'adipiscing elit. Mauris sed ligula vitae tellus pellentesque '
            'vehicula nec eu velit. Curabitur luctus et nibh et ornare. '
            'Suspendisse non mattis lacus. Cras vitae mi ornare, euismod velit'
            ' sit amet, iaculis tortor. In tempor purus sapien.'
            '\n'
            'Donec tincidunt 1. Question - ANSWER_1 metus nec dui tristique'
            'malesuada.Praesent lectus nunc, accumsan vel justo in, imperdiet'
            'faucibus leo.Nullam efficitur massa nec turpis tincidunt, feugiat'
            'viverra erat rutrum.Aliquam eget auctor lectus, mollis bl andit '
            'ipsum.Phasellus maximus finibus arcu a tincidunt.'
        ),
        'Q1_A2': (
            'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur'
            ' adipiscing elit. Ut et augue id leo egestas interdum in eu '
            'lectus. Aliquam vel finibus nisi. Vestibulum mattis sagittis '
            'lectus sed pulvinar. Sed aliquam felis tortor, sed scelerisque '
            'nibh cursus sit amet. Donec a sollicitudin nisi. Mauris non enim '
            'ac felis lobortis commodo. Sed laoreet tellus non felis rutrum, '
            'in hendrerit ipsum porta. Sed quis sem velit.'
        ),
        'Q1_A3': (
            'Sed vel bibendum tortor. Proin a aliquet tortor. Vivamus rhoncus'
            ' 1. Question - ANSWER_3 risus nec ultricies rutrum. Mauris '
            'bibendum lectus risus, non porttitor urna interdum quis. '
            ''
            'Suspendisse quis risus scelerisque, 1. Question - ANSWER_3 '
            'feugiat augue nec, semper leo. Fusce euismod facilisis mi, '
            'tristique sollicitudin metus hendrerit non. Nulla ac sodales '
            'quam, sit amet finibus metus. Ut in felis tellus. Sed aliquet'
            ' metus ullamcorper est vestibulum mattis. Cras nisi sem, euismod'
            ' in egestas vel, ullamcorper ac sapien. In porttitor elementum'
            ' faucibus.'
        ),
        'Q1_A4': (
            'Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis '
            'risus. Vestibulum imperdiet enim at nibh sodales, 1. Question - '
            'ANSWER_4 or ANSWER_5 or ANSWER_6 eget scelerisque odio finibus.'
            ''
            'Nullam ut mi eget sapien accumsan iaculis. Vestibulum in maximus '
            'metus, 1. Question - ANSWER_4 or ANSWER_5 or ANSWER_6 vitae '
            'venenatis sapien. Nullam auctor odio vehicula, posuere elit in,'
            ' ullamcorper lectus. Mauris pharetra dapibus congue. Suspendisse'
            ' potenti.'
        ),
        'Q2_A1': (
            'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1'
            ' or ANSWER_3 tincidunt venenatis risus. Vestibulum imperdiet enim'
            ' at nibh sodales, eget scelerisque odio finibus. Nullam ut mi eget'
            ' sapien accumsan iaculis. Vestibulum in maximus metus, vitae '
            'venenatis sapien. Nullam auctor odio vehicula, posuere elit in, '
            'ullamcorper lectus. Mauris pharetra dapibus congue. 2. Question - '
            'ANSWER_1 or ANSWER_3 Suspendisse potenti.'
        ),
        'Q2_A2': (
            'In nisl ligula, porttitor vel lobortis vel, commodo quis mi.'
            ' Nullam sollicitudin odio ut felis tristique tempus. Cras sagittis'
            ' auctor nulla 2. Question - ANSWER_2 or ANSWER_4 eget accumsan. '
            'Nam condimentum lacus non tortor auctor semper.'
            ''
            'Suspendisse justo nisi, molestie quis purus sed, dapibus porta '
            'urna. Praesent leo massa, aliquet blandit eros at, consectetur '
            'vestibulum elit. Aliquam laoreet ex ex, et dapibus 2. Question -'
            'ANSWER_2 or ANSWER_4 ligula interdum a. Praesent quis libero arcu.'
            ' Donec felis libero, tristique et sapien non, feugiat eleifend '
            'diam.'
        ),
        'Q3_A1': (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed '
            'sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1'
            ' lectus cursus tincidunt. Nullam dapibus tincidunt libero nec '
            'volutpat. '
            ''
            'Cras sit amet massa a turpis malesuada ornare vitae '
            'sed arcu. Maecenas eleifend rutrum augue, eget imperdiet sem '
            'gravida sed. Vestibulum vel libero consectetur, 3. Question - '
            'ANSWER_4, ANSWER_3 and ANSWER_1 pellentesque lacus nec, facilisis'
            ' nisl. Phasellus faucibus lobortis tincidunt. Duis tristique '
            'congue bibendum.'
            ''
            'Morbi semper cursus felis et consequat. Nulla posuere, quam eget'
            ' pulvinar 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 dignissim,'
            ' odio sem euismod leo, at ornare purus massa quis sapien. Aliquam'
            ' eget libero nec lectus placerat congue. Aenean nec tortor a '
            'ligula aliquam pharetra. Aenean et magna enim.'
        ),
        'Q3_A2': (
            'orem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Vestibulum dictum, dui non auctor tristique, odio sem 3. Question'
            ' - ANSWER_2 and ANSWER_5 convallis lacus, non gravida libero erat'
            ' id justo. Praesent in varius nisi. Phasellus suscipit elit sit '
            'amet aliquam tincidunt.'
            ''
            'In pellentesque gravida risus, et 3. Question - ANSWER_2 and '
            'ANSWER_5 rhoncus quam. Vestibulum ac risus nulla. Phasellus '
            'iaculis interdum pulvinar. Vivamus sit amet sagittis risus. Morbi'
            ' ut pellentesque sapien.'
        ),
        'Q3_A3': (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras '
            'viverra luctus nunc, non ultrices mauris molestie vitae. Sed gravida'
            ' purus finibus 3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 '
            'efficitur congue. Vestibulum magna urna, volutpat vitae auctor non,'
            ' pharetra vel leo.Interdum et malesuada fames ac ante ipsum primis'
            ' in faucibus. Vestibulum elementum sagittis tortor, vel porta leo '
            'tristique ac. Phasellus ac metus est. 3. Question - ANSWER_4,'
            ' ANSWER_3 or ANSWER_1 Aenean vel malesuada ex, nec rutrum justo.'
            ' Sed ultricies venenatis mauris, in pharetra ante vulputate nec. '
            'Proin viverra convallis augue elementum volutpat.'
        ),
    }

    def survey_result(self, result: str):
        print(result)

    def survey_choice(self, question: Dict) -> str:
        result_text: str = ''

        for key, answer_choice in question.items():
            if key == 'ENVIRONMENT':
                answer_choice: str = answer_choice[0]
                if answer_choice == 'ETL_LOGS':
                    result_text = Survey_Result.QUES_ANS_PAIR['Q1_A1']
                    print(f' For environment Result is --> Q1_A1')
                elif answer_choice == 'ANAPLAN_LOGS':
                    result_text = Survey_Result.QUES_ANS_PAIR['Q1_A2']
                    print(f' For environment Result is --> Q1_A2')
                elif answer_choice == 'ANAPLAN_DATA':
                    result_text = Survey_Result.QUES_ANS_PAIR['Q1_A3']
                    print(f' For environment Result is --> Q1_A2')
                elif answer_choice == 'SHELL' or answer_choice == 'FILES':
                    result_text = Survey_Result.QUES_ANS_PAIR['Q1_A4']
                    print(f' For environment Result is --> Q1_A4')
            elif key == 'AUDIT_TYPES':
                answer_choice: str = answer_choice[0]
                if (
                        answer_choice == 'SCRIPT_LOGS'
                        or answer_choice == 'PYTHON_ETL'
                ):
                    result_text += Survey_Result.QUES_ANS_PAIR['Q2_A1']
                    print(f' For environment Result is --> Q2_A1')
                elif answer_choice == 'BINARY_LOGS' or answer_choice == 'NEW':
                    result_text = Survey_Result.QUES_ANS_PAIR['Q2_A2']
                    print(f' For environment Result is --> Q2_A2')

            elif key == 'AUDIT_CRITERIA':
                print(answer_choice)
                answer_choice_1, answer_choice_2, answer_choice_3 = \
                    answer_choice[0], answer_choice[1], answer_choice[2]

                if (
                        answer_choice_1 == 'CX_TSS_ATR'
                        or answer_choice_1 == 'SCLASS_INVALID_PARTY'
                        or answer_choice_1 == 'NLG_PLANNING'
                ) and (
                        answer_choice_2 == 'CX_TSS_ATR'
                        or answer_choice_2 == 'SCLASS_INVALID_PARTY'
                        or answer_choice_2 == 'NLG_PLANNING'
                ) and (
                        answer_choice_3 == 'CX_TSS_ATR'
                        or answer_choice_3 == 'SCLASS_INVALID_PARTY'
                        or answer_choice_3 == 'NLG_PLANNING'
                ):
                    result_text += Survey_Result.QUES_ANS_PAIR['Q3_A1']
                    print(f' For AUDIT_CRITERIA Result is --> Q3_A1')
                elif (
                        answer_choice_1 == 'NLG_GOALING'
                        or answer_choice_2 == 'SCLASS_CONTAINER'
                ):
                    result_text = Survey_Result.QUES_ANS_PAIR['Q3_A3']
                    print(f' For AUDIT_CRITERIA Result is --> Q3_A3')
                elif (
                        answer_choice_1 == 'CX_TSS_ATR' and
                        (
                                answer_choice_2 == 'SCLASS_INVALID_PARTY'
                                or answer_choice_3 == 'NLG_PLANNING'
                        )
                ):
                    result_text += Survey_Result.QUES_ANS_PAIR['Q3_A2']
                    print(f' For AUDIT_CRITERIA Result is --> Q3_A2')

        return result_text


surveyQuestion = Question()
answerEnvironment = Answers_Environment()
HTML_SURVEY: Dict = {}
# print(surveyQuestion.Question_types.items())
for key, question in surveyQuestion.Question_types.items():
    # print(question)
    # print(surveyQuestion.Question_types[key])
    if key == 'ENVIRONMENT':
        qans: List = ['ETL_LOGS']
    elif key == 'AUDIT_TYPES':
        qans: List = ['SCRIPT_LOGS']
    elif key == 'AUDIT_CRITERIA':
        qans: List = ['CX_TSS_ATR', 'SCLASS_INVALID_PARTY',
                      'NLG_PLANNING']
    elif key == 'SIZE':
        qans: List = ['2:GB']
    else:
        qans: str = 'No selection'
    HTML_SURVEY[key] = qans

print(HTML_SURVEY)
surveyresult = Survey_Result()
report_result: str = surveyresult.survey_choice(question=HTML_SURVEY)
print(report_result)
