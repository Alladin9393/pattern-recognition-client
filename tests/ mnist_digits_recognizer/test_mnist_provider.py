"""
Provide tests for DataReader.
"""
import pytest

from statprly.mnist_digits_recognizer import MNISTProvider


def test_get_mnist_digits_data():
    """
    Case: get mnist digits data.
    Expected: mnist digits data is returned.
    """
    mnist_provider = MNISTProvider()
    x_train, y_train, x_test, y_test = mnist_provider.get_mnist_digits()

    assert len(x_train) != 0
    assert len(y_train) != 0
    assert len(x_test) != 0
    assert len(y_test) != 0


def test_get_mnist_digits_data_with_non_existing_data_path():
    """
    Case: get mnist digits data with non-existing data path.
    Expect: no such file or directory error message.
    """
    with pytest.raises(FileNotFoundError):
        MNISTProvider(mnist_data_path="")
