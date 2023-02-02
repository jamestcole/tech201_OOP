# Object Oriented Programming (OOP)

# Everything in OOP is an object and objects are modelled against

# Classes are the temlates we use to create objects
# Classes are a of bringing beth data and functionality of our code together

# Create a class

class Dog:

    animal_kind = "canine" #class variable

    def bark(self): # method
        return "woof"

#self - "I'm referring to the current class.
#print(Dog.animal_kind) #canine
#print(Dog.bark()) # ERROR
#print(Dog.bark())
#Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(lassie)) #<class '__main__.Dog'>

print(fido.bark()) #woof

print(lassie.animal_kind) #canine

print(fido.bark()) #woof
lassie.animal_kind = "Monkey"
fido.animal_kind = "Dolphin"
print(fido.animal_kind) #New outputs Dolphin
print(lassie.animal_kind) #New outputs Monkey

print(fido.bark(),lassie.bark()) #woof woof