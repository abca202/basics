# Exercise 9.5

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.

"""


from classes.classes_exercise9_3 import *
print()
# user3 = User('bob', 'martin', 33, 'mexico')
# user3.describe_user()

class User_login(User):

    # Additional method not given in the exercise
    username = 'john'
    password = '$Today2023'

    # Add an attribute called login_attempts to your User class
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.login_attempts = 0

    # Write a method called increment_login_attempts()
    # that increments the value of login_attempts by 1."""
    def increment_login_attempts(self):
        """ number of login attempts will be incremented by 1"""
        self.login_attempts += 1
        # self.login_attempts = self.login_attempts + 1 # same as above

    # Write another method called reset_login_attempts()
    # that resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        """ number of login attempts will be set to 0"""
        self.login_attempts = 0

    # Additional method not given in the exercise
    def login_to_website(self, username:str, password:str):
        # self.username = username # we skip this because global variables are given above
        # self.password = password
        if username.lower() == self.username and password == self.password:
            self.reset_login_attempts()
            print("You have logged in successfully. Welcome to your homepage.")
        else:
            if self.login_attempts > 3:
                print(f"Your account is locked, please try again later.")
            else:
                self.increment_login_attempts()
                print(f"Your username or password was incorrect. Try again later.")



# Make an instance of the User class
user4 = User_login('jane', 'doe', 28, 'france')
user4.describe_user() # this instance calling generates new user4 information provided above
print(f"Welcome {user4.first_name.title()} {user4.last_name.title()}!")
print()

# and call increment_login_attempts() several times.
user4.increment_login_attempts()
# Print the value of login_attempts to make sure it was incremented properly,
print(f"your login attempts = {user4.login_attempts}")

user4.increment_login_attempts()
# Print the value of login_attempts to make sure it was incremented properly,
print(f"your login attempts = {user4.login_attempts}")

user4.increment_login_attempts()
# Print the value of login_attempts to make sure it was incremented properly,
print(f"your login attempts = {user4.login_attempts}")

# and then call reset_login_attempts().
user4.reset_login_attempts()
# Print login_attempts again to make sure it was reset to 0.
print(f"your login attempts set to: {user4.login_attempts}")
print()

## Additional method calling, not from the exercise
user4.reset_login_attempts()
# print(f"Your total login attempts set to: {user4.login_attempts}")
user4.login_to_website('jane', 'ffs.ere')
print(f"1. Your total login attempts set to: {user4.login_attempts}")
user4.login_to_website('jim', '$Today2023')
print(f"2. Your total login attempts set to: {user4.login_attempts}")
user4.login_to_website('james', '%jfsdjaj')
print(f"3. Your total login attempts set to: {user4.login_attempts}")
user4.login_to_website('jake', '$fjsaaf')
print(f"4. Your total login attempts set to: {user4.login_attempts}")
user4.login_to_website('john', '$Today2023')
print(f"5. Your total login attempts set to: {user4.login_attempts}")


