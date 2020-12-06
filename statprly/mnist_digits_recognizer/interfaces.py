"""
Provide interfaces for `mnist` digits recognizer.
"""
from abc import (
    ABC,
    abstractmethod,
)

import numpy as np


class BaseRecognizer(ABC):
    """
    Implementation of the basic recognizer.
    """

    @abstractmethod
    def train(self, x_train: np.array, max_iteration: int):
        """
        Train recognizer by ` based on `x_train` and `y_train` data.

        :param x_train: digit data to train recognizer.
        :param max_iteration: max iteration of the training.
        """

    @abstractmethod
    def predict(self, digit_data_to_predict: np.array) -> int:
        """
        Predict digit by digit data.

        :param digit_data_to_predict: digit data to be predicted.
        :return: predicted digit label.
        """
