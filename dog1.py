#Initialisation

#Initialisation -> Relates to setting a particular data for an instance of a class
#Instantiation -> Is the creation of an instance of an object

class Dog:

    animal_kind = "canine"
    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"

fido = Dog("Fido", "Brown")

print()
print(fido.colour) #Brown
print(fido.bark()) #woof
# __init__
#Initialisation a class