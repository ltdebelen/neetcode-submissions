from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    index = -1
    for i, num in enumerate(nums):
        if num == 7:
            index = i
            return index

    return index
    pass


def get_dist_between_sevens(nums: List[int]) -> int:
    first_7_index = -1
    second_7_index = -1

    for i, num in enumerate(nums):
        if num == 7:
            # if first_7_index is empty or -1, it means it hasn't been set yet. So this is the first occurence
            if first_7_index == -1:
                first_7_index = i
            elif second_7_index == -1:
                second_7_index = i

    return second_7_index - first_7_index

    pass


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
