import pytest
from algorithms.src.hw2.merged_median import main


def test_no_input():
    with pytest.raises(Exception):
        main([])


def test_empty_inputs():
    with pytest.raises(Exception):
        arr1 = []
        arr2 = []
        arr3 = []
        main([arr1, arr2, arr3])


def test_unequal_size_inputs():
    with pytest.raises(Exception):
        arr1 = [1, 2, 5]
        arr2 = [8, 11]
        arr3 = [15, 47]
        main([arr1, arr2, arr3])


def test_single_arr_input():
    assert main([[22]]) is 22


def test_single_size_inputs():
    assert main([[5], [3], [4], [2], [1]]) is 3


def test_two_sorted_arrays():
    arr1 = [1, 6, 15, 22]
    arr2 = [0, 3, 18, 56]
    assert main([arr1, arr2]) is 10.5


def test_three_larger_sorted_arrays():
    arr1 = [6, 18, 33, 49, 79]
    arr2 = [4, 23, 29, 52, 81]
    arr3 = [7, 19, 26, 55, 83]
    assert main([arr1, arr2, arr3]) is 29


def test_different_range_arrays():
    arr1 = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176]
    arr2 = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041]
    arr3 = [177, 205, 212, 222, 335, 351, 370, 492, 517, 555, 560]
    assert main([arr1, arr2, arr3]) is 351
