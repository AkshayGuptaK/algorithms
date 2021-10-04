# We are given a sequence of n distinct numbers a1, ..., an. We say that two indices i < j form
# an inversion if ai > aj , that is if the two elements ai and aj are “out of order”. Provide a
# divide and conquer algorithm to determine the number of inversions in the sequence a1, ..., an
# in time O(n log n)
#


def main(numbers):
    return counting_inversions(numbers)[1]


def counting_inversions(numbers):
    if len(numbers) <= 1:
        return (numbers, 0)
    mid = len(numbers) // 2
    return merge(
        counting_inversions(numbers[0:mid]),
        counting_inversions(numbers[mid:]),
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
