import sys
from colorama import init
from termcolor import colored, cprint

init()

print(
    colored(
        "HEY THERE",
        color="magenta",
        on_color="on_cyan",
        attrs=["blink", "concealed", "reverse"],
    )
)
