"""
Provide implementation of the recognition of the monochrome digits.
"""
from numpy import array

from statprly.constants import (
    DIGIT_STANDARDS_PATH,
    MOST_LIKELY_OUTCOME,
)
from statprly.mono_digits_recognizer.data_reader import DataReader
from statprly.mono_digits_recognizer.interfaces import BaseRecognizer


class MonoDigitRecognizer(BaseRecognizer):
    """
    Implementation of the monochrome digits recognizer.
    """

    def __init__(
        self,
        data_provider=DataReader,
        digit_standards_path=DIGIT_STANDARDS_PATH,
    ):
        self._digit_standards_path = digit_standards_path
        self._data_provider = data_provider(
            digit_standards_path=self._digit_standards_path,
        )
        self._digit_standards = self._data_provider.get_digit_standards_dict()

    def recognize(self, digit_to_predict: array, noise_probability: float) -> int:
        """
        Predict number from `digit_to_predict` matrix.

        :param digit_to_predict: displaying an image of a digit to numpy array `1` and `0`.
        :param noise_probability: the probability of the noise in digit_to_predict data array.
        :return: predicted number.
        """
        possible_exodus = range(0, 10)
        digits_probabilities = {}
        for exodus in possible_exodus:
            digit_probability = self.get_digit_probability(
                array,
                exodus,
                noise_probability,
            )

            if digit_probability == MOST_LIKELY_OUTCOME:
                return exodus

            digits_probabilities[exodus] = digit_probability

        most_likely_outcome = max(digits_probabilities, key=digits_probabilities.get)
        return most_likely_outcome

    def get_digit_probability(
        self,
        digit_data: array,
        digit_to_compare: int,
        noise_probability: float,
    ) -> float:
        """
        Get the probability of a digit behind its array.

        :param digit_data: displaying an image of a digit to numpy array `1` and `0`.
        :param digit_to_compare: the number of probability to be obtained.
        :param noise_probability: the probability of the noise in digit_to_predict data array.
        :return: probability.
        """
        return MOST_LIKELY_OUTCOME

    @property
    def digit_standards_path(self) -> str:
        """
        Get `digit_standards_path` variable.

        :return: `digit_standards_path` string value
        """
        return self._digit_standards_path

    @digit_standards_path.setter
    def digit_standards_path(self, value):
        """
        Set `digit_standards_path` value and get new basic dictionary of standards digits.

        :param value: `digit_standards_path` variable value
        """
        self._digit_standards_path = value
        self._digit_standards = self._data_provider.get_digit_standards_dict()

    @property
    def data_provider(self):
        """
        Get `data_provider` variable.

        :return: `data_provider` instance value
        """
        return self._data_provider

    @data_provider.setter
    def data_provider(self, value):
        """
        Set `data_provider` value and and get new basic dictionary of standards digits.

        :param value: `data_provider` variable value
        """
        self._data_provider = value(self._digit_standards_path)
        self._digit_standards = self._data_provider.get_digit_standards_dict()

    def __repr__(self):
        """
        Printable representation of the MonoDigitRecognizer.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self._digit_standards!r}, "
            f"{self._data_provider!r}, "
            f"{self._digit_standards_path!r}"
            f")"
        )
