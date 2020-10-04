"""
Provide constants for `Statprly` pattern recognition package.
"""
from os.path import dirname

MOST_LIKELY_OUTCOME = 1
DIGIT_STANDARDS_PATH = (
    dirname(__file__) + "/mono_digits_recognizer/digit_standards/digits.json"
)
SUPPORTED_DIMENSION_OF_STANDARDS = 2
