from typing import List


def replace_element(arr: List[int]) -> List[int]:
    n = len(arr)
    maximum = -1
    for i in range(n - 1, -1, -1):
        if arr[i] > maximum:
            prev_maximum = maximum
            maximum = arr[i]
            arr[i] = prev_maximum
        else:
            arr[i] = maximum
    return arr


if __name__ == '__main__':
    # Given an array arr, replace every element in that array with
    # the greatest element among the elements to its right,
    # and replace the last element with -1.
    test = [17, 18, 5, 4, 6, 1]
    expected = [18, 6, 6, 6, 1, -1]
    actual = replace_element(test)
    assert actual == expected
