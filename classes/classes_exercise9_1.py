#### Exercises

print("------------------- Ex.9-1 ------------------")


class Restaurant:
    """ here we started with creating a constructor with all global default attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        """ make both attributes global so other functions/methods can have access and use them"""
        self.restaurant_name = restaurant_name # this creates a global variable 'restaurant_name' in the class
        self.cuisine_type = cuisine_type # same as above

    def describe_restaurant(self): # method/function
        print(f"Name of the restaurant is: {self.restaurant_name}.")
        print(f"This is: {self.cuisine_type} restaurant.")

    def open_restaurant(self): # method/function
        print(f"Welcome to {self.restaurant_name} everyone! We are now open!")


# Create an instance called restaurant from your class.
# Restaurant name: Brooklyn Pizza
# Cuisine type: Italian
restaurant1 = Restaurant("Brooklyn Pizza", 'Italian')

print('---- Printing two attributes individually ----')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

print('---- and then callng both methods. ----')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
