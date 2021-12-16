from collections import deque
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                flip_connected(grid, i, j)
                count += 1
    return count


def flip_connected(grid, i, j):
    queue = deque([(i, j)])
    while queue:
        I, J = queue.popleft()
        for i, j in [I+1, J], [I, J+1], [I-1, J], [I, J-1]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                queue.append((i, j))


if __name__ == "__main__":
    # Given an m x n 2D binary grid grid which represents a map of '1's (land)
    # and '0's (water), return the number of islands.
    # An island is surrounded by water and is formed by connecting adjacent 
    # lands horizontally or vertically. You may assume all four edges of 
    # the grid are all surrounded by water.
    grid = [
      ["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]
    ]
    assert num_islands(grid) == 1

    grid = [
      ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]
    ]
    assert num_islands(grid) == 3
