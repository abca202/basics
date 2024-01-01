# # SLICING the list:
num_list = [2, 7, 4, 6, 3, 9, 5, 1]
# print(f"the original list of numbers: {num_list}")
# print(f"sliced list from index 1 to 5 (index 5 excluded): {num_list[1:5]}")

## another way of slicing by creating a new list
# new_list = num_list[1:5]
# print(new_list)
## more of slicing
print(f"original list: {num_list}")
print(f"sliced num_list[:5]: {num_list[:5]}")
print(f"sliced num_list[2:]: {num_list[2:]}")
print()

new_list2 = []
for num in num_list[:5]:
    new_list2.append(num)
print(f"new_list2: {new_list2}")
print(f"original list: {num_list}")
print()

print("Looping through the slice of the list")
for num in num_list[1:5]:
    print(num)
print()

num_list = [2, 7, 4, 6, 3, 9, 5, 1]
print("original list:", num_list)
print(num_list[1:5]) ## 1:5 means from index 1 up to index 5, not including index5
print(num_list[:4])
print(num_list[2:])
print(num_list[:])

## NOTE: if you don't mention start than default is 0
## NOTE: if you don't mention end than default is -1 or last index


