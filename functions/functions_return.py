# Functions with Return statement

def build_full_name(firstname, lastname):
    """Returns full name"""
    print('Starting to build a full name...')
    full_name = f"{firstname} {lastname}"
    return full_name.title()


# print('Result of the function:', build_full_name('john', 'doe'))
# person2 = build_full_name('john', 'doe')
# print('Person2:', person2)

'''
ex 8-6
'''

def city_country(city: str, country: str):  # 'city: str' defines that city should be a string
    """Returns the name of the city with country"""
    return f"{city.title()}, {country.upper()}" # creates and saves the variable which can be reused/recalled anytime
    ## print(f"{city.title()}, {country.upper()}") # 'print' will not save the variable in the memory, non-recallable

## city_country('paris', 'france') # calling the function using 'print'
print(city_country('paris', 'france')) # printing 'return' function
print(city_country('london', 'uk'))
print(city_country('new york', 'usa'))


