from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    for n in nums:
        if nums[abs(n)-1] > 0: 
            nums[abs(n)-1] *= -1
    return [i+1 for i in range(len(nums)) if nums[i]>0]


if __name__ == '__main__':
    # Given an array nums of n integers where nums[i] is in the range [1, n], 
    # return an array of all the integers in the range [1, n] that do not 
    # appear in nums.
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers([1, 1]) == [2]
