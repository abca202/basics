## Conventional way of working with range() and append()
num_list = []
for i in range(10, 20, 2):
    num_list.append(i**2)
print(num_list)
print()


## Comprehensive way
num_list = [i ** 2 for i in range(10, 20, 2)]
print(num_list)
print()


## List Comprehension: simplifying the code
## Orignal code:
# even_nums = [] ## creating an empty list
# for num in range(100, 150, 2): ## looping a range
#     even_nums.append(num ** 2) ## squaring number and adding it to the empty list
# print(even_nums)
# print()

## Comprehensive code:
even_nums = [num**2 for num in range(2, 21, 2)]
print(even_nums)
print()




