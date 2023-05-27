# ask for age

from curses.ascii import isdigit
from sre_compile import isstring


# age = input("How old are you: ")
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         # 18-21 wristband
#         print("You can enter, but must wear a wristband")
#     elif age >= 21:
#         # 21+ drink, normal entry

#         print("You can enter and drink")
#     else:
#         # too young sorry
#         print("You can't enter little one :-(")
# else:
#     print("Please enter an number")


# More efficient:
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        # 18-21 wristband
        print("You can enter and drink")
    elif age >= 18:
        # 21+ drink, normal entry
        print("You can enter, but must wear a wristband")
    else:
        # too young sorry
        print("You can't enter little one :-(")
else:
    print("Please enter an number")
