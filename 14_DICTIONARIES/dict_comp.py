numbers = dict(first=1, second=2, third=3)

# squared_numbers = {key: value ** 2 for key, value in numbers.items()}
# print(squared_numbers)

# print({num: num ** 2 for num in [1, 2, 3, 4, 5]})

# str1 = "ABC"
# str2 = "123"

# combo = {str1[i]: str2[i] for i in range(0,len(str1))}
# print(combo)

# instructor = dict(name="colt", city="san francisco", color="purple")

# print({key.upper(): value.upper() for key, value in instructor.items()})

num_list = [1, 2, 3, 4]

print({num: ("even" if num % 2 == 0 else "odd") for num in num_list})
