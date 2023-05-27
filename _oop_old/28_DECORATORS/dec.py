def be_polite(fn):
    def wrapper():
        print("What a pleaure to meet you!")
        fn()
        print("Have a great day!")

    return wrapper


@be_polite
def greet():
    print("My name is What?!")


@be_polite
def rage():
    print("I HATE YOU!")


# we are decorating our function with politeness!

# greet = be_polite(greet)

# polite_rage = be_polite(rage)

greet()

rage()
