"""
Provide implementation of the `mnist` digits provider.
"""
import pickle
from typing import Tuple

import numpy as np

from statprly.constants import MNIST_DIGITS_DATA_PATH


class MNISTProvider:
    """
    Implementation of the `mnist` provider.
    """

    def __init__(self, mnist_data_path=MNIST_DIGITS_DATA_PATH):
        self.mnist_data_path = mnist_data_path

    @property
    def mnist_data_path(self):
        """
        Get `mnist_data_path`.

        :return: path to the `mnist` digits data.
        """
        return self._mnist_data_path

    @mnist_data_path.setter
    def mnist_data_path(self, data_path: str):
        """
        Set `mnist_data_path` and load new data.
        """
        self._mnist_data_path = data_path
        self.x_train, self.y_train, self.x_test, self.y_test = self.__load_mnist_data(
            self._mnist_data_path,
        )

    def __load_mnist_data(
        self,
        mnist_data_path: str,
    ) -> Tuple[np.array, np.array, np.array, np.array]:
        """
        Load and prepare mnist data from `mnist_data_path`.

        :param mnist_data_path: path to the mnist digits data.
        :return: tuple of the x_train, y_train x_test, y_test
        """
        with open(mnist_data_path, "rb") as f:
            self.mnist_data = pickle.load(f)

        x_train = self.mnist_data["training_images"]
        y_train = self.mnist_data["training_labels"]
        x_test = self.mnist_data["test_images"]
        y_test = self.mnist_data["test_labels"]
        # Reshaping the array to 4-dims.
        x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
        x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
        # Making sure that the values are float so that we can get decimal points after division.
        x_train = x_train.astype("float32")
        x_test = x_test.astype("float32")
        # Normalizing the RGB codes by dividing it to the max RGB value.
        x_train /= 255
        x_test /= 255

        y_train_zeros_idx = np.where(y_train == 0)
        y_train_ones_idx = np.where(y_train == 1)
        y_test_zeros_idx = np.where(y_test == 0)
        y_test_ones_idx = np.where(y_test == 1)

        x_train_zeros_data = x_train[y_train_zeros_idx]
        x_train_ones_data = x_train[y_train_ones_idx]
        x_test_zeros_data = x_train[y_test_zeros_idx]
        x_test_ones_data = x_train[y_test_ones_idx]

        x_train = np.concatenate([x_train_zeros_data, x_train_ones_data], axis=0)
        x_test = np.concatenate([x_test_zeros_data, x_test_ones_data], axis=0)

        y_train = np.concatenate(
            [
                np.zeros(x_train_zeros_data.shape[0]),
                np.ones(x_train_ones_data.shape[0]),
            ],
        )
        y_test = np.concatenate(
            [
                np.zeros(x_test_zeros_data.shape[0]),
                np.ones(x_test_ones_data.shape[0]),
            ],
        )

        return x_train, y_train, x_test, y_test

    def get_mnist_digits(self) -> Tuple[np.array, np.array, np.array, np.array]:
        """
        Get `mnist` digits data with answers.

        :return: digits data with answers.
        """
        return self.x_train, self.y_train, self.x_test, self.y_test
