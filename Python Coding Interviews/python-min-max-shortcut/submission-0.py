from typing import List


def disallow_negatives(num: int) -> int:
    result = max(0, num)
    return result
    pass


def max_difference(nums: List[int]) -> int:
    largest_diff = -1

    # important note:
    # start at (1) instead of (0)
    # because we want to subtract the right element first
    for i in range(1, len(nums)):
        # in this case:
        # nums[i] = 1, since we set this to (1)
        # nums[i - 1] = (0)
        # nums[1] - nums[0], [nums[2] - nums[1]]... and so forth
        diff = nums[i] - nums[i - 1]
        largest_diff = max(largest_diff, diff)
    return largest_diff 



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
