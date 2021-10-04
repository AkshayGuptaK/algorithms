from algorithms.src.counting_inversions import counting_inversions


def sampleTest():
    arr = [1, 4, 3, 2]
    assert counting_inversions(arr) is 3
