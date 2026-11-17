def add_two_numbers() -> int:
    x = input()
    string = x.split(",")
    nums = []
    for number in string:
        nums.append(int(number))
    total = sum(nums)
    return total 

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
