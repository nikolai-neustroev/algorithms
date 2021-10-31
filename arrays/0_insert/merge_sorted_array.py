from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    nums1[:n] = nums2[:n]
    return nums1


if __name__ == '__main__':
    test = [
        [1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3,
    ]
    expected = [1, 2, 2, 3, 5, 6]
    assert merge(test[0], test[1], test[2], test[3]) == expected
