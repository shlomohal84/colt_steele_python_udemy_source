arr = [4, "Hi", "5", "Hi", 1, 25, 'f', 25]
newArr = []
# # print(arr[1:])
# # print(arr[4:])


# # newArr = arr[:]
# # print(newArr == arr)
# # print(newArr is arr)

# # newArr = arr[:5:2]

# # newArr = arr[:-1]
# newArr = arr[1:-1]

# print(newArr)


# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# # newArr = colors[2:4]
# # # print(newArr)

# # newArr = colors[0::2]
# # # print(newArr)

# # newArr = colors[::2]
# # print(newArr)

# first_list = [1, 2, 3, 4, 5, 6]

# # print(first_list[1::-1])
# # print(first_list[:1:-1])
# # print(first_list[2::-1])

# print(colors[0][::-1])


# names = ["Sanchez", "Rick"]

# names[0], names[1] = names[1], names[0]

# print(names)

friends = ['ashley', 'matt', 'michael']

print([friend[0].upper() + friend[1:] for friend in friends])
