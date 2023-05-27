from random import choice, randint

# def say_hi():
#     print('HI!')


# say_hi()

def sing_happy_bday(name):
    print(f'Happy birthday to you!')
    print(f'Happy birthday to you!')
    print(f'Happy birthday dear {name.upper()}!')
    print(f'Happy birthday to you!')

# sing_happy_bday('wanker')


def print_square_of_7():
    print(7**2)


# print_square_of_7()

def square_of_7():
    return 7**2


result = square_of_7()
# print(result)


# Write a function called speak_pig that returns 'oink'.  Yup, that's it.

def speak_pig():
    return 'oink'


# print(speak_pig())

"""
This exercise is a little harder than the previous make_noise  function.

Write a function called generate_evens  that returns a list of the even numbers
between 1 and 50(not including 50). Basically, it should return a list: [2, 4,
6....all the way up to 48] Inside the function, you can construct the list using
either a loop OR list comprehension. You do not need to call the function in
this exercise, defining it is enough.
"""


def generate_evens():
    return [x for x in range(1, 50) if x % 2 == 0]


# print(generate_evens())


def square_of_num(n):
    return n * n


# print(square_of_num(5))
# print(square_of_num(10))
# print(square_of_num(256))

def power_of_num(n, p):
    return n ** p


# print(power_of_num(2, 8))
# print(power_of_num(p=3, n=2))


def print_full_name(first_name, last_name):
    return (f"Your full name is {first_name} {last_name}")


# print(print_full_name("Shlomo", "Halperin"))

def divide(num1, num2):
    return num1 / num2


# print(divide(2, 5))
# print(divide(5, 2))


""" 
Implement a function yell  which accepts a single string argument.  It should
return (not print) an uppercased version of the string with an exclamation point
aded at the end.  For example: yell("go away")   # "GO AWAY!" yell("leave me
alone")   # "LEAVE ME ALONE!" You do not need to call the function to pass the
tests. Remember, that currently you can't use f-strings in Udemy coding
challenges, so either use string concatenation or the format() method.
 """


def yell(str):
    return "{}!".format(str.upper())


# print(yell('go away'))


""" 
The pre-written count_dollar_signs  function is broken.   It's supposed to
return the number of $ characters in a given string.  For example:
count_dollar_signs("$uper $ize")  should return 2 .  But for some reason, the
function always returns either 0 or 1. What's going on?

Without adding any new lines (just move existing code around), make it work as
intended.
"""

# Without adding any new lines of code, make count_dollar_signs work as intended


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count


# print(count_dollar_signs("$hlomo The $ex Machine"))

""" 
Write a function called speak  that accepts a single parameter, animal.  

If animal is "pig", it should return "oink". 
If animal is "duck", it should return "quack".  
If animal is "cat", it should return "meow"
If animal is "dog", it should return "woof"
If animal is anything else, it should return "?"
If no animal is specified, it should default to "dog"


speak()  # "woof"
speak("pig")  # "oink"
speak("duck")  # "quack"
speak("cat")  # "meow"
speak("dog")  # "woof"
speak("banana")  # "?"
"""


def speak(str="dog"):
    if str == "pig":
        return "oink"
    elif str == "duck":
        return "quack"
    elif str == "cat":
        return "meow"
    elif str == "dog":
        return "woof"
    else:
        return "?"


# print(speak("potat"))

x = 0


def set_x():
    global x
    x += 1


# set_x()
# print(x)


def outer():
    """abcd"""

    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


# print(outer())
print(len(outer.__doc__))
