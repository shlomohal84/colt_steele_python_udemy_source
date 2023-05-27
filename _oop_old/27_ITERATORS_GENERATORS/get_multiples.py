# get_multiples
# Write a function called get_multiples, which accepts a number and a count, and
# returns a generator that yields the first count multiples of the number.
# The default number should be 1, and the default count should be 10.
"""
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


# def get_multiples(num=1, count=10):
#     i = 1
#     while i <= count:
#         yield num * i
#         i += 1
def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


res = get_multiples(2, 3)
print(next(res))
print(next(res))
print(next(res))
print(next(res))

# default_multiples = get_multiples()
# print(list(default_multiples))
