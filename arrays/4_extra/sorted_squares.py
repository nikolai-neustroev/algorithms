from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    return_array = [0] * len(nums)

    write_pointer = len(nums) - 1
    left_read_pointer = 0
    right_read_pointer = len(nums) - 1

    left_square = nums[left_read_pointer] ** 2
    right_square = nums[right_read_pointer] ** 2
    
    while write_pointer >= 0:
        if left_square > right_square:
            return_array[write_pointer] = left_square
            left_read_pointer += 1
            left_square = nums[left_read_pointer] ** 2
        else:
            return_array[write_pointer] = right_square
            right_read_pointer -= 1
            right_square = nums[right_read_pointer] ** 2
        write_pointer -= 1
    return return_array


if __name__ == '__main__':
    # Given an integer array nums sorted in non-decreasing order, 
    # return an array of the squares of each number sorted 
    # in non-decreasing order.
    assert sorted_squares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sorted_squares([-7,-3,2,3,11]) == [4,9,9,49,121]
