import unittest
from typing import Dict

from report.survey_gen import Choices
from report.text import Text


class TestFileSize(unittest.TestCase):

    def test_answer_large_mb_file(self):
        test_answer: Dict = {
            'SIZE': 200,
            'UNIT': 'MB'
        }

        choices = Choices(answer={'FSIZE': test_answer})
        choices.filesize()
        text = Text()
        gb_to_mb: float = text.calc_gb_size(
            unit=test_answer['UNIT'],
            size=test_answer['SIZE']
        )

        self.assertEqual(
            choices.result_text,
            '\n' +
            text.large_size_in_megabytes(gb_size=gb_to_mb)
        )

    def test_answer_large_gb_file(self):
        test_answer: Dict = {
            'SIZE': 2,
            'UNIT': 'GB'
        }
        choices = Choices(answer={'FSIZE': test_answer})
        choices.filesize()
        text = Text()
        gb_to_mb: float = text.calc_gb_size(
            unit=test_answer['UNIT'],
            size=test_answer['SIZE']
        )

        self.assertEqual(
            choices.result_text,
            '\n' +
            text.large_size_in_megabytes(gb_size=gb_to_mb)
        )

    def test_answer_small_gb_file(self):
        test_answer: Dict = {
            'SIZE': 1,
            'UNIT': 'GB'
        }
        choices = Choices(answer={'FSIZE': test_answer})
        choices.filesize()
        text = Text()
        gb_to_mb: float = text.calc_gb_size(
            unit=test_answer['UNIT'],
            size=test_answer['SIZE']
        )

        self.assertEqual(
            choices.result_text,
            '\n' +
            text.small_size_in_megabytes(gb_size=gb_to_mb)
        )

    def test_answer_small_mb_file(self):
        test_answer: Dict = {
            'SIZE': 49,
            'UNIT': 'MB'
        }

        choices = Choices(answer={'FSIZE': test_answer})
        choices.filesize()
        text = Text()
        gb_to_mb: float = text.calc_gb_size(
            unit=test_answer['UNIT'],
            size=test_answer['SIZE']
        )
        self.assertEqual(
            choices.result_text,
            '\n' +
            text.small_size_in_megabytes(gb_size=gb_to_mb)
        )
