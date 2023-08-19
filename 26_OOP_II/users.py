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


class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active moderators"


user1 = User("Shlomo", "Halperin", 39)
user2 = User("Pablo", "Aimar", 21)

jasmine1 = Moderator("Jasmine", "O'Conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'Conner", 61, "Piano")

u1 = User("Tom", "Garcia", 35)
print(User.display_active_users())
print(Moderator.display_active_mods())
