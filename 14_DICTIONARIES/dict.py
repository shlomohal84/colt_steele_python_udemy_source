# cat = [
#     {
#         "name": "cat litter",
#         "quantity": 1,
#         "isCute": True
#     },
# ]

# user_info = {
#     "size": "smol",
#     "description": "potat",
#     "sound": "meow"
# }

# prop = "smol"
# print(user__info[prop])

# print(user__info)

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

# full_name = artist["first"] + " " + artist["last"]
# full_name = "{} {}".format(artist["first"], artist["last"])
# print(full_name)

# items = user__info.items()
# for item in user__info.items():
#     print(item)

# for key, value in user__info.items():
#     print(f"key is {key} and value is {value}")


# # Given the provided dictionary of donations:

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
#                  stan=150.0, lisa=50.25, harrison=10.0)

# # Use a loop to calculate the total value of the donations.
# #  Save the result to a variable called total_donations

# total_donations = 0

# for v in donations.values():
#     total_donations += v


# print(total_donations)


# print("size" in user__info)

# if "size" in user__info:
#     print("There is \"size\" key in user_info dictionary")

# print("smol" in user__info.values())

# copy = user_info.copy()
# print(copy)

# print(copy == user_info)
# print(copy is user_info)

# print({}.fromkeys("a", "b"))  # {"a": "b"}
# # {'email': 'unknown'}
# print({}.fromkeys(["email", "username", "password"], "unknown"))
# print({}.fromkeys("a", [1, 2, 3, 4, 5]))  # {'a': [1, 2, 3, 4, 5]}


# new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unknown")
# print(new_user.fromkeys(["phone"], "unknown"))
# print(new_user)

# print({}.fromkeys("phone", "unknown"))
# print({}.fromkeys(range(1, 10), "unknown"))

# print(new_user.get('name'))
# print(new_user.get('potato'))
# print(new_user['potato'])


# For this exercise, I've defined some code for you already.

# The food  variable will store a randomly chosen food string like "gummy bear"
# or "morning bun".  Some of these items are in the bakery_stock  dictionary,
# and some are not .

# Your task is to simply print out a string depending on if food is a value in bakery_stock
# If food is contained in bakery_stock print out a string that states how many items are left: "3 left"
# if food is "toffee cookie" or "1 left" if food is "morning bun", etc.
# If food is not contained in bakery_stock(like "gummy bear"), print out "We  don't make that"

# This code picks a random food item:
# from random import choice  # DON'T CHANGE!

# food = choice(["cheese pizza", "quiche", "morning bun",
#               "gummy bear", "tea cake"])  # DON'T CHANGE!
# # print(food)

# # DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant": 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# item = {}

# if bakery_stock.get(food):
#     item = bakery_stock[food]
#     print("{} left".format(item))
# else:
#     print("We don\'t make that")

# # YOUR CODE GOES BELOW:


# # DO NOT TOUCH game_properties!
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
#                    "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

# # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
# initial_game_state = {}.fromkeys(game_properties, 0)
# print(initial_game_state)

# inventory = {'croissant': 19, 'bagel': 4,
#              'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!

# # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
# stock_list = inventory.copy()

# # add the value 18 to stock_list under the key "cookie"
# stock_list.update({"cookie": 18})

# # remove 'cake' from stock_list USE A DICTIONARY METHOD
# stock_list.pop("cake")
# print(stock_list)
