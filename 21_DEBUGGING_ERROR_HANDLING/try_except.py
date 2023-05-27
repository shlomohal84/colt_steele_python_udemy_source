# try:
#     foobar
# except:
#     print("PROBLEM")

# print("after the try")

# d["city"]


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {"name": "Ricky"}
# print(get(d, "city"))
# print(get(d, "name"))

while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That's not a number")
    else:
        print("GOOD JOB. YOU ENTERED A NUMBER")
        break
    finally:
        print("RUNS NO MATTER WHAT")
print("REST OF GAME LOGIC")
