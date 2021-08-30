from typing import Dict


class Question:
    Question_types: Dict = {
        'COFFEE_ADDITIONS': (
            'If you drink Ccffee, which statement would '
            'best describe how you drink it'
        ),
        'COFFEE_STRENGTH': 'If you drink coffee or tea, do you like it',
        'COCKTAILS': (
            'If you occasionally drink cocktails or distilled spiris, '
            'which would be more likely to choose multiple choices can be '
            'selected'
        ),
        'WEIGHT': 'What is your current weight',

        'ALLERGIES': (
            'Do you have any food allergies that might affect your wine '
            'choice'
        )
    }


class Answers_Coffee_Additions:
    Addition_types: Dict = {
        'SUGAR_CREAM': (
            'Add sugar, or sugar ( or sweetener) and cream'
        ),
        'CREAM': 'Add cream only',
        'LEMON': 'Add lemon only',
        'BLACK': 'Take it straight without sugar or cream',
        'NA': 'Don\'t drink coffee'
    }


class Answers_Coffee_Stremgth:
    Strength: Dict = {
        'FAIR': 'Failr strong',
        'AVERGAE': 'Average Strength',
        'LiGHT': 'Mostly on the weak side',
        'ANY': 'ANy strength but cut with sugar or sweetener'
    }


class Answers_Cocktails:
    Cocktails: Dict = {
        'MARTINI': 'Martini',
        'BOURBON': 'Bourbon or Scotch',
        'MARGARITA': 'Margarita',
        'COSMO': 'Mai/Tai or Cosmopolitan',
        'SPARKLING': 'Sparkling Wine',
        'RARE': 'Rarely drink spirits or cocktails'
    }


class Answers_Weight:
    pass


class Answers_Allergies:
    Allergies: Dict = {
        'NO': 'No',
        'NK': 'Don\'t know',
        'YES': 'Yes',
        'YES CHOICE': 'Chicken, Wheat, Soy......'
    }


class Wine_Result:
    Wine_pairings: Dict = {
        'STRONG_COFFEE': 'Robust red with an espresso shot - perfect balance.',
        'COFFEE_CREAM': 'California Merlots',
        'MILD_COFFEE': (
            'Cabernet Sauvignon Rose are a good choice. Several other Roses '
            'are there providing dry to sweet wine.'
        ),
        'LEMON_PAIRING': (
            'THis is not known to me much. I could recommend Pinot Noir, '
            'which is very light red wine.'
        ),
        'ALLERGIES': 'White wine allergies are well-known.'
    }

    Wine_scores: Dict = {
        'Merlot': 1,
        'Cabernet Savignon': 1,
        'Pinot Noir': 1,
        'Pinot Griogio': 1,
        'Zinfandel': 1,
        'Champagne': 1,
        'Dessert': 1,
        'Moscato': 1,
        'Sparkling': 1,
        'Blend': 1,
        'Chardonnay': 1,
        'Reisling': 1,
        'Syrah': 1,
        'Shiraz': 1
    }

    def survey_result(self, score: int) -> str:
        pass

    def survey_choice(self, **question: str):
        question_one: str = question[0]
        question_two: str = question[1]

        if question_one:
            if (
                    Answers_Coffee_Additions.Addition_types.keys() =
            'SUGAR_CREAM'
            ):
                self.Wine_scores['Shiraz'] += 1

            elif (
                    Answers_Coffee_Additions.Addition_types.keys() =
            'CREAM'
            ):
                self.Wine_scores['Pinot Noir'] += 1
            elif (
                    Answers_Coffee_Additions.Addition_types.keys() =
            'LEMON'
            ):
                self.Wine_scores['Chardonnay'] += 1
                self.Wine_scores['Sparkling'] += 1
        if question_two:
            if Answers_Coffee_Stremgth.Strength.keys() = 'FAIR':
                self.Wine_scores['Pinot Noir'] += 1
                self.Wine_scores['Pinot Grigio'] += 1
                self.Wine_scores['Merlot'] += 1
