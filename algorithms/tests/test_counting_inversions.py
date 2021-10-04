from algorithms.src.hw2.counting_inversions import main


def test_empty_input():
    arr = []
    assert main(arr) is 0


def test_single_input():
    arr = [2]
    assert main(arr) is 0


def test_unsorted_list():
    arr = [1, 4, 3, 2]
    assert main(arr) is 3


def test_list_with_duplicates():
    arr = [1, 5, 3, 7, 5, 5, 7, 2]
    assert main(arr) is 9
