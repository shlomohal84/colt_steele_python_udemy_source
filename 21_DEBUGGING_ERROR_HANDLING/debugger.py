# first = "First"
# second = "Second"
# result = ""
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


def add_numbers(a, b, c, d):
    import pdb

    pdb.set_trace()
    return a + b + c + d


# add_numbers(1, 2, 3, 4)


# Write a function called divide, which accepts two parameters (you can call
# them num1 and num2). The function should return the result of num1 divided by
# num2. If you do not pass the correct type of arguments to the function, it
# should return the string "Please provide two integers or floats". If you pass
# as the second argument a 0, Python will raise a ZeroDivisionError, so if this
# function is invoked with a 0 as the value of num2, return the string "Please
# do not divide by zero"

# Examples

# divide(4,2)  2
# divide([],"1")  "Please provide two integers or floats"
# divide(1,0)  "Please do not divide by zero"


def divide(x, y):
    try:
        total = x / y
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
    # try:


print(divide(4, 2))
print(divide([], "1"))
print(divide(1, 0))


# except TypeError:
#     print("Please provide two integers or floats")

# print(divide([],"1"))
# print(divide(1, 0))
