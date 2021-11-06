from typing import List


def n_and_m_exist(arr: List[int]) -> bool:
    pass


if __name__ == '__main__':
    # Given an array arr of integers, check if there exists two integers N
    # and M such that N is the double of M (i.e. N = 2 * M).
    test = [10, 2, 5, 3]
    expected = True
    actual = n_and_m_exist(test)
    assert actual == expected
