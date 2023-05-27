# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age


# user1 = User("Joe", "Gomez", 25)
# user2 = User("Virgil", "van Dijk", 31)

# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)

# Your First Class - Social Media Comments It's time to define your own class!
# Suppose we're creating a social network application where users can comment on
# posts and photos.

# Create a class called Comment .  Each comment should have the following
# attributes:
# username  - the username of the person who created the comment (like
# "bluethecat") text  - the actual comment itself (like "omg so cute!" or
# "hahah") likes  - the number of likes the comment has.  Likes should default
# to 0. The following code should work:

# c = Comment("davey123", "lol you're so silly", 3) c. username #"davey123" c.
# text           #"lol you're so silly" c.likes           #3 another_comment =
# Comment("rosa77", "soooo cute!!!") another_comment.username #"rosa77"
# another_comment.text
# #"soooo cute!!!" another_comment.likes
# #0 Hints:
# __init__ is like any other function.  To add a default value for a parameter,
# just use the equals sign =.  Remember that your default parameters need to
# come at the end!


class Comment:
    def __init__(self, username, text="", likes=0):
        self.username = username
        self.text = text
        self.likes = likes


comment1 = Comment("BiggusDickus", "TROLOLOLOLOL", 69)

# print(comment1.username, comment1.text, comment1.likes)


class User:
    active_users = 0

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


print(User.active_users)
user1 = User("Joe", "Gomez", 25)
user2 = User("Virgil", "van Dijk", 31)
user3 = User("Erling Braut", "Haaland", 22)

print(User.active_users)

print(user2.logout())

print(User.active_users)

# print(user1.full_name())
# print(user2.full_name())
# print(user3.full_name())

# print(user1.initials())
# print(user2.initials())
# print(user3.initials())

# print(user1.likes("breaking opponent's legs"))
# print(user2.likes("scoring a header"))
# print(user3.likes("grinding Liverpool's defence"))

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())


# Define a new class called BankAccount.

# Each BankAccount should have an owner , specified when a new BankAccount is
# created like BankAccount("Charlie") Each BankAccount should have a balance
# attribute  that always starts out as 0.0 Each instance should have a deposit
# method that accepts a number and adds it to the balance. It should return the
# new balance. Each instance should have a withdraw method that accepts a number
# and subtracts it from the balance. It should return the new balance.
# acct = BankAccount("Darcy") acct.owner #Darcy acct.balance #0.0 acct.deposit(10)
# #10.0 acct.withdraw(3)  #7.0 acct.balance .  #7.0


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


# client1 = BankAccount("Shlomo", 5)
# print(client1.deposit(10))
