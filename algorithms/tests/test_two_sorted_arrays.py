import pytest
from algorithms.src.hw2.two_sorted_arrays import two_sorted_arrays


def test_empty_inputs():
    with pytest.raises(Exception):
        arr1 = []
        arr2 = []
        two_sorted_arrays(arr1, arr2, 1)


def test_zero_k():
    with pytest.raises(Exception):
        arr1 = [1, 3, 5]
        arr2 = [7, 8, 9]
        two_sorted_arrays(arr1, arr2, 0)


def test_too_large_k():
    with pytest.raises(Exception):
        arr1 = [1, 3, 5]
        arr2 = [7, 8, 9]
        two_sorted_arrays(arr1, arr2, 7)


def test_one_empty_input():
    arr1 = [1, 2, 5]
    arr2 = []
    assert two_sorted_arrays(arr1, arr2, 1) is 1


def test_single_inputs():
    arr1 = [2]
    arr2 = [1]
    assert two_sorted_arrays(arr1, arr2, 2) is 2


def test_two_sorted_arrays():
    arr1 = [1, 6, 15, 22]
    arr2 = [0, 3, 18, 56]
    assert two_sorted_arrays(arr1, arr2, 5) is 15
