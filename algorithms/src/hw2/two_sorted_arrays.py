# You are given two sorted arrays, each of size n. Give as efficient an algorithm as possible to
# find the k-th smallest element in the union of the two arrays.


def two_sorted_arrays(arr1, arr2, k):
    assert k > 0
    assert k <= len(arr1) + len(arr2)

    def two_sorted_arrays_helper(i, j, k):
        if len(arr1) - i == 0:
            return arr2[j + k - 1]
        if len(arr2) - j == 0:
            return arr1[i + k - 1]
        if k == 1:
            return min(arr1[i], arr2[j])
        if arr1[i] <= arr2[j]:
            i += 1
        else:
            j += 1

        return two_sorted_arrays_helper(i, j, k - 1)

    return two_sorted_arrays_helper(0, 0, k)
