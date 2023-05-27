age = 222

# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dollar to everyone

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You pay 10$ and are not a child or a senior")
else:
    print("You are a child or senior")

# x = 0 Falsy
# y = -1 Truthy
# (x or y) and x - 1 == y and y + 1 == x
