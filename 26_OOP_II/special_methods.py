from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"A human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "You can't multiply that!"


b = Human("Biggus", "Dickus", 53)
# print(b)
# print(len(b))

i = Human("Incontinentia", "Buttocks", 27)

# print(b + i)

# print(b * 2)
# print(i * 2)

# triplets = b * 3

# triplets[1].first = "Tinus"
triplets = (b + i) * 3
print(triplets)
