def num_squares(n: int) -> int:
    # BFS
    squares = [i**2 for i in range(1, int(n**0.5)+1)]
    d, q, nq = 1, {n}, set()
    while q:
        for node in q:
            for square in squares:
                if node == square: 
                    return d
                if node < square: 
                    break
                nq.add(node-square)
        d, q, nq = d+1, nq, set()


if __name__ == "__main__":
    assert num_squares(12) == 3
    assert num_squares(13) == 2
