# We can pass funcs as args to other funcs


def sum(n, func):
    total = 0
    for num in range(1, n + 1):
        total += func(num)
    return total


def square(x):
    return x * x


def cube(x):
    return x**3


# print(sum(3, square))
# print(sum(3, cube))
