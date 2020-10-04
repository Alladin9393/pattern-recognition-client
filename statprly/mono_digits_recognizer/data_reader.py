"""
Provide implementation of the DataReader.
"""


class DataReader:
    """
    Implementation of the DataReader.
    """

    def __init__(self, digit_standards_path):
        self.digit_standards_path = digit_standards_path

    def get_digit_standards_dict(self) -> dict:
        """
        Read data from `seed_data_path`.

        Read data from `digit_standards_path` and transform it into `dictionary` object
        where the key is the digit, value is the array of digit image data (array of `1` and `0`).
        """

    @staticmethod
    def __validate_data(data: list):
        """
        Digit standards data validation.

        :param data: digit data to be validated
        """
