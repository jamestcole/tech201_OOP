# tech201_OOP
tech201_OOP
# Object Oriented Programming (OOP)

- Everything in OOP is an object and objects are modelled against
- Classes are the temlates we use to create objects
- Classes are a of bringing beth data and functionality of our code together

## Classes
Create a class

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

# Methods

# class MethodExamples:
#
#     this_can_be_accessed_easily = "Hi, I am easily found!"
#
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hi, I am easily found!"
#
#
# x = MethodExamples()
#
#
#
# print(x.this_can_be_accessed_easily) #Hi, I am easily found!
# x.this_can_be_accessed_easily = "I have been changed"
# print(x.this_can_be_accessed_easily) #I have been changed



# in most languages public and private must be specified but in python , __init__ can still be accessed
class MethodExamples:
    #this_can_be_accessed_easily = "Hi, I am easily found!"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, I am easily found!"

    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self.this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()
print(x._this_can_be_accessed_easily) #Hi, I am easily found!
x.set_this_can_be_accessed_easily = "I have been changed"
print(x._this_can_be_accessed_easily) #I have been changed

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