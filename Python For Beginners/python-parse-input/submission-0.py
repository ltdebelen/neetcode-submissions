from typing import List

def read_integers() -> List[int]:
    
    numbers_input = input()
    numbers = []

    for item in numbers_input.split(","):
        numbers.append(int(item))

    return numbers


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
