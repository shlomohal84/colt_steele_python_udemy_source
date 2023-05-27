from random import choice

# We can nest functions inside one another
def greet(person):
    def get_mood():
        msg = choice(("hello there ", "go away ", "i love you "))
        return msg

    result = get_mood() + person
    return result


print(greet("toby"))
