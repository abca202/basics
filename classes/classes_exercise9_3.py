# Exercise 9.3
"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.

"""
# Make a class called User
class User:
    def __init__(self, first_name, last_name, age, country):
        """ Create two attributes called first_name and last_name,"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        """ and then create several other attributes that are typically stored
            in a user profile.
        """

    def describe_user(self):
        """ Make a method called describe_user() that prints a summary
            of the user’s information."""
        print(f"The following is the user's information:")
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age} y.o")
        print(f"Country: {self.country.upper()}")

    def greet_user(self):
        """ Make another method called greet_user() that prints
            a personalized greeting to the user."""
        print(f"Welcome dear {self.first_name}, you are now logged in!\n")


""" Create several instances representing different users, and call both methods 
for each user."""

user1 = User('tony', 'montana', 21, 'usa')
user1.describe_user()
print(f"Welcome {user1.first_name.title()} {user1.last_name.title()}!")

print()

user2 = User('john', 'doe', 30, 'canada')
user2.describe_user()
print(f"Welcome {user2.first_name.title()} {user2.last_name.title()}!")
# print(user1.greet_user())
