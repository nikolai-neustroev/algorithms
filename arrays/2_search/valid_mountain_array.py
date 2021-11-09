from typing import List


def is_mountain_array(arr: List[int]) -> bool:
    len_arr = len(arr)
    i = 0

    # walk up
    while i + 1 < len_arr and arr[i] < arr[i + 1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == len_arr - 1:
        return False

    # walk down
    while i + 1 < len_arr and arr[i] > arr[i + 1]:
        i += 1

    return i == len_arr - 1


if __name__ == '__main__':
    # Given an array of integers arr, return true if and only if
    # it is a valid mountain array.
    test = [0, 3, 2, 1]
    expected = True
    actual = is_mountain_array(test)
    assert actual == expected
