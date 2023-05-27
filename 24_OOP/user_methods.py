class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0].upper()}.{self.last[0].upper()}."

user1 = User("Joe","Johnson",69)
user2 = User("Negra","Blanca",25)
print(user1.full_name())
print(user1.initials())
print(user2.full_name())
print(user2.initials())