from pyfiglet import figlet_format
from termcolor import colored
from requests import get
from random import choice


def print_splash_screen(msg, color):
    valid_colors = (
        "grey",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    )
    if color not in valid_colors:
        color = "magenta"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


print_splash_screen("DAD JOKE 3000", "fewfwe")


def run_prompt():
    game_over = False
    counter = 1

    while not game_over:
        url = "https://icanhazdadjoke.com/search"
        print("-" * 50)
        user_input = input("Let me tell you a joke! Give me a topic: ")
        if user_input == "/quit":
            game_over = True
            print("\nGoodbye!")
            break
        limit = input("Type your desired search result amount: ")

        data = get(
            url,
            headers={"Accept": "application/json"},
            params={"term": user_input, "limit": limit},
        ).json()

        num_jokes = data["total_jokes"]
        jokes = data["results"]

        if num_jokes > 1:
            random_joke = choice(jokes)
            print(f'\nI\'ve found {num_jokes} jokes about "{user_input}"')
            print(choice(jokes)["joke"])

        elif num_jokes == 1:
            print(
                f"I've got one joke about \"{user_input}\". Here it is:\nJoke: {jokes[0]['joke']}"
            )
        else:
            print(f"Sorry i don't have any jokes about {user_input}. Please try again")


run_prompt()
