from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    # create array, prefill with 0, length should be based on size given
    new_list = [0] * size

    # insert value at given index
    new_list[index] = value
    return new_list

# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
