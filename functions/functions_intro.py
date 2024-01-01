# CHAPTER 8: FUNCTIONS
# Defining, executing, docstring
# overriding - resetting the content with same name
# wrong way of using function: calling before defining
# functions with parameters (arguments are passed when you execute)
# executing functions with positional arguments
# executing functions with parameters and arguments mentioned, position does not matter
# keyword and argument


# Built-in functions: print(argument), input(), list.append(), sorted(),

# User Defined Functions (created by a user)
# Declaring the function name and defining the function
def greet_user():
    print("hello class!")
    print("wonderful sunny day today!")


# # Registering in the python execution system

# # overriding the function
def greet_user():
    print("hello class!")
    print("Enjoy your day!")


# # Execution: call the function
# greet_user()
# print('logged in to the system')
# greet_user()
#
# print()


# Keyword 'name'
def greet_user_by_name(name): # defining a function
    """ function with argument: positional argument, required """
    print(f"Hello, {name.title()}!")
    print("Enjoy your day!")
#
# greet_user_by_name('tony') # calling the function
# print()

# giving multiple argument names and parameters
def greet_user_by_name(name, day_of_week): # defining a function
    """ function with argument: positional argument, required """
    print(f"Hello, {name.title()}!")
    print(f"Enjoy your {day_of_week.title()}!")
#
# greet_user_by_name('bob', 'friday') # calling the function
# print()
#
# changed argument positions:
def greet_user_by_name(name, day_of_week): # defining a function
    """ function with argument: positional argument, required """
    print(f"Hello, {name.title()}!")
    print(f"Enjoy your {day_of_week.title()}!")
#
# greet_user_by_name(day_of_week='monday', name='jane') # calling the function by the specific parameter name
## 'day_of_week'-> keyword, 'monday'-> argument


# default values
def greet_user_by_name_with_def(name, day_of_week='monday'): # 'day_of_week' has a default value
    """     function with default value: name is required, day_of_week is not required    """
    print(f"Hello, {name.title()}!")
    print(f"Enjoy your {day_of_week.upper()} today.")
#
# greet_user_by_name_with_def("nina", 'sunday') # new value for 'day_of_week' is given
# greet_user_by_name_with_def("bill") # only one argument is given, the default second argument value is used
# greet_user_by_name_with_def("bill", 'thursday') # only one argument is given, the default second argument value is used
# # greet_user_by_name_with_def(day_of_week='wednesday') # only one argument is given, the default second argument value is used
# greet_user_by_name_with_def('jane', 'saturday')

## exercise 8-3
def make_shirt(size, txt_to_print):
    """ prints message and size of the shirt """
    print(f"The size of your shirt is {size.title()}.")
    print(f"The message to be printed on your shirt is: \n\t\t'{txt_to_print.upper()}'.")

make_shirt('medium', 'super nova!')  # positional argument method used
make_shirt(txt_to_print='super Nova!', size='large')  # keyword argument method used
make_shirt(size='small', txt_to_print='Super nova!')  # keyword argument method used
