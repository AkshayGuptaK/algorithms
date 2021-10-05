# You are given two sorted arrays, each of size n. Give as efficient an algorithm as possible to
# find the k-th smallest element in the union of the two arrays.

# Subproblem approach, O(k)
def two_sorted_arrays(arr1, arr2, k):
    assert len(arr1) == len(arr2)
    assert k < len(arr1) + len(arr2)

    def two_sorted_arrays_helper(i, j, k):
        if len(arr1) - i == 0:
            return arr2[j + k]
        if len(arr2) - j == 0:
            return arr1[i + k]
        if k == 0:
            return min(arr1[i], arr2[j])
        if arr1[i] <= arr2[j]:
            i += 1
        else:
            j += 1

        return two_sorted_arrays_helper(i, j, k - 1)

    return two_sorted_arrays_helper(0, 0, k)


# Divide and Conquer
def main(arr1, arr2, k):
    assert len(arr1) == len(arr2)
    return dc_two_sorted_arrays(arr1[: k + 1], arr2[: k + 1], k)


def dc_two_sorted_arrays(left, right, k):
    assert len(left) == len(right)
    n = len(left)
    assert k < 2 * n

    if k == 0:
        return min(left[0], right[0])
    if k == 1:
        if n == 1:
            return max(left[0], right[0])
        if left[1] <= right[0]:
            return left[1]
        if left[0] <= right[0]:
            return right[0]
        return min(left[0], right[1])

    mid = k // 2
    if left[mid] <= right[mid]:
        return dc_two_sorted_arrays(left[mid:], right[k - n : k - mid], n - mid)
    return dc_two_sorted_arrays(right[mid:], left[k - n : k - mid], n - mid)
