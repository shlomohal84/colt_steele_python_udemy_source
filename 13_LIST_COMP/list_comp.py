# List Comprehension

numbers = [1, 2, 3, 4, 5]

# doubled_numbers = []

# for num in numbers:
#     doubled_number = num * 2
#     doubled_numbers.append(doubled_number)

# print(doubled_numbers)

# doubled_numbers = [num*2 for num in numbers]
# print(doubled_numbers)


# name = "shlomo"

# print([char.upper() for char in name])

# print([num * 10 for num in range(1, 6)])

# print([bool(val) for val in [0, [], '', {}, None, -1]])

string_list = [str(num) * 2 for num in numbers]
print(string_list)
