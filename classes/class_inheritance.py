# Chapter 9. Class Encapsulation and Inheritance >> reuse the code from other classes

# class A is parent of class B
# class B inherits class A
# class B (child) has access to everything that class A has

## For example: let's create class A and class B will inherit all from class A
class A:
    name = 'i am from class A'

    def greet(self):
        print('Hello!')

class B(A):
    age = 25

    def get_age(self):
        print(f"My age is: {self.age}")

# class C(B):
    # pass
    """ 
    if class C inherits class B than since class B inherited class A, 
        class C will inherit both A and B
    """
#class C (A,B):
    # pass
"""
- if class B is independent of class A >> hasn't inherited from A,
    than class C(A,B) > class C can inherit from both A and B
"""
# object of class B has access to attributes and method of class A and B
item1 = B()
print(item1.name)
print(item1.age)
item1.greet()
item1.get_age()

# parent class DOES NOT have access to child class's attributes and methods
item2 = A()
print(item2.name)
item2.greet()

print()


print("---------- Implementing inheritance concept with Car class  ------------")

from classes.working_with_classes import Car # imported class Car from 'working_with_classes.py' file

print("---------------------------------------------------")
class ElectricCar(Car):


    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # super().__init__() executes the constructor of the parent class
        self.battery_size = 80


    def get_description(self):
        super().get_description()
        print(f"Battery size: {self.battery_size}")



    def fill_tank(self):
       """
       we aew overriding the 'fill_tank()' function from the parent class
       :return:
       """
       print("Sorry, this car does not have a gas tank. Please go to the electric charging station.")

ecar1 = ElectricCar('tesla', 'model X', 2022)
ecar1.get_description()
ecar1.fill_tank()
ecar1.get_description()

print("-----------------------------------------")
car1 = Car('bmw', 'x7', '2022')
car1.fill_tank()
car1.get_description()


