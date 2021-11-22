from typing import List


def sort_array(nums: List[int]) -> List[int]:
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] % 2 > nums[j] % 2:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] % 2 == 0:
            i += 1
        if nums[j] % 2 == 1:
            j -= 1
    return nums


if __name__ == '__main__':
    # Given an integer array nums, move all the even integers at
    # the beginning of the array followed by all the odd integers.
    # Return any array that satisfies this condition.
    test = [3, 1, 2, 4]
    expected_0 = [2, 4, 3, 1]
    expected_1 = [4, 2, 3, 1]
    expected_2 = [2, 4, 1, 3]
    expected_3 = [4, 2, 1, 3]
    actual = sort_array(test)
    assert actual == expected_0 or \
           actual == expected_1 or \
           actual == expected_2 or \
           actual == expected_3
