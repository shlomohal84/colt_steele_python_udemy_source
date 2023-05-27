# while True:
#     command = input("Type \"exit\" to exit: ")
#     if (command == "exit"):
#         break


# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break


modifier = input("How many times do i have to tell you? ")
modifier = int(modifier)
reminder = "Clean up your room!!!".upper()

if modifier:
    for x in range(modifier):
        print(f"{reminder} #{x+1}")
        if x >= 4:
            print(f"Do you even listen anymore?!\n{reminder}")
            break
