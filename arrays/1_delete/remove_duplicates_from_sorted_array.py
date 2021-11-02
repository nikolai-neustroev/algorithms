from typing import List


def remove_duplicates(nums: List[int]):
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[:i+1]


if __name__ == '__main__':
    test = [0, 0, 1, 1, 2, 3, 3, 3, 4, 4]
    expected = [0, 1, 2, 3, 4]
    actual = remove_duplicates(test)
    assert actual == expected
