#Class example with constructor
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

    pass
#Class instance methods
class BankAccount:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0.0
        pass
    def balance(self):
        return self.balance

    def deposit(self,depot):
        self.balance+=depot
        return self.balance
    def withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        return self.balance

    #class attribute
    class Chicken:
        total_eggs = 0

        def __init__(self, species, name):
            self.species = species
            self.name = name
            self.eggs = 0

        def lay_egg(self):
            self.eggs += 1
            Chicken.total_eggs += 1
            return


# Inheritance Example Using Super()
# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")



blue = Cat("Blue","Scottish Fold", "String")
blue.play()


class Character:
	def __init__(self, name="bob", hp=0, level=0):
		self.name = name
		self.hp = hp
		self.level = level


class NPC(Character):
	def __init__(self, name, hp, level):
		super().__init__(name, hp, level)

	def speak(self):
		return "{0} says: 'I heard monsters running around last night!'".format(self.name)


class Aquatic:
	def __init__(self,name,fins):

		print("Aqua Init")
		self.fins=fins
		self.name=name
	def swim(self):
		return f"{self.name} is swimming with its {self.fins} fins"
	def greet(self):
		return f"I am {self.name} of the sea"

class Ambulatory:
	def __init__(self,name,legs):
		print("Amb INIT")
		self.name=name
		self.legs=legs
	def walk(self):
		return f"{self.name} is walking with its {self.legs} legs"
	def greet(self):
		return f"I am {self.name} of the land!"

class Penguin(Ambulatory,Aquatic):
	def __init__(self,name,legs,fins):
		print("Penguin Init")
		Aquatic.__init__(self,name=name,fins=fins)
		Ambulatory.__init__(self,name=name,legs=legs)
	def greet(self):
		return f"Happy feet {self.name} greets you"


captain_cook=Penguin("Captain Cook",2,2)

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())
print(Ambulatory.greet(captain_cook))
#print(Penguin.mro())
#help(Penguin)


#Common (Magic) def
class Train():
    def __init__(self,num_cars):
        self.num_cars=num_cars
    def __repr__(self):
        return "{} car train".format(self.num_cars)
    def __len__(self):
        return self.num_cars
