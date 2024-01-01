# Exercise 9.7

"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method

"""
from classes.classes_exercise9_3 import *
print()

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        """ Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on."""
        super().__init__(first_name, last_name, age, country)
        self.privileges = ["can add post", "can delete post", "can add user", "can ban user"]

    # Write a method called show_privileges()
    # that lists the administrator’s set of privileges.
    def show_privileges(self):
        print(f"Admin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


# Create an instance of Admin, and call your method
admin1 = Admin('mike', 'tyson', 37, 'russia')
admin1.privileges = ["can add post", "can delete post", "can add user", "can ban user"]
print(f"Admin information: {admin1.first_name.title()} {admin1.last_name.title()}, "
      f"{admin1.age}, {admin1.country.upper()}")
admin1.show_privileges()

