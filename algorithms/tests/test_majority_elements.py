import pytest
from algorithms.src.hw2.majority_elements import main


def test_empty_input():
    with pytest.raises(Exception):
        arr = []
        main(arr)


def test_single_input():
    arr = [12]
    assert main(arr) is 12


def test_no_majority():
    arr = [1, 3, 2, 2, 1]
    assert main(arr) is False


def test_bare_majority():
    arr = [5, 5, 3, 7, 5, 5, 7, 5, 6]
    assert main(arr) is 5


def test_clear_majority():
    arr = [2, 3, 2, 2, 2, 7, 2, 2]
    assert main(arr) is 2
