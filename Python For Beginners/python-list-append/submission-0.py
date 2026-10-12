from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:

    new_list = []

    for num in my_list:
        new_list.append(num)
    
    for num in elements:
        new_list.append(num)

    return new_list

    pass



# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
