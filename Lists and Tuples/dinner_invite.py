invite = ["Ron Burgundy", "Chazz Michael Michaels", "Ricky Bobby"] # Created a list of three names
print(invite) # display the list

print(f"\n{invite[0]}, {invite[1]} and {invite[2]},  you are invited to dinner.") # inviting the three guests in the list

print(f"\n{invite[2]},  is unable to make it to dinner.") # displaying a guest can not make it

del invite[2] # Deleting the guest from the invite list
print(invite) # displaying the new list
invite.insert(0, "Mugatu") # inserting a new invited guest to index 0

print(f"\n{invite[0]},  you are invited to dinner.") # displaying invite to new guest
print(invite) # displaying the new list

print(f"\n More invites.") # displaying more will be invited to list (added to list)
invite.insert(0, "Frank the Tank") # inserting new guest to index 0
invite.insert(2, "Buddy the Elf") # inserting new guest to index 2 position 3 of the list
invite.append("Gator") # using append to add a new guest to end of the list

print(f"\n{invite[0]}, {invite[2]} and {invite[-1]},  you are invited to dinner.") # displaying new invites
print(invite) # displaying new list

print("\nOnly two people can be invited.") # displaying that only two can be invited

uninvite = invite.pop() # created a variable for the popped out guest which pops the last item from the list
print(f"Sorry, {uninvite} you are uninvited to dinner.") # display that the guest has been removed

uninvite = invite.pop() # created a variable for the popped out guest which pops the last item from the list
print(f"Sorry, {uninvite} you are uninvited to dinner.") # display that the guest has been removed

uninvite = invite.pop() # created a variable for the popped out guest which pops the last item from the list
print(f"Sorry, {uninvite} you are uninvited to dinner.") # display that the guest has been removed

uninvite = invite.pop() # created a variable for the popped out guest which pops the last item from the list
print(f"Sorry, {uninvite} you are uninvited to dinner.") # display that the guest has been removed

print(f"\n{invite[:]},  you are invited to dinner.") # displaying new list with the two invited guests which are the first two items in the list
