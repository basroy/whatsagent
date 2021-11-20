import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestFileSize(unittest.TestCase):

    def test_answer_large_file(self):
        test_answer: Dict = {
            'SIZE': 200,
            'UNIT': 'MB'
        }
        if test_answer['UNIT'] == 'GB':
            gb_to_mb: float = round(test_answer['SIZE'] * 1024, 2)

        else:
            gb_to_mb: float = round(test_answer['SIZE'], 2)

        choices = Choices(answer={'FSIZE': test_answer})
        choices.filesize()

        self.assertEqual(
            choices.result_text,
            '\n' +
            Text.large_size_in_megabytes(self, gb_size=gb_to_mb)
        )

    def test_answer_small_file(self):
        test_answer: Dict = {
            'SIZE': 1,
            'UNIT': 'GB'
        }
        if test_answer['UNIT'] == 'GB':
            gb_to_mb: float = round(test_answer['SIZE'] * 1024, 2)

        else:
            gb_to_mb: float = round(test_answer['SIZE'], 2)

        choices = Choices(answer={'FSIZE': test_answer})
        choices.filesize()

        self.assertEqual(
            choices.result_text,
            '\n' +
            Text.small_size_in_megabytes(self, gb_size=gb_to_mb)
        )
