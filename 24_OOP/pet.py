class Pet:
	allowed = ['cat','dog','fish','rat']
	def __init__(self,name,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species
	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!") 
		self.species = species

cat = Pet("Blue","cat")
dog = Pet("Belle","dog")
# tony = Pet('Tony',"tiger")
print(id(cat.name))
print(id(dog.name))
print(id(Pet.allowed))
