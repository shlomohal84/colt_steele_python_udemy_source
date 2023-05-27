class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0].upper()}.{self.last[0].upper()}."

    def likes(self, things):
        return f"{self.first} likes {things}"

    def is_senior(self):
        return self.age >= 29

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday {self.first}!"


# user1 = User("Joe", "Gomez", 25)
# user2 = User("Virgil", "van Dijk", 31)
# print(User.display_active_users())

# user1 = User("Joe", "Gomez", 25)
# user2 = User("Virgil", "van Dijk", 31)
# print(User.display_active_users())

john = User.from_string("John,Stones,28")
print(john.first, john.last, john.age)
print(john.birthday())
