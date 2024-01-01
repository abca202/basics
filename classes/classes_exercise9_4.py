# Exercise 9.4
"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num￾ber you like that could represent how many customers were served in, say, a
day of business.

"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        """ Add an attribute called number_served with a default value of 0"""
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of the restaurant is: {self.restaurant_name}.")
        print(f"This is: {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name} everyone! We are now open!")

    def set_number_served(self, new_number_served):
        """Add a method called set_number_served() that lets you set the number of customers that have been served."""
        self.number_served = new_number_served

    def increment_number_served(self, num_served):
        """Add a method called increment_number_served() that lets you increment the number of customers that have been served.
        :param num_served: numbers that number_served to be incremented by
        :return:
        """
        self.number_served += num_served



# Create an instance called restaurant from your class.
restaurant1 = Restaurant("Brooklyn Pizza", 'Italian')
print(restaurant1.describe_restaurant())

# Print the number of customers the restaurant has served
print(f"Number of customers restaurant served: {restaurant1.number_served}")

# and then change this value (0) and print it again
restaurant1.number_served = 15
print(f"Number of customers restaurant served: {restaurant1.number_served}")

# Call set_number_served() method with a new number and print the value again
restaurant1.set_number_served(20)
print(f"Number of customers restaurant served: {restaurant1.number_served}")

# Call increment_number_served() method with a any number you like that could represent how many customers were served
# in a day of business
restaurant1.increment_number_served(7)
print(f"Number of customers restaurant served: {restaurant1.number_served}")

