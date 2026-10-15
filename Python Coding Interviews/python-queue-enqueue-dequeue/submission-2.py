from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    # queue = deque(arr)
    # for _ in range(k):
    #     queue.append(queue.popleft())
    # return queue

    queue = deque(arr)
    for _ in range(k): # k = steps // start with
        # print(rotate_list([1, 2, 3, 4, 5], 1))
        # [popleft arr], [list]
        # [2], [1, 3, 4, 5]
        #       0, 1 = k step
        # [2, 3], [1, 4, 5]
        #          0, 1
        # [2, 3, 4] [1, 5]
        #            0, 1
        # [2, 3, 4, 5], [1]
        # 2,3,4,5, 1 

        queue.append(queue.popleft())
    return queue

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
