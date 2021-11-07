from typing import List


def n_and_m_exist_(arr: List[int]) -> bool:
    """Brute Force algorithm"""
    checker = []
    for i, val in enumerate(arr):
        for j, val_ in enumerate(arr):
            if (i != j) & (j < len(arr)) & (val == 2 * val_):
                checker.append(True)
            else:
                checker.append(False)
    return any(checker)


def n_and_m_exist(arr: List[int]) -> bool:
    """O(N)"""
    hashmap = {}
    for el in arr:
        if hashmap.get(el / 2, False) or hashmap.get(el * 2, False):
            return True
        hashmap[el] = hashmap.get(el, 0) + 1
    return False


if __name__ == '__main__':
    # Given an array arr of integers, check if there exists two integers N
    # and M such that N is the double of M (i.e. N = 2 * M).
    test = [10, 2, 5, 3]
    expected = True
    actual = n_and_m_exist(test)
    assert actual == expected
