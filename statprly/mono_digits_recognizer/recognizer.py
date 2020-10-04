"""
Provide implementation of the recognition of the monochrome digits.
"""
from numpy import array

from statprly.constants import MOST_LIKELY_OUTCOME
from statprly.mono_digits_recognizer.interfaces import BaseRecognizer


class MonoDigitRecognizer(BaseRecognizer):
    """
    Implementation of the monochrome digits recognizer.
    """

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
