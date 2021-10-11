from typing import Dict


class Answer:
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

    audit_type: Dict = {
        'SCRIPT_LOGS': (
            'Shell scripts that write standard output to text log '
            'files with .log extension.'
        ),
        'BINARY_LOGS': 'Informatica session logs with .bin extension.',
        'PYTHON_ETL': 'Execute specific python apis for data audit.',
        'NEW': 'Audits unidentified and need to be coded.'
    }

    audit_criteria: Dict = {
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

    importance: Dict = {
        'HIGH': 'Must not skip any day.',
        'MEDIUM': 'The data gets refreshed on next cycle.',
        'LOW': 'Good to have audits',
        'IF HIGH': 'Frequency, daily, weekly, hourly......'
    }


class SurveyResult:
    QUES_ANS_PAIR: Dict = {
        'ETL_LOG': (
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
        'ANAPLAN_LOG': (
            'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur'
            ' adipiscing elit. Ut et augue id leo egestas interdum in eu '
            'lectus. Aliquam vel finibus nisi. Vestibulum mattis sagittis '
            'lectus sed pulvinar. Sed aliquam felis tortor, sed scelerisque '
            'nibh cursus sit amet. Donec a sollicitudin nisi. Mauris non enim '
            'ac felis lobortis commodo. Sed laoreet tellus non felis rutrum, '
            'in hendrerit ipsum porta. Sed quis sem velit.'
        ),
        'ANAPLAN_DATA_QUALITY': (
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
        'SHELL_OR_FILES': (
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
        'SHELL_PYTHON_OUTPUT': (
            'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1'
            ' or ANSWER_3 tincidunt venenatis risus. Vestibulum imperdiet enim'
            ' at nibh sodales, eget scelerisque odio finibus. Nullam ut mi eget'
            ' sapien accumsan iaculis. Vestibulum in maximus metus, vitae '
            'venenatis sapien. Nullam auctor odio vehicula, posuere elit in, '
            'ullamcorper lectus. Mauris pharetra dapibus congue. 2. Question - '
            'ANSWER_1 or ANSWER_3 Suspendisse potenti.'
        ),
        'BINARY_LOG_AND_OTHERS': (
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
        'NLG_PLANNING_AND_SCLASS_AND_CXTSSATR': (
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
        'CXTSSATR_AND_NLG_PLANNING_OR_SCLASS': (
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
        'NLG_GOALING_OR_SCLASS_CONTAINER2': (
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
        'LARGE_SIZE_FILE': (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Calories: ..... Vivamus hendrerit arcu eros, nec bibendum mi'
            ' sodales id. Ut auctor nisl a placerat porttitor. Duis at tortor '
            'posuere, gravida sapien in, fermentum ligula. '
            ''
            'Quisque eu ipsum lobortis, hendrerit justo vitae, varius nisi.'
            'Etiam in leo feugiat purus facilisis tempor.Fusce congue metus '
            'non massa mollis, id imperdiet ex viverra.Cras Calories:.....'
            'imperdiet lectus at imperdiet ornare.'
        ),
        'SMALL_SIZE_FILE': (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Integer porta at odio ac rhoncus. Calories: ..... Integer viverra'
            ' porta eros nec ultrices. Nullam ante sem, tincidunt vitae orci '
            'id, vestibulum auctor risus. Phasellus sit amet lobortis eros. '
            'Maecenas convallis dolor ex, vel congue ipsum ornare eu. '
            ''
            'Nunc in mattis dolor, quis posuere lorem. Calories: ..... Nullam '
            'condimentum semper diam, lacinia tempor eros tristique ut. Etiam '
            'ultrices imperdiet tortor at eleifend. Aenean lorem felis, '
            'volutpat eu euismod at, congue id erat. Duis luctus quam vitae'
            ' mattis tempus.'
        ),
        'HIGH_IMPORTANCE_SEL_1': (
            'Mauris viverra lobortis ante, eget faucibus felis pulvinar et. '
            'Suspendisse urna diam, ANSWER_YES and ANSWER_YES_CHOICE_2, '
            'ANSWER_YES_CHOICE_3 elementum nec tincidunt ornare, convallis '
            'condimentum nisi.'
            ''
            'Nam gravida ac magna eget cursus. ANSWER_YES and '
            'ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 Maecenas fermentum '
            'lacus eu tempor condimentum. Quisque tristique viverra justo,et'
            ' mollis magna ornare a. In lacus elit, vestibulum a ex facilisis,'
            ' faucibus gravida dui. Morbi consectetur egestas tempor. Sed '
            'neque ex, condimentum congue facilisis non,aliquet sed odio.'
        ),
        'HIGH_IMPORTANCE_SEL_2': (
            'Fusce sem est, maximus ac efficitur in, accumsan eu libero. '
            'Praesent facilisis, augue at pretium malesuada, ANSWER_YES '
            'and ANSWER_YES_CHOICE_1, ANSWER_YES_CHOICE_4 erat eros eleifend '
            'velit, at iaculis nunc nisi nec odio. Ut consequat ac metus a '
            'bibendum. Donec venenatis euismod eros ac dignissim. Donec dictum'
            ' odio a augue tincidunt interdum.'
        ),
        'MEDIUM_IMPORTANCE': (
            'Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod tellus id, '
            'sagittis felis. Nullam viverra est nibh, et dignissim elit '
            'tincidunt nec. Integer vel dolor aliquam, eleifend metus in, '
            'tincidunt erat. Nam id facilisis tortor. '
            ''
            'Donec malesuada, libero nec tincidunt ANSWER_I_DONT_KNOW commodo,'
            ' nulla velit imperdiet mauris, sit amet cursus dui quam maximus '
            'justo. In accumsan nisi ut orci finibus ullamcorper. Aliquam '
            'consequat risus non orci dapibus, id commodo erat egestas. '
        ),
        'LOW_IMPORTANCE': (
            'Nam maximus et massa laoreet congue. In facilisis egestas neque. '
            'Nullam ac euismod nibh. ANSWER_NO Aenean pulvinar lacinia ligula,'
            ' nec lobortis magna accumsan sed. '
            ''
            'Duis tempor pellentesque quam. ANSWER_NO Sed non est dui. Sed '
            'commodo odio vel augue pellentesque, et sagittis dolor tristique.'
            ' Phasellus mollis magna eu egestas viverra. Cras elementum erat '
            'vel libero venenatis, ut suscipit nibh scelerisque.'
        ),
        'NONE_IMPORTANCE': (
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Pellentesque sed scelerisque nulla, at mattis mauris. Vestibulum'
            ' dignissim viverra nulla quis tempus. (Any other case) Donec '
            'finibus nisl sapien, sed auctor elit sodales ac. Nulla dictum '
            'ante ante, eget maximus mi efficitur nec.'
        )
    }
