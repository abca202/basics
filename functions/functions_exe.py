# Scenarios
# from functions_while_loop import fuzz_buzz # importing a certain function
# from functions_while_loop import * # importing all functions from the file
# from functions.functions_return import *


# fuzz_buzz()
# while_loop_decrement()
# while_loop_increment()

# print(city_country('paris', 'france')) # printing 'return' function
# print(city_country('london', 'uk'))
# print(city_country('new york', 'usa'))

## Defining a Function
def greet_user(username):
    print(f"Hello {username.title()}!")


# greet_user('mr.t')
# username is variable and in function it is called 'parameter'
# the value 'mr.t' is called an 'argument'


## Positional and Keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


# describe_pet('dog', 'pushka') # positional arguments (dog(animal_type), pushka(pet_name))
# describe_pet(animal_type='dog', pet_name='pushka') # keyword arguments
# describe_pet(pet_name='pushka', animal_type='dog') # keyword arguments


## Default (optional) values for parameters in the function
def describe_pet(pet_name,
                 animal_type='dog'):  # when setting default values for parameters, they have to be placed after non-default parameters
    # def describe_pet(animal_type='dog', pet_name): # this parameters order is incorrect!
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


# describe_pet(pet_name='pirate')
# describe_pet('pirate') # same as above
# describe_pet(animal_type='cat', pet_name='murka') # keyword argument method/format
# describe_pet('murka', animal_type='cat') # positional/keyword argument format with a new argument for 'animal_type' parameter
# describe_pet('murka', 'cat') # positional argument format with a new argument for 'animal_type' parameter

## Return function
def get_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# musician = get_full_name('john', 'doe')
# print(musician)
# print(get_full_name('john', 'doe')) # gives the same result but without creating a variable


## Making an Argument optional

def get_full_name(first_name, last_name, middle_name=''):  # middle name is optional argument, can be called or ignored
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# musician = get_full_name('nodirbek', 'iskhakov')
# print(musician)
# # print(get_full_name('john', 'doe')) # gives the same result but without creating a variable
# musician = get_full_name('nodirbek', 'iskhakov', 'batirovich')
# print(musician)


## Returning a Dictionary

def member(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


# musician = member('john', 'doe')
# print(musician)


## Optional value in dictionary

def member(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# musician = member('john', 'doe', age=27)
# print(musician)


## Using a function with a 'while loop'

def get_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First Name: ")
#     l_name = input("Last Name: ")
#
#     formated_name = get_full_name(f_name, l_name)
#     print(f"Hello, {formated_name}!")

# This is breakable loop with 'Break Statement'
# while True:
#     print("\nPlease tell me your name:")
#     print("Enter 'q' at any time to quit")
#
#     f_name = input("First Name: ")
#     if_statement f_name == 'q':
#         break
#
#     l_name = input("Last Name: ")
#     if_statement l_name == 'q':
#         break
#
#     formated_name = get_full_name(f_name, l_name)
#     print(f"Hello, {formated_name}!")
#


## ex.8-6. City Country Names

def city_country(city:str, country: str):

    return f"{city.title()}, {country.upper()}"

# print(city_country('santiago', 'chile'))
# print(city_country('brasilia', 'brazil'))
# print(city_country('buenos aires', 'argentina'))



## ex 8-8. Album

def make_album(artist_fn, artist_ln, title):
    singer = {'first': artist_fn, 'last': artist_ln, 'album': title}
    return singer

# artist = make_album('lenny', 'cravitz', 'love')
# print(artist)


## Passing a List

def great_users(names):
    for name in names:
        msg = (f"hello {name.title()}!")
        ## msg = "Hello, " + name.title() + "!" ## sames as above
        print(msg)

# usernames = ['hannah', 'john', 'mary']
# great_users(usernames)

## ex 8-9. Magicians
def show_magicians(magic_names):
    for name in magic_names:
        print(name.title())

magicians = ('focus', 'pokus', 'abrakadabra')
show_magicians(magicians)

print()
## ex 8-10. Great Magicians

def make_great(magic_names2):
    for name in magic_names2:
        msg = (f"Hello, {name.title()}")
        print(msg)

magicians = ('focus', 'pokus', 'abrakadabra')
make_great(magicians)


## ex. 8-11. Unchanged Magicians



