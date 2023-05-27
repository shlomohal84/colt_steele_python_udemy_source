
nums = [2, 4, 6, 8, 10]

doubles = list(map(lambda x: x*2, nums))

# print(doubles)

people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = list(map(lambda name: name.upper(), people))

# print(peeps)


def decrement_list(lst):
    return list((map(lambda x: x-1, lst)))


# print(decrement_list([1, 2, 3]))


names = ['austin', 'penny', "anthony", 'angel', 'billy']

a_names = list(filter(lambda n: n[0] == 'a', names))

# print(a_names)


def remove_negatives(lst):
    return list(filter(lambda item: item >= 0, lst))


# print(remove_negatives([-1, 3, 4, -99]))
# print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
# print(remove_negatives([50, 60, 70]))

# Implement a function is_all_strings  that accepts a single iterable and
# returns True if it contains ONLY strings.  Otherwise, it should return false.

# is_all_strings(['a', 'b', 'c'])  #True

# is_all_strings([2,'a', 'b', 'c'])  #False

# is_all_strings(('hello', 'goodbye'))  #True

def is_all_strings(lst):
    return all(type(elm) == str for elm in lst)


# print(is_all_strings(['a', 'b', 'c']))  # True

# print(is_all_strings([2, 'a', 'b', 'c']))  # False

# print(is_all_strings(('hello', 'goodbye')))  # True

more_nums = [4, 6, 1, 30, 55, 23, -1]

# sorted(more_nums)
# sorted_nums = sorted(more_nums, reverse=True)
# print(more_nums)
# print(sorted_nums)

more_nums_tuple = (4, 6, 1, 30, 55, 23, -1)

# sorted(more_nums_tuple)
# print(more_nums_tuple)
# print(tuple(sorted(more_nums_tuple, reverse=True)))

users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
        }
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
        }
    },
    {
        "id": 4,
        "name": "Patricia Lebsack",
        "username": "Karianne",
        "email": "Julianne.OConner@kory.org",
        "address": {
            "street": "Hoeger Mall",
            "suite": "Apt. 692",
            "city": "South Elvis",
            "zipcode": "53919-4257",
            "geo": {
                "lat": "29.4572",
                "lng": "-164.2990"
            }
        },
        "phone": "493-170-9623 x156",
        "website": "kale.biz",
        "company": {
            "name": "Robel-Corkery",
            "catchPhrase": "Multi-tiered zero tolerance productivity",
            "bs": "transition cutting-edge web services"
        }
    },
    {
        "id": 5,
        "name": "Chelsey Dietrich",
        "username": "Kamren",
        "email": "Lucio_Hettinger@annie.ca",
        "address": {
            "street": "Skiles Walks",
            "suite": "Suite 351",
            "city": "Roscoeview",
            "zipcode": "33263",
            "geo": {
                "lat": "-31.8129",
                "lng": "62.5342"
            }
        },
        "phone": "(254)954-1289",
        "website": "demarco.info",
        "company": {
            "name": "Keebler LLC",
            "catchPhrase": "User-centric fault-tolerant solution",
            "bs": "revolutionize end-to-end systems"
        }
    },
    {
        "id": 6,
        "name": "Mrs. Dennis Schulist",
        "username": "Leopoldo_Corkery",
        "email": "Karley_Dach@jasper.info",
        "address": {
            "street": "Norberto Crossing",
            "suite": "Apt. 950",
            "city": "South Christy",
            "zipcode": "23505-1337",
            "geo": {
                "lat": "-71.4197",
                "lng": "71.7478"
            }
        },
        "phone": "1-477-935-8478 x6430",
        "website": "ola.org",
        "company": {
            "name": "Considine-Lockman",
            "catchPhrase": "Synchronised bottom-line interface",
            "bs": "e-enable innovative applications"
        }
    },
    {
        "id": 7,
        "name": "Kurtis Weissnat",
        "username": "Elwyn.Skiles",
        "email": "Telly.Hoeger@billy.biz",
        "address": {
            "street": "Rex Trail",
            "suite": "Suite 280",
            "city": "Howemouth",
            "zipcode": "58804-1099",
            "geo": {
                "lat": "24.8918",
                "lng": "21.8984"
            }
        },
        "phone": "210.067.6132",
        "website": "elvis.io",
        "company": {
            "name": "Johns Group",
            "catchPhrase": "Configurable multimedia task-force",
            "bs": "generate enterprise e-tailers"
        }
    },
    {
        "id": 8,
        "name": "Nicholas Runolfsdottir V",
        "username": "Maxime_Nienow",
        "email": "Sherwood@rosamond.me",
        "address": {
            "street": "Ellsworth Summit",
            "suite": "Suite 729",
            "city": "Aliyaview",
            "zipcode": "45169",
            "geo": {
                "lat": "-14.3990",
                "lng": "-120.7677"
            }
        },
        "phone": "586.493.6943 x140",
        "website": "jacynthe.com",
        "company": {
            "name": "Abernathy Group",
            "catchPhrase": "Implemented secondary concept",
            "bs": "e-enable extensible e-tailers"
        }
    },
    {
        "id": 9,
        "name": "Glenna Reichert",
        "username": "Delphine",
        "email": "Chaim_McDermott@dana.io",
        "address": {
            "street": "Dayna Park",
            "suite": "Suite 449",
            "city": "Bartholomebury",
            "zipcode": "76495-3109",
            "geo": {
                "lat": "24.6463",
                "lng": "-168.8889"
            }
        },
        "phone": "(775)976-6794 x41206",
        "website": "conrad.com",
        "company": {
            "name": "Yost and Sons",
            "catchPhrase": "Switchable contextually-based project",
            "bs": "aggregate real-time technologies"
        }
    },
    {
        "id": 10,
        "name": "Clementina DuBuque",
        "username": "Moriah.Stanton",
        "email": "Rey.Padberg@karina.biz",
        "address": {
            "street": "Kattie Turnpike",
            "suite": "Suite 198",
            "city": "Lebsackbury",
            "zipcode": "31428-2261",
            "geo": {
                "lat": "-38.2386",
                "lng": "57.2232"
            }
        },
        "phone": "024-648-3804",
        "website": "ambrose.net",
        "company": {
            "name": "Hoeger LLC",
            "catchPhrase": "Centralized empowering task-force",
            "bs": "target end-to-end models"
        }
    }
]
# print(len(users))
# user_info = ({f"{user['username']} - {user['name']}" for user in users})
# print(user_info)
# print(sorted(users, key=lambda user: user['username']))
sorted_info = sorted(users, key=lambda user: len(
    user["username"]), reverse=True)

limited_info = [elm["name"]for elm in sorted_info]


def print_users(lst):
    for elm in lst:
        print(f"#{elm['id']} {elm['username']} {len(elm['username'])}")


# print_users(sorted_info)

# print(max(more_nums_tuple))
# print(min(more_nums_tuple))

# print(limited_info)

updated_users = limited_info.copy()
updated_users.append("Shlomo Halperin")
# print(updated_users)
# print(max([limited_info, updated_users]))

# print(min(len(name) for name in updated_users))

# print(updated_users)
# print(max(updated_users, key=lambda name: len(name)))
# print(min(updated_users, key=lambda name: len(name)))


# Extremes Exercise - Using Min and Max

# Write a function called extremes  which accepts an iterable. It should return
# a tuple containing the minimum and maximum elements.  For example:

# extremes([1, 2, 3, 4, 5])  # (1, 5)

# extremes((99, 25, 30, -7))  # (-7, 99)

# extremes("alcatraz")  # ( 'a', 'z')

# REMEMBER, RETURN A TUPLE!!!

def extremes(itr):
    return (min(itr), max(itr))


# print(extremes([1, 2, 3, 4, 5]))


# Greatest Magnitude Exercise

# Write a function max_magnitude  that accepts a single list full of numbers. It
# should return the magnitude of the number with the largest magnitude(the
# number that is furthest away from zero).

# max_magnitude([300, 20, -900])  # 900

# max_magnitude([10, 11, 12])  # 12

# max_magnitude([-5, -1, -89])  # 89

# Hint: use max and abs!

# def max_magnitude(lst):
#     max = 0
#     for num in lst:
#         if abs(num) > max:
#             max = abs(num)
#     return max

def max_magnitude(lst):
    return max(abs(num) for num in lst)


# print(max_magnitude([300, 20, -900]))


# sum_even_values

# Write a function called sum_even_values. This function should accept a
# variable number of arguments and return the sum of all the arguments that are
# divisible by 2. If there are no numbers divisible by 2, the function should
# return 0.  To be clear, it accepts all the numbers as individual arguments!


def sum_even_values(*args):
    return sum([num for num in args if num % 2 == 0])


# print(sum_even_values(1, 2, 3, 4, 5, 6))  # 12
# print(sum_even_values(4, 2, 1, 10))  # 16
# print(sum_even_values(1))  # 0

# sum_floats

# Write a function called sum_floats. This function should accept a variable
# number of arguments. The function should return the sum of all the parameters
# that are floats. If there are no floats the function should return 0

# def sum_floats(*args):
#     return sum(num for num in list(filter(lambda n: type(n) == float, args)))

def sum_floats(*args):
    return sum(elm for elm in args if type(elm) == float)


# print(sum_floats(1.5, 2.4, 'awesome', [], 1))  # 3.9
# print(sum_floats(1, 2, 3, 4, 5))  # 0
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# print(list(zip(*five_by_two)))
