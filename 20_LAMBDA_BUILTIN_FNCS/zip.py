nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

# print(list(zip(nums1, nums2)))

midterms = [80, 91, 78]
finals = [98, 89, 54]
students = ['dan', 'ang', 'kate']


# Desired output: final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

final_grades = {t[0]: max(t[1], t[2])  # dict comprehension
                for t in zip(students, midterms, finals)}
# print(final_grades)  # final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

final_grades_map = zip(  # map and lambda
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

# print(dict(final_grades_map))

avg_grades = zip(  # map and lambda avg arithmetic
    students,
    map(
        lambda pair: ((pair[0]+pair[1]) / len(pair)),
        zip(midterms, finals)
    )
)

# print(dict(avg_grades))


avg_grades = zip(  # map and lambda avg with sum
    students,
    map(
        lambda pair: sum([pair[0], pair[1]]) / len(pair),
        zip(midterms, finals)
    ),
)

# print(dict(avg_grades))


# Interleaving Strings(kind of tough!)

# This challenge is a bit more involved than the others in this section.  Do not
# worry if you can't get it!

# Write a function interleave  that accepts two strings.  It should return a new
# string containing the 2 strings interwoven or zipped together. For example:

# interleave('hi', 'ha')    # 'hhia'

# interleave('aaa', 'zzz')  # 'azazaz'

# interleave('lzr', 'iad')  # 'lizard'

# This might seem like an easy task using zip, but in fact there are a couple
# intermediate steps to go from zip  back to a single string.  If you need help,
# I've written up a basic walkthrough of the steps:

# suppose we call interleave('hi', 'no')

# zip  the two strings together, giving you a list of tuples(once you convert
# from the default zip_object) - [('h', 'n'), ('i', 'o')]

# For each of the tuples in the list, join them together using "".join
# resulting in ['hn', 'io'] - Easiest if you use a list comp.  You need to join
# EACH tuple.

# Finally, join the items in the list together using "".join  again resulting in
# 'hnio'

# Don't stress if you don't get this one!

def interleave(*args):
    return "".join((["".join(elm) for elm in list(zip(*args))]))


# print(interleave('hi', 'no'))    # 'hnio'

# print(interleave('hi', 'ha'))    # 'hhia'

# print(interleave('aaa', 'zzz'))  # 'azazaz'

# print(interleave('lzr', 'iad'))  # 'lizard'


# triple_and_filter

# Write a function called triple_and_filter. This function should accept a list
# of numbers, filter out every number that is not divisible by 4, and return a
# new list where every remaining number is tripled.

def triple_and_filter(lst):
    return list(
        [
            item * 3 for item in
            filter(
                lambda elm: elm % 4 == 0, lst
            )
        ]
    )


# print(triple_and_filter([1, 2, 3, 4]))  # [12]
# print(triple_and_filter([6, 8, 10, 12]))  # [24,36]


def triple_and_filter(lst):  # map
    return list(filter(lambda num: num % 4 == 0, map(lambda elm: elm * 3, lst)))


# print(triple_and_filter([1, 2, 3, 4]))  # [12]
# print(triple_and_filter([6, 8, 10, 12]))  # [24,36]


# extract_full_name

# Write a function called extract_full_name. This function should accept a list
# of dictionaries and return a new list of strings with the first and last name
# keys in each dictionary concatenated.

names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]


def extract_full_name(lst):
    return list(map(lambda elm: "".join("{} {}".format(elm["first"], elm["last"])), lst))


print(extract_full_name(names))
