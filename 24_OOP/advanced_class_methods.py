# Advanced class methods


class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(",")
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

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        remainder = self.age % 100
        suffix_list = ["st", "nd", "rd", "th"]
        if remainder not in range(11, 13 + 1):
            if remainder % 10 == 1:
                return f"Happy {self.age}{suffix_list[0]} Birthday {self.first}!!!"
            elif remainder % 10 == 2:
                return f"Happy {self.age}{suffix_list[1]} Birthday {self.first}!!!"
            elif remainder % 10 == 3:
                return f"Happy {self.age}{suffix_list[2]} Birthday {self.first}!!!"
        return f"Happy {self.age}{suffix_list[3]} Birthday {self.first}!!!"


user1 = User("Shlomo", "Halperin", 39)
user2 = User("Pablo", "Aimar", 21)
# print(user1.logout())
# print(user1.full_name())
# print(user1.initials())
# print(user1.likes("Pizza"))
# print(user1.birthday())
print(User.display_active_users())

user1 = User("Shlomo", "Halperin", 39)
user2 = User("Pablo", "Aimar", 21)

print(User.display_active_users())

john_doe = User.from_string("John,Doe,21")
print(john_doe.full_name())
print(john_doe.birthday())
