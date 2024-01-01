############ Exercises ############
'''
ex.3-4.  If you could invite anyone, living or deceased, to dinner, who
would you invite?
- Make a list that includes at least three people you’d like to
invite to dinner.
- Then use your list to print a message to each person, inviting
them to dinner
'''

# guests = ['akmal', 'john', 'tony', 'bella', 'anna']
# print("########### printing guests by using index number ##########")
# print(f"Dear {guests[0].title()}, I am inviting you to dinner!")
# print(f"Dear {guests[1].title()}, I am inviting you to dinner!")
# print(f"Dear {guests[2].title()}, I am inviting you to dinner!")
#
# print()
#
# print("########### LOOPing makes it much simpler and easier to go through the entire list ##########")
# for guest in guests:
#     print(f"Dear {guest.title()}, I am inviting you to dinner!")
#     ## print(f"Hey {guestS}, welcome to the party!") >> 'guestS' is incorrect for looping
# print()
#
#
# '''
# ex.3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# '''
#
# '''
# - Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# '''
#
# ### Method 1.
# print(f"Dear guests! Unfortunately, {guests.pop(1).title()} can't make it tonight.")
# print(guests)
# print()
#
# ### Method 2.
# removed_guest = guests.pop(1)
# print(f"Dear guests! Unfortunately, {removed_guest.title()} can't make it tonight.")
# print(guests)
# print()
#
# print(f"Hopefully, all other guests are still coming to the dinner.")
# print()
#
# '''
# - Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# '''
# guests.append('max')
# print(f"Hey {guests[-1].title()}, please join us tonight for the dinner party!")
# print(guests)
# print()

'''
- Print a second set of invitation messages, one for each person who is still 
in your list.
'''
# for guest in guests:
#     print(f"Hey {guest.title()}, I'm looking forward to see you later at the dinner!")
#     ## print(f"Hey {guestS}, welcome to the party!") >> 'guestS' is incorrect for looping
# print()


'''
3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a 
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.
'''

# print(f"Hey folks, I actually found a bigger dinner table and am planning to add a couple more people to our party.")
# guests.insert(0, 'mike')
# print(guests)
# guests.insert(2, 'lucy')
# print(guests)
# guests.append('ted')
# print(guests)
# print()
#
# for guest in guests:
#     print(f"Hey {guest.title()}, I'm looking forward to see you later at the dinner!")
#     ## print(f"Hey {guestS}, welcome to the party!") >> 'guestS' is incorrect for looping
# print()


## ex.4-3. Counting to twenty
# nums = list(range(1, 21))
# for num in nums:
#     print(num)

## ex.4-4. One million for loop
nums = list(range(1, 1000000))
# for num in nums:
#     print(num)

## ex.4-5. Summing a million
# print(min(nums))
# print(max(nums))
# sum = 0
# for num in nums:
#     sum +=num
# print(sum)

## ex.4-6. Odd numbers
# odds = list(range(1,20, 2))
# for odd in odds:
#     pass
# print(odds)

## ex.4-7. Threes

