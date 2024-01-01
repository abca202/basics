## CHAPTER 3. LIST SORTING

#### PERMANENT SORTING ASC
cars = ['tesla', 'bmw', 'lada', 'nissan']
print("Permanent sorting - sort().")
print("List before sorting: ", cars)
cars.sort() ## sorting in ascending order
print("List after sorting: ", cars)
print()

#### PERMANENT SORTING DESC
print("Permanent sorting in reversed/descending order")
names = ['john', 'mark', 'steve', 'alex']
print("List before sorting: ", names)
names.sort()
print("list after default/ascending sorting: ", names)
names.sort(reverse=True) ## permanent sorting in reversed/descending order
print("List after reversed/descending sorting: ", names)
print()

##### TEMPORARY SORTING ASC
car_models = ['model x', '750 i', '21099','maxima']
print("Temporary sorting - sorted().")
print("Car models before sorting: ", car_models)
temp_sorted_car_models_asc = sorted(car_models)

##### TEMPORARY SORTING DESC
temp_sorted_car_models_desc = sorted(car_models, reverse=True)
print("Car models after sorting: ", car_models)

print("Sorted car models after sorting in asc order: ", temp_sorted_car_models_asc)
print("Sorted car models after sorting in desc order: ", temp_sorted_car_models_desc)
print('Original list: ', car_models)
print()


#### REVERSING PERMANENTLY ASC
print("Reversing a list without sorting")
nums = [6, 2, 0, 8, 3]
print("List before reversing: ", nums)
nums.reverse()
print("List after reversing: ", nums)
print()

#### LEN function to count the number of elements in the list
print("# number of elements in the list len()")
print('number of elements in the nums list is: ', len(nums))
print('number of elements in the names list is: ', len(names))
print('number of elements in the cars list is: ', len(cars))
print('number of elements in the car_models list is: ', len(car_models))
print('last index in the car_models list is: ', len(car_models)-1)

#### SORTING a list Permanently with sort() method
# print("Sorting a list Permanently with sort() method")
# print(cars)
# cars.sort() # sorting by default in ASC order
# print(cars)
# cars.sort(reverse=True) # sorting in DESC
# print(cars)

# print("Sorting a list Temporarly with sorted() method")
# print("sorted list:", sorted(cars)) # doesn't create a new list; just displays the result
# print("original list: ", cars)
# cars_sorted = sorted(cars) # creating a new list 'cars_sorted' by assigning 'sorted(cars)' value
# print("cars sorted in asc order by default: ", cars_sorted)
# cars_sorted_desc = sorted(cars, reverse=True)
# print("cars sorted in desc order: ", cars_sorted_desc)

#### REVERSING the list Permanently >> NO SORTING happens with the 'list.reverse()'
# cars.reverse()
# print("reversed list: ", cars)

#### FINDING the Length of the list -  how many elements are there in the list?
# num_of_cars = len(cars)
# print("the length of the cars list: ", len(cars))
# print("the length of the cars list: ", num_of_cars)
# # the last index is always 1 less than the length of the list
# print("the last index in the list is: ", len(cars) -1)
# # Always make sure that the index that being searched is within the index range of the list





