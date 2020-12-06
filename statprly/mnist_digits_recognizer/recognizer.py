"""
Provide implementation of the `mnist` recognizer.
"""
import numpy as np

from statprly.constants import SUPPORTED_NUMBER_OF_MNIST_CLASSES
from statprly.mnist_digits_recognizer.interfaces import BaseRecognizer


class MNISTRecognizer(BaseRecognizer):
    """
    Implementation of the mnist recognizer.
    """

    def train(self, x_train: np.array, max_iteration: int):
        """
        Train recognizer by ` based on `x_train` and `y_train` data.

        :param x_train: digit data to train recognizer.
        :param max_iteration: max iteration of the training.
        """

    def predict(self, digit_data_to_predict: np.array) -> int:
        """
        Predict digit by digit data.

        :param digit_data_to_predict: digit data to be predicted.
        :return: predicted digit label.
        """

    @staticmethod
    def _generate_aposterior_probabilities(size_of_split):
        """
        Generate aposterior probabilities `p(k|Xc)`.

        :param size_of_split: size of train data split.
        :return: random aposterior probabilities.
        """
        aposterior_probabilities = []
        random_matrix = np.random.randint(
            low=0,
            high=1000,
            size=(size_of_split, SUPPORTED_NUMBER_OF_MNIST_CLASSES),
        )

        matrix_row_sum = random_matrix.sum(axis=1)
        for i, prob in enumerate(random_matrix):
            aposterior_probabilities.append(prob / matrix_row_sum[i])

        return np.array(aposterior_probabilities)

    @staticmethod
    def _calculate_aprior_probabilities(aposterior_probabilities: np.array) -> np.array:
        """
        Calculate aprior probabilities `p(k)`.

        `p(k) = sum(p(k|x) / |x|`.

        :return: aprior probabilities `p(k)`.
        """
        return aposterior_probabilities.mean(axis=0)
