# Dictionaries / Maps or Hashmaps - JavaScript Object

from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    my_map = {}
    my_map[name] = age

    return my_map
    pass


def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_map = {}

    for i in range(len(words)):
        my_map[words[i]] = i

    return my_map
    pass



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
