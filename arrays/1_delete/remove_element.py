from typing import List


def remove(nums: List[int], val: int):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return nums[:i]


if __name__ == '__main__':
    test = [
        [3, 2, 2, 3],
        3
    ]
    expected = [2, 2]
    actual = remove(test[0], test[1])
    assert actual == expected
