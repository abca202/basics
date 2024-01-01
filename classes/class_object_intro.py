# Chapter 9: Classes and Objects Intro

# Class is a model/template and Object is a sample derived from the model(class)

#### Interview question:
'''
# What is the difference between class and object?
        - Class is a template, a model; and Object is the instance/sample which is created using that template/model (class).
        - Instance of a class is object: sample that was created based on the class is called object.
        - Object is specific(customized) whereas class is general(standardized)
        - using a class we can create many objects/instances
'''


# PEP8: guidelines
# use combination of lowercase letters and underscores for:
# package, folder, file, variable (object of class), functions names
# use combinations of title case for:
# class has attributes (variables) and behavior (functions)
# 'self' keyword shows that function or variable belongs to the current class

## outside of the class variable:
msg = 'wouf wouf'
breed = 'General'

class Dog: # use UPPPER case for class name
    """Model of dogs, template for dogs."""

    # CLASS will have 'ATTRIBUTE' (description) - variables, instance variables
    # they are global variables
    # these variables are changeable if they are defined in constructor '__init__'

    # name = 'pushka' # default-optional >> commented out because it is defined in the Constructor
    # breed = 'no breed' # default-optional >> commented out because it is defined in the Constructor
    size = 'medium' # not defined in the Constructor
    age = '2' # not defined in the Constructor
    # color = '' # >> commented out because it is defined in the Constructor

    # CONSTRUCTOR (of the class when you instantiate) >>> we need it in the Class to make it easier to customize attributes
    """ 
    # __init__ function will override the global variable values (name='pushka', breed='no breed')
    # everything defined in the Constructor does not have to be defined in the Class Global variable!!! 
    # if the attribute is defined in the Constructor than later while instantiating we wouldn't have to update >>> 
         >>> any of the default variables in the separate line
    # for example: if we define 'name' in the constructor than later there is no need to assign a new value to the 'name' for an object
    # it means we don't have to write: "dog1.name = 'charlie'"; instead we will just include it in the 'Dog' class while creating a new object:
        # dog1 = Dog('charlie', ...) >> and there is no need for an extra line: dog1.name  = 'charlie'
    """

    ## def __init__(self)
        # default function to make required arguments
        # executed automatically everytime when you create an object (instance)
    def __init__(self, nm, brd, clr): # '__init__' is the method
        self.name = nm # not global variable
        self.breed = brd # not global variable
        self.color = clr # not global variable
        # 'size', 'age' were not defined in the Constructor function, therefore they will not get overrided
        # print(f"{self.breed} {msg}") # 'self.breed' will use local class attribute; 'msg' is outside class variable
        # print(f"{self.breed} {breed}") # same as above

    # CLASS will have 'BEHAVIOR' (actions) - functions
    def eat(self):
        print(f"{self.name} is eating...")
        print(f"{self.name} wants more...")
        print(f'{self.name} done eating...')

    def run(self):
        miles = 5 # local variable belonging to the function 'run' only
        print(f"{self.name} is running")
        print(f"{self.name} is running {miles} miles.")
        # run() # outside of the class
        # self.run() # inside the class

    def get_description(self):
        print(f"Name of the dog is: {self.name}")
        print(f"Breed of the dog is: {self.breed}")
        print(f"Size of the dog is: {self.size}")
        print(f"Age of the dog is: {self.age} years old")
        print(f"Color of the dog is: {self.color}")


# Instantiation - creating instance/sample of the class - creating object/sample -> executing class
# dog1, dog2 are objects

## Before adding 'def: __init__' >> dog1 = Dog() # copying everything from the model 'Dog' to a new object 'dog1'
## After adding def: __init__': >> we will need to give attribute values in the Dog() class
print('-------------------dog1 attribute--------------------------')
dog1 = Dog('charlie', 'chow chow', 'white') # giving new attribute values to the 'dog1' object (name, breed, color)
print('name of the dog by default is', dog1.name.title())

dog1.name = 'pirate'  # assigning a new value to the attribute 'name'
print('name of the dog after reassigning a new name is', dog1.name.title())
print()


print('dog1 breed default value is', dog1.breed.title())
dog1.breed = 'doberman' # assigning a new value to the attribute 'breed'
print('dog1 breed value after assigning new value is', dog1.breed.title())
print()

print('-------------------dog1 behavior(function)--------------------------')
dog1.eat()
print()


Dog.run(self=Dog) # using default attributes
dog1.run() # correct
print()

print('-----------Description of the dog1--------------')
dog1.get_description()
print()

print('-------------------dog2--------------------------')
dog2 = Dog('max', 'german sheppard', 'black and yellow')
print('dog2 name changed to', dog2.name)
print('dog2 breed changed to', dog2.breed)
dog2.age = 5
dog2.size = 'big'
print()
dog2.get_description()

#### Interview question:
''' 
- What is the difference between class and object?
        - Class is a template, a model; and Object is the instance which is created using that template/model (class).
        - Instance of a class is object: sample that was created based on the class is called object.
        - Object is specific whereas class is general
        - using a class we can create many objects/instances
'''

