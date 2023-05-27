# loop through 1-20

# - for 4 and 13 print "<num> is unlucky"
# - for even numbers, print "<num> is even"
# - for odd numbers, print "<num> is odd"

# for num in range(1, 20+1):
#     if num == 4 or num == 13:
#         print(f'{num} is Unlucky!'.upper())
#     elif num % 2 == 0:
#         print(f"{num} is even!".upper())
#     else:
#         print(f"{num} is odd!".upper())

for num in range(1, 20+1):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}".upper())
