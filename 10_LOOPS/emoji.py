# "\U0001f600"
emoji = "\U0001f600"

# for loop
print('\n********')
print('for loop')
for num in range(1, 10+1):
    print(emoji * num)

# while loop nested in for loop without string multiplication
print('\n********')
print('while loop nested in for loop')

for num in range(1, 10+1):
    smileys = emoji
    count = 1
    while count < num:
        smileys += emoji
        count += 1
    print(smileys)


# while loop
print('\n********')
print('while loop')
times = 1
while times < 10+1:
    print(emoji * times)
    times += 1


# centering emojies with for loop
times = 20 + 1
print('\n********')
print('centering emojies with for loop')
for num in range(1, times):
    print(' ' * (times - num) + emoji * num)
