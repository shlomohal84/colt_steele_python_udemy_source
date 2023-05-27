nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[0][1])
# print(nested_list[1][2])
# print(nested_list[-1][1])
# print(nested_list[2][-2])


# for l in nested_list:
#     for val in l:
#         print(val)
# """
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# """

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

# for loc in coords:
#     print(loc)
#     for coord in loc:
#         print(coord)


# [[print(val) for val in l] for l in nested_list]
# """
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# """

# board = [[num for num in range(1, 4)] for val in range(1, 4)]
# print(board)

# print([["X" if num % 2 != 0 else "O" for num in range(1, 4)]
#       for val in range(1, 4)])
""" 
[['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
"""

# Using a nested list comprehension and range(), create a variable called answer
# with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] .  To break it
# down...start by using range and a list comp to generate the list[0, 1, 2].
# And then repeat that whole thing 3 times in a nested list comp.  It's all a
# bit tricky to discuss, so maybe it's just best to look at the solution if you
# get stuck.


# answer = [[num for num in range(0, 3)] for val in range(0, 3)]
# print(answer)

""" 
Using list comprehension, create a variable called answer with the following value :

[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 ]
it's a 10x10 nested list.  10 rows, each row contains the numbers 0-9.   Don't
worry about the formatting/spacing, I just added a bunch of returns to make
things clearer. Your answer will be all on one giant line. Use nested list
comprehension and range() to accomplish this.
"""

answer = [[i for i in range(0, 9+1)] for j in range(0, 9+1)]
print(answer)
