"""
Provide tests for MonoDigitRecognizer.
"""
import json
import random
from os.path import dirname

import numpy
import pytest

from statprly import MonoDigitRecognizer
from statprly.constants import (
    LEAST_LIKELY,
    MOST_LIKELY,
)
from statprly.errors import ValidationDataError
from statprly.mono_digits_recognizer.standards_provider import StandardsProvider

DIRNAME = dirname(__file__)

ACCURACY = 0.7


def test_recognize_random_digit_with_random_noise_less_than_half():
    """
    Case: recognize random digit with random noise < 0.44 and scale.
    Expect: recognized digit is returned.
    """
    test_cases = 100

    with open(DIRNAME + "/custom_standardts_data/mock_data_to_recognize.json") as f:
        digit_data_to_recognize = json.loads(f.read())

    standards_provider = StandardsProvider()
    recognizer = MonoDigitRecognizer()

    number_of_success = 0
    for i in range(100):
        random_noise = numpy.random.uniform(0, 0.44)
        random_scale = random.randrange(20)
        expected_digit = random.randrange(10)

        digit_with_noise = standards_provider.get_scaled_standard_with_noise(
            digit_data=digit_data_to_recognize[str(expected_digit)],
            vertical_scale=random_scale,
            horizontal_scale=random_scale,
            noise_probability=random_noise,
        )
        digit_with_noise = numpy.array(digit_with_noise)

        recognized_digit = recognizer.recognize(
            digit_to_predict_data=digit_with_noise,
            noise_probability=random_noise,
        )

        is_success = recognized_digit == expected_digit
        number_of_success += int(is_success)

    accuracy = number_of_success / test_cases
    assert accuracy > ACCURACY


def test_recognize_random_digit_with_random_noise_more_than_half():
    """
    Case: recognize random digit with random noise > 0.6 and scale.
    Expect: recognized digit is returned.
    """
    test_cases = 100

    with open(DIRNAME + "/custom_standardts_data/mock_data_to_recognize.json") as f:
        digit_data_to_recognize = json.loads(f.read())

    standards_provider = StandardsProvider()
    recognizer = MonoDigitRecognizer()

    number_of_success = 0
    for i in range(100):
        random_noise = numpy.random.uniform(0.6, 1)
        random_scale = random.randrange(20)
        expected_digit = random.randrange(10)

        digit_with_noise = standards_provider.get_scaled_standard_with_noise(
            digit_data=digit_data_to_recognize[str(expected_digit)],
            vertical_scale=random_scale,
            horizontal_scale=random_scale,
            noise_probability=random_noise,
        )
        digit_with_noise = numpy.array(digit_with_noise)

        recognized_digit = recognizer.recognize(
            digit_to_predict_data=digit_with_noise,
            noise_probability=random_noise,
        )

        is_success = recognized_digit == expected_digit
        number_of_success += int(is_success)

    accuracy = number_of_success / test_cases
    assert accuracy > ACCURACY


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
