from typing import List


def remove_element(nums: List[int], val: int) -> int:
    i = 0
    j = 0
    for cur in range(len(nums)):
        if nums[cur] != val:
            nums[i] = nums[cur]
            i += 1
        else:
            j += 1
    return len(nums) - j


if __name__ == '__main__':
    # Given an integer array nums and an integer val, 
    # remove all occurrences of val in nums in-place. 
    # The relative order of the elements may be changed.
    # Return k after placing the final result in the first k slots of nums.
    test = ([3, 2, 2, 3], 3)
    expected = 2
    actual = remove_element(*test)
    assert actual == expected

    test = ([0, 1, 2, 2, 3, 0, 4, 2], 2)
    expected = 5
    actual = remove_element(*test)
    assert actual == expected
