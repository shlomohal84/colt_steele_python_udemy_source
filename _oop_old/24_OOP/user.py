class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.first)
print(user1.last)
print(user1.age)
