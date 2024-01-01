# Exercise 9.9

"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.

"""

# Use the final version of electric_car.py
from classes.class_inheritance import ElectricCar
from classes.working_with_classes import Car
print("******************************************\n")

# Add a method to the Battery class called upgrade_battery().
class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def get_range(self):
        """ Print a statement about the range this battery provides."""
        # global range
        range = 0
        if self.battery_size == 70:
            range = 260
        elif self.battery_size == 85:
            range = 310

        # message = f"This car can go approximately {range}
        # message += "miles on a full charge."
        # print(message)
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 85:
            print(f"Your car's battery size is {self.battery_size}, which is lower than the national standard. "
                  f"You are eligible for an upgrade.")
            self.battery_size = 85
            print(f"Battery size got upgraded to 85 kwh.")
        else:
            print("Battery size is at the upgraded level.")


class ElectricCar(Car):
    """ Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

print('Check the battery of this electric car:')
electric_car1 = ElectricCar('Rivian', 'R1T', 2022)
electric_car1.battery.get_range()

print('\nCheck the upgraded battery of this electric car:')
electric_car1.battery.upgrade_battery()
electric_car1.battery.get_range()


