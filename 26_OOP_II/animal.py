class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    pass


blue = Cat()
blue.make_sound("MEOW")
# print(blue.cool)
# print(Animal.cool)
# print(Cat.cool)

print(isinstance(blue, object))
# print(isinstance([1, 2, 3], list))
# print(isinstance({"a": [1, 2, 3]}, dict))
