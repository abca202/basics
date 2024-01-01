# Exercise 9.8
"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.

"""
from classes.classes_exercise9_7 import *
print()

# Write a separate Privileges class.
class Privileges(Admin):
    def __init__(self):
        """ The class should have one attribute, privileges,
        that stores a list of strings as described in Exercise 9-7."""
        self.privileges = []

    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t{privilege}")
        else:
            print(f"\nNo privileges.")

# Make a Privileges instance as an attribute in the Admin class.
class Admin(User):
    # privileges = Privileges()

    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.admin_privileges = Privileges()

    def test(self):
        print('privileges:')
        print(self.admin_privileges.show_privileges())

# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.
admin1 = Admin('jackie', 'chan', 40, 'china')
admin1.describe_user()
admin1.admin_privileges.show_privileges()
admin1.admin_privileges.show_privileges()

print('\nNew addition ->')
admin1_privileges = [
    'can override error',
    'can reset account',
    'can moderate comments'
]
# admin1 is the object of Admin class
# admin_privileges is the object inside the Admin class
# list_of_privileges is the attribute inside Priviliges class
admin1.admin_privileges.privileges = admin1_privileges

# list_of_privileges is the method (behavior) inside
admin1.admin_privileges.show_privileges()

# why we need object in the class?
admin1.test()
admin1.admin_privileges