# Chapter 9: Working with Classes and Instances

# ObjectOrientedProgramming (OOP) concepts - class, object, encapsulation
# Encapsulation - hiding from the object, child classes

class Car:
    # what attributes I need to have? which are required (put them in '__init__') and which are optional (default)?
    # attribute - required, optional (default)
    # behavior - CRUD -> set (setter) (create, UPDATE, delete), get (getter) (READ), other functions (create, delete)

    def __init__(self, make, model, year):  # 'make, model, year' >> local variables (required)
        self.make = make  # self.make >> assigning local variables to a global variable (belongs to class Car)
        self.model = model
        self.year = int(year) # use 'int' function
        # self.mileage = 0 # this was before encapsulation
        self.__mileage = 0    # we need to hide it from the object so he cannot play with it as he wished, child classes >> encapsulation

    def get_description(self):
        """gets detail of a car"""
        print(f"Car details: \n\tManufacturer: {self.make.upper()}\n\tModel:{self.model.upper()}\n\tYear:{self.year}")
        # return f"Car details: \nManufacturer: {self.make}\nModel:{self.model}\nYear:{self.year}"
        print(f"Current Mileage: {self.__mileage}")

    def set_mileage(self, new_mileage):
        """ sets the mileage not less than current mileage"""
        if new_mileage > self.__mileage:
            print("Setting new value to the mileage\n")
            self.__mileage = new_mileage
        else:
            print("Entered mileage was less than current mileage, cannot be updated\n")

    def add_to_mileage(self, miles):
        """ increments the mileage with given miles"""
        if miles > 0:
            self.__mileage = self.__mileage + miles
            # self.__mileage += miles >> same as above
            print(f"{miles} miles were added to your car mileage.")
        else:
            print("You cannot input a negative number to increment mileage.")


    def fill_tank(self):
        print("Filling the tank with gas ...")
        print("Done! It is ready to hit the road.")



car1 = Car('bmw', 'x5', '2023')
# print(car1.make, car1.year + 1)

# print("## GETTER functions")
car1.get_description()
# print(car1.get_description())

# print("## SETTERs - updating values of attributes")
car1.model = 'x7m'

# # car1.__mileage = 50 # since mileage is hidden from the object we cannot update the value
car1.set_mileage(50)
car1.get_description()

car1.set_mileage(10)
# car1.__mileage = 10 # setting a new value >> logically it is not appropriate to lower the mileage of the car, therefore there should be certain restriction
car1.get_description()
# # input: 100, -15

car1.add_to_mileage(100)
car1.get_description()

car1.add_to_mileage(-15)
car1.get_description()


# make = input("enter the make of the car: ")
# model = input("enter the model of the car: ")
# year = input("enter the year of the car: ")
# car2 = Car(make, model, year)



