numbers = [1, 2, 3, 4, 5, 6]

# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# odds = [num for num in numbers if num % 2 != 0]
# print(odds)

# x = [num*2 if num % 2 == 0 else num/2 for num in numbers]
# print(x)

with_vowels = "This is so much fun!"

# without_vowels = [char for char in with_vowels if char not in "aeiou"]
# print(with_vowels)
# print(without_vowels)

# answer = [char[0] for char in ["Elie", "Tim", "Matt"]]
# # print(answer)

# answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
# # print(answer2)


# # [1,2,3,4]
# # [3,4,5,6]
# answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]
# print(answer)

# # ["Elie", "Tim", "Matt"]
# answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
# print(answer2)


""" 
For all the numbers between 1 and 100(including 100), create a variable called answer, 
which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)

USE A LIST COMPREHENSION.

"""

# answer = [num for num in range(1, 100+1) if num % 12 == 0]
# print(answer)

""" 
Given the string "amazing", create a variable called answer,
which is a list containing all the letters from "amazing" but not the vowels (a, e, i, o, and u).
The answer should look like: ['m', 'z', 'n', 'g'].

Use a list comprehension!
"""

# answer = [char for char in "amazing" if not char in "aeiou"]

# print(answer)
