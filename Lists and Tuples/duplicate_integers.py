list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] # Create the list

list.sort() # sort the list
output_list = [] # make an empty list for the duplicates to be put in

for i in range(len(list)-1): # Looping through the length of the list
    if list[i] == list[i+1]: # condition statment to check if index is equal to the next index in the sorted list
        if list[i] not in output_list: # and if true and not already in the list using anested if statement
            output_list.append(list[i]) # Then add to the new list
            
print(output_list) # display the new list