modifier = input("How many times do i have to tell you? ")
modifier = int(modifier)
reminder = "Clean up your room!!!".upper()

if modifier:
    for x in range(modifier):
        print(f"{reminder} #{x+1}")
