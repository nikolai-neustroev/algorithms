from collections import deque
from typing import List


def open_lock(deadends: List[str], target: str) -> int:
    # The edge case
    if "0000" in deadends:
        return -1
    
    # BFS
    q = deque([("0000", 0)])  # state of the 4 wheels and turns counter
    visited = set()  # visited vertices

    while q:
        state, turns = q.popleft()

        if state == target:
            return turns

        for i in range(4):
            for digit in [
                ((int(state[i]) + 1) % 10),  # previous slot digit
                ((int(state[i]) - 1) % 10)  # next slot digit
            ]:
                nx = state[:i] + str(digit) + state[i+1:]  # next vertex
                if nx not in deadends and nx not in visited:
                    visited.add(nx)
                    q.append((nx, turns+1))

    return -1


if __name__ == "__main__":
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    assert open_lock(deadends, target) == 6

    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    assert open_lock(deadends, target) == -1

    deadends = ["8888"]
    target = "0009"
    assert open_lock(deadends, target) == 1

    deadends = ["0000"]
    target = "8888"
    assert open_lock(deadends, target) == -1
