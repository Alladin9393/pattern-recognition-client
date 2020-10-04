"""
Provide tests for MonoDigitRecognizer.
"""
import json
import random
from os.path import dirname

import numpy

from statprly import MonoDigitRecognizer

with open(dirname(__file__) + '/custom_standardts_data/mock_data_to_recognize.json') as f:
    MOCK_DATA_TO_RECOGNIZE = json.loads(f.read())


def test_recognize_random_digit():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    digit_data_to_recognize = numpy.array(MOCK_DATA_TO_RECOGNIZE.get(digit_to_recognize))
    noise = random.random()
    recognize_digit = recognizer.recognize(digit_data_to_recognize, noise)

    mock_answer = 0  # TODO: REMOVE MOCKS
    assert recognize_digit == mock_answer


def test_recognize_random_digit_with_zero_noise():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    noise = 0
    recognize_digit = recognizer.recognize(MOCK_DATA_TO_RECOGNIZE.get(digit_to_recognize), noise)

    mock_answer = 0  # TODO: REMOVE MOCKS
    assert recognize_digit == mock_answer


def test_recognize_random_digit_with_hundred_percent_noise():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    recognizer = MonoDigitRecognizer()
    digit_to_recognize = random.randrange(10)
    noise = 1
    recognize_digit = recognizer.recognize(MOCK_DATA_TO_RECOGNIZE.get(digit_to_recognize), noise)

    mock_answer = 0  # TODO: REMOVE MOCKS
    assert recognize_digit == mock_answer


def test_get_digit_probability():
    """
    Case: recognize random digit.
    Expect: recognized digit is returned.
    """
    recognizer = MonoDigitRecognizer()
    digit_to_get_prob = random.randrange(10)
    noise = 1
    digit_prob = recognizer.get_digit_probability(
        MOCK_DATA_TO_RECOGNIZE.get(digit_to_get_prob),
        digit_to_get_prob,
        noise,
    )

    mock_answer_prob = 1  # TODO: REMOVE MOCKS
    assert digit_prob == mock_answer_prob
