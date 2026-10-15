from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    # 2 x 3 grid
    # [  
    #         c1, c2, c3 
    #     r1: [0, 0, 0]
    #     r2: [0, 0, 0]
    # ]
    #      set col nums and init value, then set row num   
    grid = [[value for i in range(cols)] for j in range(rows)]
    # print(grid)

    return grid


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
