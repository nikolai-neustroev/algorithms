from typing import List


def third_max(nums: List[int]) -> int:
    n = list(set(nums))
    T = 3 * [float('-inf')]
    for i in n:
        if i > T[2]:
            T = [T[1], T[2], i]
        elif i > T[1]:
            T = [T[1], i, T[2]]
        elif i > T[0]:
            T = [i, T[1], T[2]]
    return T[0] if T[0] != float('-inf') else max(n)


if __name__ == '__main__':
    # Given an integer array nums, return the third distinct maximum number in 
    # this array. If the third maximum does not exist, return the maximum 
    # number.
    assert third_max([3, 2, 1]) == 1
    assert third_max([1, 2]) == 2
    assert third_max([2, 2, 3, 1]) == 1
