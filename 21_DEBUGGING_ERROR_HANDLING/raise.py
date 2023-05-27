def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")

    if type(text) is not str:
        raise TypeError("text must be an instance of string")
    if type(color) is not str:
        raise TypeError("color must be an instance of string")
    if color not in colors:
        raise ValueError(f"{color}is invalid color")
    print(f"Printed {text} in {color}")


colorize("hello", 5)
colorize(5, "magenta")
colorize("Meowdy", "purple")
