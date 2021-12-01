from typing import List


def check_height(heights: List[int]) -> int:
    expected = quick_sort(heights)
    counter = 0
    for x, y in zip(heights, expected):
        if x != y: counter += 1
    return counter


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    # A school is trying to take an annual photo of all the students. 
    # The students are asked to stand in a single file line in 
    # non-decreasing order by height. Let this ordering be represented 
    # by the integer array expected where expected[i] is the expected 
    # height of the ith student in line.
    # 
    # You are given an integer array heights representing the current 
    # order that the students are standing in. Each heights[i] is 
    # the height of the ith student in line (0-indexed).
    # 
    # Return the number of indices where heights[i] != expected[i].
    
    assert check_height([1, 1, 4, 2, 1, 3]) == 3
    assert check_height([5, 1, 2, 3, 4]) == 5
    assert check_height([1, 2, 3, 4, 5]) == 0
