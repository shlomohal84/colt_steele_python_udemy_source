from random import randint

# Write a function called product that accepts two parameters and returns the
# product of the two parameters (multiply them together)

'''
product(2,2) # 4
product(2,-2) # -4
'''

# define product below:


def product(a, b):
    return a * b


# print(product(2, 3))


# Write a function called return_day. this function takes in one parameter (a
# number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3
# is Tuesday etc.). If the number is less than 1 or greater than 7, the function
# should return None

# Hint: store the days of the week in a list (or dict using numbers as keys).

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

lst = ["Sunday", "Monday", "Tuesday",
       "Wednesday", "Thursday", "Friday", "Saturday"]


def return_day(lst, num):
    if num > 0 and num <= len(lst):
        return lst[num-1]
    return None


# print(return_day(lst, randint(1, 8)))


# Write a function called last_element. This function takes in one parameter(a
# list) and returns the last value in the list. It should return None if the
# list is empty.

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(lst):
    if lst:
        return lst[len(lst)-1]
    return None


# print(last_element([1, 2, 3, 4, 5, 'FU']))
# print(last_element([]))


# Write a function called number_compare. This function takes in two
# parameters(both numbers). If the first is greater than the second, this
# function returns "First is greater" If the second number is greater than the
# first, the function returns "Second is greater" Otherwise the function returns
# "Numbers are equal"

def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"


# print(number_compare(5, 5))

# single_letter_count
#  Write a function called single_letter_count. This function
# takes in two parameters(two strings). The first parameter should be a word and
# the second should be a letter. The function returns the number of times that
# letter appears in the word. The function should be case insensitive(does not
# matter if the input is lowercase or uppercase). If the letter is not found in
# the word, the function should return 0.

# Hint: take advantage of count() method

# def single_letter_count(str, letter):
#     counter = 0
#     idx = 0
#     while idx < len(str):
#         if str[idx].lower() == letter.lower():
#             counter += 1
#         idx += 1
#     return counter

def single_letter_count(str, letter):
    return str.lower().count(letter.lower())


# print(single_letter_count('heLlLLLlllo', 'l'))

# multiple_letter_count Write a function called multiple_letter_count. This
# function takes in one parameter(a string) and returns a dictionary with the
# keys being the letters and the values being the count of the letter.  Hint:
# use a dictionary comprehension and count().

# Here's how it should work:

#     # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
# multiple_letter_count("awesome")

def multiple_letter_count(str):
    return {char: str.count(char) for char in str}


# print(multiple_letter_count("Hello"))

# list_manipulation Write a function called list_manipulation. This function
# should take in four parameters(a list, command, location and value).

# If the command is "remove" and the location is "end", the function should
# remove the last value in the list and return the value removed.

# If the command is "remove" and the location is "beginning", the function
# should remove the first value in the list and return the value removed.
#
#  If the command is "add"  and the location is "beginning", the function should
# add the value(fourth parameter) to the beginning of the list and return the
# list
#
#  If the command is "add" and the location is "end", the function should add
# the value(fourth parameter) to the end of the list and return the list

def list_manipulation(lst, cmd, loc, val):
    if cmd.lower() == 'remove':
        if loc.lower() == 'end':  # remove last index
            return lst.pop()
        elif loc.lower() == 'beginning':  # remove first index
            return lst.pop(0)
    elif cmd.lower() == 'add':
        if loc.lower() == 'end':
            lst.append(val)
            return lst
        elif loc.lower() == 'beginning':
            lst.insert(0, val)
            return lst


# print(list_manipulation([1, 2, 3, 4], "remove", "end", 5))
# print(list_manipulation([1, 2, 3, 4], "remove", "beginning", 5))
# print(list_manipulation([1, 2, 3, 4], "add", "end", 5))
# print(list_manipulation([1, 2, 3, 4], "add", "beginning", 5))

# Write a function called is_palindrome. A Palindrome is a word, phrase, number,
# or other sequence of characters which reads the same backward or forward. This
# function should take in one parameter and returns True or False depending on
# whether it is a palindrome. As a bonus, allow your function to ignore
# whitespace and capitalization so that is_palindrome('a man a plan a canal
# Panama') returns True.

# def is_palindrome(str):
#     def trim_spaces(str):
#         trimmed_str = ""
#         for char in str:
#             if char != ' ':
#                 trimmed_str += char
#         return trimmed_str

#     trimmed_str = trim_spaces(str)
#     i = 0
#     j = len(trimmed_str) - 1
#     while i < j:
#         print(i, j)
#         if trimmed_str[i].lower() == trimmed_str[j].lower():
#             i += 1
#             j -= 1
#         else:
#             return False

#     return True

def is_palindrome(str):
    stripped = str.lower().replace(" ", "")
    return stripped == stripped[::-1]


# print(is_palindrome('amanaplan   acana    lpanama'))


# frequency

#  Write a function called frequency. This function accepts a list and
# a search_term(this will always be a primitive value) and returns the number of
# times the search_term appears in the list.

def frequency(lst=[], val=""):
    return lst.count(val)


# print(frequency(["Booty", "Boobs", "Ass", "Feet",
#       "Booty", "Boobs", "Boobs", "Dick", "Potato"], "Boobs"))

# multiply_even_numbers

# Write a function called multiply_even_numbers. This function accepts a list of
# numbers and returns the product of all even numbers in the list.

def multiply_even_numbers(lst):
    product = 1
    for num in lst:
        num = int(num)
        if num % 2 == 0:
            print(product, num)
            product *= num
    return product


# print(multiply_even_numbers([1, 2, 3, 4]))

# Write a function called capitalize. This function accepts a string and returns
# the same string with the first letter capitalized.  You may want to use slices
# to help you out.

def capitalize(str):
    return str[0:1].upper() + str[1:]


# print(capitalize("potato"))


# compact

# Write a function called compact. This function accepts a list and returns a
# list of values that are truthy values, without any of the falsey values.

# compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]

def compact(lst):
    return [val for val in lst if val]


# print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))


# intersection

# Write a function called intersection. This function should accept two lists
# and return a list with the values that are in both input lists.

# intersection([1,2,3], [2,3,4])    #[2,3]
# intersection(['a','b','z'],  ['x','y','z']) .  # ['z']

def intersection(lst1, lst2):
    return [val for val in lst1 if val in lst2]


# print(intersection(['a', 'b', 'z'],  ['x', 'y', 'z']))


# partition

# Write a function called partition. This function accepts a list and a callback
# function(which you can assume returns True or False).

# The function should iterate over each element in the list and invoke the
# callback function at each iteration.

# If the result of the callback function is True, the element should go into the
# first list(i.e. the "truthy" list). If the result of the callback function is
# False, the element should go into the second list(i.e. the "falsy" list). When
# it's finished, partition should return both lists inside of one larger list,
# like so:

# [truthy_list, falsy_list]
def isEven(num):
    return num % 2 == 0


# def partition(lst, cb_fnc):
#     matrix = [[], []]

#     for val in lst:
#         if cb_fnc(val):
#             matrix[0].append(val)
#         else:
#             matrix[1].append(val)
#     return matrix


# def partition(lst, cb_fnc):
#     return [[val for val in lst if cb_fnc(val)], [val for val in lst if not cb_fnc(val)]]


def partition(lst, cb_fnc):
    return [[lst.pop(lst.index(i)) for i in lst if cb_fnc(i)], lst]


# print(partition([1, 2, 5, 6, 7, 11], isEven))
