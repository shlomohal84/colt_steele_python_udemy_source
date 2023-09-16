class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        return f'YOU WANT "{key}"? WELL IT AIN\'T HERE'

    def __setitem__(self, key, value):
        print("DO YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("NO IT AIN'T HERE!")
        return False


data = GrumpyDict({"first": "Tom", "Animal": "Cat"})
print(data)
print(data["last"])
data["first"] = "Major"
print(data)

print("city" in data)
