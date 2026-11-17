from typing import List

def read_integers() -> List[int]:
    numbers = input()
    n_list = numbers.split(",")
    int_list = []
    for string in n_list:
        int_list.append(int(string))
    return int_list 
 

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
