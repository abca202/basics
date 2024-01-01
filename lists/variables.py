# This is my first file, this line is comment line for me to put some description
# comment line will always be ignored by execution

# VARIABLE - temp storage while your program runs, during execution time
message = "hello world"
# message is the name of the variable
# "hello world" is the value, '=' is setting a value to a variable
# print(message)
# print()

# Variable naming rules:
# - start the name with the lower case
# - do not start with indentation
# - do not start the variable with the number
# - do not use a space in the name between to words : 'variable name' -> not good; 'variable_name' -> good
# - do not use too short or too long names for variables


# Data types:
# # primitive data: string(text), num (int, float, doubles), boolean (true/false), None
msg = "I am a string data type"
note = 'oh I am also a string data type'
num = 456
price = 99.99
result = True
truth = False
something_else = None
#
# # Debug - shows what is going on in the background/behind the scene; those items that we didn't print
#
# print(msg, note, num, price, result, truth, something_else)
# print(note)
#
# note = 'oh I am an updated value of the note!'
# print(msg, note, num, price, result, truth, something_else)
# print(note)
# print()
#
# # String, What we can do with string variable: we can change the key cases
# print(note.title())
# print(note.upper())
# print(note.lower())

# Data types: string - text (word, latter, long paragraph,..); it is covered by 'single' or "double quotes"
# some useful functions(methods) that are built-in in python
# What is function? - example here is print() function
# print('hello', 'hi', 2)
# print('hello\n', 'hi\n', 2)
# print('ola', 'oley', 4)
# print('\t\t\t\t\thello\n\n', '\t\t\t\t\t\thi\n', 2)

# print(message.upper())
first_name = 'john'
last_name = ('doe')

# print(first_name.title()+ " " +last_name.upper()) # concatenation
#
# full_name = first_name.title() + last_name.upper()
# print(full_name)
# full_name = first_name.title() + " " +last_name.upper()
# print(full_name)
# full_name = first_name.title() + "\t" + last_name.upper()
# print(full_name)
# print(first_name, last_name)

# Concatenation using f-string
# fname = f"Full name is: {first_name.title()} {last_name.upper()}"
# print(fname)
#
# variableName = f"adding 23 to 42: {23+42}"
# print(variableName)

city = 'brooklyn'
# print(f"I lived in: {city}")
city = '            Brooklyn         '
street = '   Brighton street  '
# print(f"I lived in: {city.strip()}, {street.strip()}") # this function removes the whitespaces from either right or left of the string
# print(f"I lived in: {city.lstrip()}, {street}")
# print(f"I lived in: {city.lstrip()}, {street.lstrip()}")
# print(f"I lived in: {city.lstrip()}, {street.rstrip()}")
# print(f"I lived in: {city.lstrip()}, {street.strip()}")
# print(f"I lived in: {city.rstrip()}, {street.rstrip()}")
# print(f"I lived in: {city.rstrip()}, {street.lstrip()}")

############ variables and numbers #############
num1 = 21
num2 = 5
num3 = 30
# operations
# print(f"addition: {num1 + num2}")
# print(f"subtraction: {num1 - num2}")
# print(f"multiplication: {num1 * num2}")
# print(f"division: {num1 / num2}")
# print(f"exponent: {3 ** 2}")
# print(f"modulo: {num1 % num2}") # modulo/remainder from division of 21 by 5 = 1 - 'num1' is Odd number
# print(f"modulo: {num1 % 2}") # modulo/remainder from division of 21 by 2 = 1 - 'num1' is Odd number
# print(f"modulo: {num3 % 2}") # if_statement the modulo/remainder is 0 than 'num1' is Even number
# print(f"floor division: {num1 // num2}") # how many 5s in 21? - four 5s

# numbers: integers, floats(double)
# using numbers and strings
age = 25
age2 = "35"
# print("yay, I am " + str(age) + " now.")  # integer '25' converted into string
# print("yay, I am " + age2 + " years old.")  # two strings/texts are combined
# print("my brother is " + str(5 + int(age2)) + " years old.")  # string '35' converted into integer and '5' another int is added.
# print(f"my brother is {str(5 + int(age2))} years old.")  # same as above but using 'f' string

# int() converts number or string in to integer; returns 0 if_statement it is not convertible
# print(int(num1 / num2))  # 4.2 will be converted into 4 without decimals

a = 1000  # 'a' is a Variable and 1000 is a value (int)
a = a + 1  # the result of 1000 + 1 will be assigned and stored in a Variable 'a'; now 'a' will have a new value
## a += 1 >> is the same as above
# print(a)

# print("####### Usefull functions for strings ##########")
# print("# .title(), .upper(), .lower(), .islower(), .isupper(), .isdigit()")
name = 'john_Doe'
msg = 'Hello world!'
# print(name.isupper())
# print(name.istitle())
# print(name.isalpha())

# print("## Concatination ##")
# print("my message is: " + name + ', ' + msg)
# print("my message is: " + name.title() + ', ' + msg.upper())
# print("### Special Characters: \\t >> tab, \\n >> new paragraph")
# print("my message: \t\t\t" + name.title() + ',\n\n\n\t\t\t' + msg.upper())
# print("Message to everyone:\n\t\t\tPLEASE HAVE FUN!!!")
# print("Message to everyone:\n\t\t\t" + " please have fun!!!".title())

## strip(), rstrip(), lstrip() >> removes white space in the value of the variable
location = '  \thawaii\n\t'
# print(location)
# print(location.strip())
# print('my wedding venue: ' + location.strip().upper() + ' islands')

print('##### Working with numbers ########')
num1 = 21
num2 = 5
num3 = 30
# operations
# print(f"addition: {num1 + num2}")
# print("addition: ", num1 + num2)
# print(f"subtraction: {num1 - num2}")
# print("subtraction: ", num1 - num2)
# print(f"multiplication: {num1 * num2}")
# print("multiplication: ", num1 * num2)
# print(f"division: {num1 / num2}")
# print("division: ", num1 / num2)
# print(f"exponent: {3 ** 2}")
# print("exponent: ", 3 ** 2)

# print(" ######### Modulo ##########")
# print(f"modulo: {num1 % num2}") # modulo/remainder from division of 21 by 5 = 1 - 'num1' is Odd number
# print("modulo: ", num1 % num2) # modulo/remainder from division of 21 by 5 = 1 - 'num1' is Odd number
# print(f"modulo: {num1 % 2}") # modulo/remainder from division of 21 by 2 = 1 - 'num1' is Odd number
# print("modulo: ", num1 % 2) # modulo/remainder from division of 21 by 2 = 1 - 'num1' is Odd number
# print(f"modulo: {num3 % 2}") # if_statement the modulo/remainder is 0 than 'num1' is Even number
# print("modulo: ", num3 % 2) # if_statement the modulo/remainder is 0 than 'num1' is Even number
# print(f"floor division: {num1 // num2}") # how many 5s in 21? - four 5s
# print("floor division: ", num1 // num2) # how many 5s in 21? - four 5s

# find an odd numbers 20-50 -> 21(21=2*10+1), 23(23=2*11+1)
# if_statement n%2 returns 1 than 'n' is odd number (pseudocode)
# if_statement n%2 returns 0 than 'n' is even number (pseudocode)

print("#### str(expression) >> converts expression into a string")
# print("addition: "+ (num1 + num2))
print("addition: "+ str(num1 + num2))
num3 = '456' ## is a string because of ''
print(num3)
print("adding integer 21 to a string '456': ", num1 + int(num3))
num4 = 45.7566
print('converted to int:', int(num4))
print('converted to int and rounded up:', int(round(num4)))

