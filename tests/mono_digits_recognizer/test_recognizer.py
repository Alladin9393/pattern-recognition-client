"""
Provide tests for MonoDigitRecognizer.
"""
import json
import random
from os.path import dirname

import pytest
import numpy

from statprly import MonoDigitRecognizer
from statprly.errors import ValidationDataError
from statprly.constants import (
    MOST_LIKELY,
    LEAST_LIKELY,
)

DIRNAME = dirname(__file__)


def test_recognize_random_digit_with_zero_noise():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    with open(DIRNAME + "/custom_standardts_data/mock_data_to_recognize.json") as f:
        digit_data_to_recognize = json.loads(f.read())

    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    digit_to_recognize_data = numpy.array(
        digit_data_to_recognize.get(str(digit_to_recognize)),
    )
    noise = LEAST_LIKELY
    recognized_digit = recognizer.recognize(
        digit_to_recognize_data,
        noise,
    )
    assert recognized_digit == digit_to_recognize


def test_recognize_random_digit_with_hundred_percent_noise():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    with open(DIRNAME + "/custom_standardts_data/inversed_digit_standards.json") as f:
        digit_data_to_recognize = json.loads(f.read())

    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    digit_to_recognize_data = numpy.array(
        digit_data_to_recognize.get(str(digit_to_recognize)),
    )
    noise = MOST_LIKELY
    recognized_digit = recognizer.recognize(
        digit_to_recognize_data,
        noise,
    )

    assert recognized_digit == digit_to_recognize


def test_get_digit_probability():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    with open(DIRNAME + "/custom_standardts_data/inversed_digit_standards.json") as f:
        digit_data_to_get_prob = json.loads(f.read())

    recognizer = MonoDigitRecognizer()
    digit_to_get_prob = random.randrange(10)
    digit_to_get_prob_data = numpy.array(
        digit_data_to_get_prob.get(str(digit_to_get_prob)),
    )
    noise = MOST_LIKELY
    digit_prob = recognizer.get_digit_probability(
        digit_to_get_prob_data,
        digit_to_get_prob,
        noise,
    )

    assert digit_prob == MOST_LIKELY


def test_recognize_random_digit_with_invalid_digit_data_type():
    """
    Case: recognize digit with invalid digit data type.
    Expect: `digit_to_predict_data` must be a numpy array data error message.
    """
    with open(DIRNAME + "/custom_standardts_data/mock_data_to_recognize.json") as f:
        digit_data_to_recognize = json.loads(f.read())

    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    noise = LEAST_LIKELY
    with pytest.raises(ValidationDataError):
        recognizer.recognize(
            digit_data_to_recognize.get(str(digit_to_recognize)),
            noise,
        )


def test_recognize_random_digit_with_invalid_noise():
    """
    Case: recognize digit with invalid digit data type.
    Expect: `digit_to_predict_data` must be a numpy array data error message.
    """
    with open(DIRNAME + "/custom_standardts_data/mock_data_to_recognize.json") as f:
        digit_data_to_recognize = json.loads(f.read())

    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    negative_noise = random.randrange(-100, -1)
    positive_noise = random.randrange(1, 100)

    with pytest.raises(ValidationDataError):
        recognizer.recognize(
            digit_data_to_recognize.get(str(digit_to_recognize)),
            negative_noise,
        )

    with pytest.raises(ValidationDataError):
        recognizer.recognize(
            digit_data_to_recognize.get(str(digit_to_recognize)),
            positive_noise,
        )
