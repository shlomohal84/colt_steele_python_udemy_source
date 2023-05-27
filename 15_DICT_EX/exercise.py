# Given two lists["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode
# Island"] create a dictionary that looks like this {'CA': 'California', 'NJ':
# 'New Jersey', 'RI': 'Rhode Island'}. Save it to a variable called answer.

# I expect you to do this with a dictionary comprehension, but you can also use
# a built-in function called zip .  We cover it later in the course.
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0, len(list1))}
# print(answer)


# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Create a dictionary called answer, that makes each first item in each list a
# key and the second item a corresponding value.  That's a terrible explanation.
# I think it'll be easier if you just look at the end goal:

# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

# There are many potential solutions for this.

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# # use the person variable in your answer
# # answer = {entry[0]: entry[1] for entry in person}

# # print(answer)

# # answer = {k: v for k, v in person}

# # print(answer)
# answer = dict(person)

# print(answer)


# Create a dictionary with the key as a vowel in the alphabet and the value as
# 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u':
# 0}.

# Do this programmatically(using a dict comprehension or dict method) rather
# than hard coding the answer!

# answer = {v: 0 for v in ["a", "e", "i", "o", "u"]}
# print(answer)
# answer = dict.fromkeys("aeiou", 0)
# print(answer)

# This is a bit different. Every character has an ASCII code(basically, a number
# that represents it).  Python has a function called chr() that will return a
# string if you provide the corresponding integer ASCII code.  For example:

# chr(65)  will return 'A'

# chr(66)  will return 'B'

# All the way up to:

# chr(90)  will return 'Z'

# Your task is to create dictionary that maps ASCII keys to their corresponding
# letters.  Use a dictionary comprehension and chr() . Save the result to the
# answer variable. You only need to care about capital letters(65-90).

# The end result will look like this:

# { 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73:
#     'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81:
#     'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89:
#     'Y', 90: 'Z'
# }

# answer = {num: chr(num) for num in range(65, 90+1)}
# print(answer)
