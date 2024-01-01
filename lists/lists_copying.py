## COPYing the list

num_list = [2, 7, 4, 6, 3, 9, 5, 1]
print("copying the original list 'num_list'-------------------")
num_list1 = num_list ## 'num_list1' is equal to the original 'num_list'; whatever happens with either list will be mirrored
num_list2 = num_list[:] ## 'num_list2' is not the same as 'num_list'; modification would not affect neither list
print(num_list)
print(num_list1)
print(num_list2)
print()

print("after modifying --------------------")
print('original list:', num_list)
num_list.append(11)
num_list1.append(33)
num_list2.append(44)
num_list2.append(77)
print('added 11 to the original list:', num_list) ## modification will not affect 'num_list2'
print('added 33 to the list1 >> original list:', num_list1) ## modification will not affect 'num_list2'
print('added 44 to the list2:', num_list2) ## modification will not affect original list and 'num_list1'
print('added 77 to the list2:', num_list2) ## modification will not affect original list and 'num_list1'
print('original list was not affected by modification of num_list2:', num_list)
print('num_list1 was not affected by modification of num_list2:', num_list1)
print()

### LOOPing through the Slice of the list:
print("LOOPing through the Slice of the list:---------------")
for num in num_list[1:5]:
    print(num)
print()


