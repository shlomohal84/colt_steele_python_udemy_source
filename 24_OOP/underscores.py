class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "Hi!"
        self.__message = "I like hedgehogs!"
        self.__lol = "HAHAHA"
p = Person()

print(p.name)
print(p._secret)
print(p._Person__message)
print(p._Person__lol)
# print(dir(p)[0])