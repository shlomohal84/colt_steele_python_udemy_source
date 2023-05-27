s = set({1, 4, 5, 4, 5})
# print(list(s))

nums = [1, 4, 5, 4, 5]

# print(len(set(nums)))

s.add(25)
# print(s)

s.remove(4)
# print(s)


# print(s.discard(500))

setCopy = s.copy()
print(s)
print(setCopy)

print(s is setCopy)

s.clear()
print(s)
