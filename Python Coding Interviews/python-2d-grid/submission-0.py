from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    # [
    #         c0  c1 c2
    #     r0: [1, 2, 3]
    #     r1: [4, 5, 6]
    #     r2: [7, 8, 9]
    # ]
    # r0, c0 = 1 = True
    # r2, c2 = 9 = True
    # r1, c1 = 5 = True
    # r4, c3 = no r4 and c3 = False
    # r3, c4 = no r3 and c4 = False
    # r3, c-1 = no r3 and c-1 = False
    # r-1, c3 = no r-1 and c3 = False

    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
