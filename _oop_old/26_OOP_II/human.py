class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


jane = Human("Jane", "Goodall", 34)
# jane.age = -100
# print(jane.get_age())
# jane.set_age(45)
# print(jane.get_age())

print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim McManus"
print(jane.full_name)
print(jane.__dict__)
