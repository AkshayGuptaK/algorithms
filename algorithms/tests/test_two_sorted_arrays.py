import pytest
from algorithms.src.hw2.two_sorted_arrays import two_sorted_arrays, main


def test_empty_inputs():
    with pytest.raises(Exception):
        arr1 = []
        arr2 = []
        main(arr1, arr2, 0)


def test_too_large_k():
    with pytest.raises(Exception):
        arr1 = [1, 3, 5]
        arr2 = [7, 8, 9]
        main(arr1, arr2, 6)


def test_unequal_size_inputs():
    with pytest.raises(Exception):
        arr1 = [1, 2, 5]
        arr2 = [8, 11]
        main(arr1, arr2, 0)


def test_single_inputs():
    arr1 = [2]
    arr2 = [1]
    assert main(arr1, arr2, 1) is 2


def test_two_sorted_arrays():
    arr1 = [1, 6, 15, 22]
    arr2 = [0, 3, 18, 56]
    assert main(arr1, arr2, 4) is 15


def test_two_larger_sorted_arrays():
    arr1 = [6, 18, 33, 49, 79]
    arr2 = [4, 23, 29, 52, 81]
    assert main(arr1, arr2, 7) is 52


def test_different_range_arrays_small_k():
    arr1 = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176]
    arr2 = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041]
    assert main(arr1, arr2, 1) is 5


def test_different_range_arrays_large_k():
    arr1 = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176]
    arr2 = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041]
    assert main(arr1, arr2, 13) is 1729
