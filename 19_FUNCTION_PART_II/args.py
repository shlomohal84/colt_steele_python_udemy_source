def sum_all_nums(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


# print(sum_all_nums(4, 6, 9, 4, 10))
# print(sum_all_nums(4, 6))

def ensure_correct_info(*args):
    print(args)
    if "Shlomo" in args and "Halperin" in args:
        return "Welcome back Shlomo!"

    return "Explain your smolness!"


# print(ensure_correct_info(False, "Am Potat", 1921.4242))
# print(ensure_correct_info(1, True, "Shlomo", "Halperin"))

# *args Exercise: The Purple Test

# Define a function contains_purple  that accepts any number of arguments.  It
# should return True if any of the arguments are "purple" (all lowercase).
# Otherwise, it should return False .  For example:

# contains_purple(25, "purple")  # True

# contains_purple("green", False, 37, "blue", "hello world")  # False

# contains_purple("purple")  # True

# contains_purple("a", 99, "blah blah blah", 1, True, False, "purple")  # True

# contains_purple(1, 2, 3)  # False

# Always remember, purple is the best color on this earth.  All hail purple.

def contains_purple(*args):
    if "purple" in args:
        return True
    return False


# print(contains_purple("purpe"))


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
    return ""


# print(fav_colors(colt="purple", ruby="red", ethel="teal"))

# **kwargs Exercise

# Note: for this exercise, make use of ** kwargs.  No default parameters
# allowed!

# Write a function called combine_words  which accepts a single string called
# word and any number of additional key word arguments.  If a prefix is
# provided, return the prefix followed by the word.  If a suffix is provided,
# return the word followed by the suffix.  If neither is provided, just return
# the word.  It might sound confusing, but the examples should make this a lot
# clearer!

# combine_words("child")  # 'child'

# combine_words("child", prefix="man")  # 'manchild'

# combine_words("child", suffix="ish")  # 'childish'

# combine_words("work", suffix="er")  # 'worker'

# combine_words("work", prefix="home")  # 'homework'

def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


# print(combine_words('Shlomo', smol="potat", show_me_what_you="got", suffix="sh"))


def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


# a - 1
# b - 2
# args - (3)
# instructor -"Colt"
# kwargs - {"last_name":"Steele","Job":"Instructor"}

# print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num

    return total


# print(sum_all_values(1, 2, 3, 9, 5))
nums = [1, 2, 3, 4, 5, 6]
# print(sum_all_values(*nums))
# print(sum_all_values(*tuple(nums)))


# Unpacking Exercise

# This time I've defined a function for you. It's called count_sevens, and you
# need to call it twice.

# First, call it with the arguments 1, 4, and 7 and save the result to a
# variable called result1. Next, call the same count_sevens function, passing in
# all the numbers contained in the nums list as individual arguments(unpack the
# list).  Save the result to a variable called result2 .

def count_sevens(*args):
    return args.count(7)


nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23,
        34, 55, 1, 90, 54, 34, 76, 8, 23, 34, 45, 56, 67, 78, 12, 23,
        34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17,
        11, 7, 11, 8, 4, 6, 2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7,
        7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 2,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]

# result1 = (count_sevens(1, 4, 7))
# result2 = (count_sevens(*nums))


def display_names(first, second):

    return f"{first} says hello to {second}"


names = {"first": "Colt", "second": "Rusty"}

# print(display_names(**names))


def add_and_multiply(a, b, c, **kwargs):
    print(kwargs)
    return (a + b * c)


data = dict(a=1, b=2, c=3, d=25, name="Tony")
# print(add_and_multiply(**data, cat="Blue"))


# Oh boy, this is a complicated set of instructions.  Bear with me. Write a
# function called calculate that accepts a list of keyword arguments

# make_float, a boolean which returns a float if True or an integer if False.

# operation which is either 'add', 'subtract', 'multiply', and 'divide'.

# first which is a number, second, which is another number, and message which is
# a string that can be added.

# The function should return the result of actually running the specified
# operation with the first and second keyword arguments. The result of the
# operation with the first and second is an integer if the make_float  keyword
# argument is False, otherwise the result of the operation is a float. If a
# message is specified, it should return the message keyword argument + the
# result of the operation.  Otherwise, it should return the string  "The result
# is " joined with the result of the operation.

# See the examples below for some more information. Remember, you can't use
# f-strings on in the Udemy Editor.

'''
calculate(make_float=False, operation='add', message='You just added',
          first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide',
          first=3.5, second=5) # "The result is 0.7"
'''


# def calculate(message="The result is", **kwargs):
#     # print(not kwargs["make_float"])
#     if kwargs["operation"] == 'add':
#         if kwargs["make_float"] == False:
#             if message:
#                 return "{} {}".format(message, int(kwargs["first"] + kwargs["second"]))
#             return "{} {}".format(kwargs["operation"], int(kwargs["first"] + kwargs["second"]))
#         if message:
#             return "{} {}".format(message, float(kwargs["first"] + kwargs["second"]))
#         return "{} {}".format(kwargs["operation"], int(kwargs["first"] + kwargs["second"]))
#     elif kwargs["operation"] == 'subtract':
#         if kwargs["make_float"] == False:
#             if message:
#                 return "{} {}".format(message, int(kwargs["first"] - kwargs["second"]))
#             return "{} {}".format(kwargs["operation"], int(kwargs["first"] - kwargs["second"]))
#         if message:
#             return "{} {}".format(message, float(kwargs["first"] - kwargs["second"]))
#         return "{} {}".format(kwargs["operation"], float(kwargs["first"] - kwargs["second"]))
#     elif kwargs["operation"] == 'multiply':
#         if kwargs["make_float"] == False:
#             if message:
#                 return "{} {}".format(message, int(kwargs["first"] * kwargs["second"]))
#             return "{} {}".format(kwargs["operation"], int(kwargs["first"] * kwargs["second"]))
#         if message:
#             return "{} {}".format(message, float(kwargs["first"] * kwargs["second"]))
#         return "{} {}".format(kwargs["operation"], float(kwargs["first"] * kwargs["second"]))

#     if kwargs["make_float"] == False:
#         if message:
#             return "{} {}".format(message, int(kwargs["first"] / kwargs["second"]))
#         return "{} {}".format(kwargs["operation"], int(kwargs["first"] / kwargs["second"]))
#     if message:
#         return "{} {}".format(message, float(kwargs["first"] / kwargs["second"]))
#     return "{} {}".format(kwargs["operation"], float(kwargs["first"] / kwargs["second"]))


# print(calculate(make_float=False, operation='add', message='You just added',
#                 first=2, second=4))  # "You just added 6"


def calculate(**kwarg):
    final = ""
    operation_lookup = {
        'add': kwarg.get("first", 0) + kwarg.get("second", 0),
        'subtract': kwarg.get("first", 0) - kwarg.get("second", 0),
        'multiply': kwarg.get("first", 0) * kwarg.get("second", 0),
        'divide': kwarg.get("first", 0) / kwarg.get("second", 0)
    }

    is_float = kwarg.get("make_float", False)
    operation_value = operation_lookup[kwarg.get("operation", "")]

    if is_float:
        final = "{} {}".format(
            kwarg.get('message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(
            kwarg.get('message', 'The result is'), int(operation_value))

    return final


print(calculate(make_float=False, operation='add', message='You just added',
                first=2, second=4))  # "You just added 6"
