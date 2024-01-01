# basics ch.2-4

## Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")


## Using the range() Function
for value in range(0,5):
    print(value)
print()

## Using range() and list() functions to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

## list the even numbers between 0 and 4:
even_numbers = list(range(0,5,2))
for num in even_numbers:
    print(num)
print(even_numbers)
print()

##  make a list of the first 10 square numbers
## (that is, the square of each integer from 1 through 10)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    # print(squares)
print(squares)
print()

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)



