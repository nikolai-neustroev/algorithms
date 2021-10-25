from typing import List


def duplicate_zeros(arr: List[int]):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0
    return arr


if __name__ == '__main__':
    test = [1, 0, 2, 3, 0, 4, 5, 0]
    expected = [1, 0, 0, 2, 3, 0, 0, 4]
    assert duplicate_zeros(test) == expected
