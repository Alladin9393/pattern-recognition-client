"""
Provide tests for DataReader.
"""
from os.path import dirname

import pytest

from statprly.mono_digits_recognizer.data_reader import DataReader
from statprly.errors import ValidationDataError


def test_get_digit_standards_dictionary():
    """
    Case: get dictionary of digit standards.
    Expected: dictionary is returned.
    """
    custom_data_path = dirname(__file__) + '/custom_standardts_data/mock_data_to_recognize.json'
    data_reader = DataReader(digit_standards_path=custom_data_path)
    base_dict = data_reader.get_digit_standards_dict()

    assert len(base_dict) != 0


def test_get_digit_standards_dictionary_with_invalid_data():
    """
    Case: get dictionary of digit standards with invalid data.
    Expect: invalid pixel in data error message.
    """
    invalid_data_path = dirname(__file__) + '/custom_standardts_data/invalid_data.json'
    data_reader = DataReader(digit_standards_path=invalid_data_path)

    with pytest.raises(ValidationDataError):
        data_reader.get_digit_standards_dict()


def test_get_digit_standards_dictionary_with_invalid_shape():
    """
    Case: get dictionary of digit standards with invalid shape.
    Expect: data shape validation error message.
    """
    invalid_data_path = dirname(__file__) + '/custom_standardts_data/invalid_shape_in_data.json'
    data_reader = DataReader(digit_standards_path=invalid_data_path)

    with pytest.raises(ValidationDataError):
        data_reader.get_digit_standards_dict()


def test_get_dictionary_by_word_len_with_non_existing_data_path():
    """
    Case: get dictionary of digit standards with non-existing data path.
    Expect: no such file or directory error message.
    """
    data_reader = DataReader(digit_standards_path='')
    with pytest.raises(FileNotFoundError):
        data_reader.get_digit_standards_dict()
