class Pet:

    allowed = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species


cat = Pet("Blue", "cat")
cat.set_species("rat")
dog = Pet("Wyatt", "dog")

# print(Pet.allowed)

# Pet.allowed.append("dragon lizard")

# print(Pet.allowed)

# dog.set_species("dragon lizard")
# print(dog.species)


# print(cat.allowed)
# print(id(cat.allowed))
# print(dog.allowed)
# print(id(dog.allowed))

# print(id(Pet.allowed))

# grizzly_bear = Pet("Baloo", "grizzly bear")
