from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_num_in_each_list = []

    for sub_arr in nested_arr:
        max_num = sub_arr[0] # reset on each sub_arr_iteration
        for element in sub_arr: # loop over sub_arr elements
            if element > max_num:
                max_num = element
        max_num_in_each_list.append(max_num) # after looping over sub_arr elements, push max_num

    return max_num_in_each_list   

# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))