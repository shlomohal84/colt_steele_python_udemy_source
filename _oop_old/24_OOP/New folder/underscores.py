class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "Hi"
        self.__msg = "I LIKE FISH STICKS!"
        self.__lol = "HAHAHAHAHAHA"


p = Person()

print(p.name)
print(p._secret)


try:
    print(p.__msg)
    print(p.__lol)
except:
    print(f"Dunder prefix: {p._Person__msg}")
    print(f"Dunder prefix: {p._Person__lol}")
