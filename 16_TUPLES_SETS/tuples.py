months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "November", "December")
# print(months)

# for month in months:
#     print(month)

# i = len(months) - 1

# while i >= 0:
#     print(months[i])
#     i -= 1

locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}
# print(locations[35.6895, 39.6917])

nums = (1, 2, 3, 3, 5, 1, 1, 7, 1, -1, 2)
# print(nums.count(1))
# print(nums.index(7))

# index = 0
# indices = []
# while index < len(nums):
#     if nums[index] == 1:
#         indices.append(index)
#     index += 1

# print(indices)


comboTuples = (1, 2, 3, (4, 5), 6, 7)

# print(comboTuples[3][1])
print(comboTuples[0:4:2])
