# We are given a sequence of n distinct numbers a1, ..., an. We say that two indices i < j form
# an inversion if ai > aj , that is if the two elements ai and aj are “out of order”. Provide a
# divide and conquer algorithm to determine the number of inversions in the sequence a1, ..., an
# in time O(n log n)
#


def counting_inversions(numbers):
    inversions = 0
    if len(numbers) <= 1:
        return inversions
    mid = len(numbers) // 2
    _, inversions = merge(
        counting_inversions_recur(numbers[:mid], inversions),
        counting_inversions_recur(numbers[mid:], inversions),
    )
    return inversions


def counting_inversions_recur(numbers, inversions):
    if len(numbers) == 1:
        return (numbers, inversions)
    mid = len(numbers) // 2
    return merge(
        counting_inversions_recur(numbers[0:mid], inversions),
        counting_inversions_recur(numbers[mid:], inversions),
    )


def merge(left_data, right_data):
    left, left_inversions = left_data
    right, right_inversions = right_data
    sorted = []
    left_index = 0
    right_index = 0
    inversions = left_inversions + right_inversions
    while left_index < len(left) and right_index < len(right):
        left_current = left[left_index]
        right_current = right[right_index]
        if left_current <= right_current:
            sorted.append(left_current)
            left_index += 1
        else:
            sorted.append(right_current)
            right_index += 1
            inversions += len(left) - left_index

    return (sorted + left[left_index:] + right[right_index:], inversions)
