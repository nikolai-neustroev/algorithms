from typing import List


def move_zeros(nums: List[int]) -> List[int]:
    zero_counter = 0
    last_non_zero_found_at = 0
    for cur in range(len(nums)):
        if nums[cur] != 0:
            nums[last_non_zero_found_at] = nums[cur]
            last_non_zero_found_at += 1
        else:
            zero_counter += 1
    for x in range(len(nums) - last_non_zero_found_at):
        nums[last_non_zero_found_at + x] = 0
    return nums


if __name__ == '__main__':
    # Given an integer array nums, move all 0's to the end of it
    # while maintaining the relative order of the non-zero elements.
    test = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    actual = move_zeros(test)
    assert actual == expected
