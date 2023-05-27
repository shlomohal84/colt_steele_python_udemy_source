set_1 = {x ** 2 for x in range(10)}
# print(set_1)

set_2 = {char.upper() for char in 'hello'}
# print(set_2)

string_1 = "hello ha ha ha"

# print(len({char for char in string_1 if char in "aeiou"}) == 5)

string_2 = "sequoia"

print(len({char for char in string_2 if char in "aeiou"}) == 5)
