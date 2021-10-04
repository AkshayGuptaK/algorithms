# An array A[1 . . . n] is said to have a majority element if more than half of its entries are the
# same. Given an array, the task is to design an efficient algorithm to tell whether the array
# has a majority element, and if so to find that element. The elements of the array are not
# necessarily from some ordered domain like the integers, so there can be no comparisons of
# the form “is A[i] > A[j]?”. The elements are also not hashable, i.e., you are not allowed to use
# any form of sets or maps with constant time insertion and lookups. However you can answer
# questions of the form: “is A[i] = A[j]?” in constant time.


def main(elems):
    return majority_elements(elems)[1]


def majority_elements(elems):
    assert len(elems) > 0

    if len(elems) == 1:
        return (elems, elems[0])

    mid = len(elems) // 2
    return combine(
        majority_elements(elems[:mid]),
        majority_elements(elems[mid:]),
    )


def combine(left_data, right_data):
    left, left_majority = left_data
    right, right_majority = right_data
    combined = left + right
    if left_majority != False and combined.count(left_majority) > len(combined) // 2:
        return (combined, left_majority)
    if right_majority != False and combined.count(right_majority) > len(combined) // 2:
        return (combined, right_majority)
    return (combined, False)
