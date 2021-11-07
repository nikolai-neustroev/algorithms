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


if __name__ == '__main__':
    # Given an array arr of integers, check if there exists two integers N
    # and M such that N is the double of M (i.e. N = 2 * M).
    test = [10, 2, 5, 3]
    expected = True
    actual = n_and_m_exist_(test)
    assert actual == expected
