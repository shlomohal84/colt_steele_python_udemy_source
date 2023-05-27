class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"


# a = Animal()
# a.make_sound("Chirp")
blue = Cat("Blue", "Cat", "String")
print(blue.play())
# blue.make_sound("Meow")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)

# print(isinstance(blue, Cat))
# print(isinstance(blue, Animal))
# print(isinstance(blue, object))
