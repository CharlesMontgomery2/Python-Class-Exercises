##############################Bubble Sort##########################################

nums = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]

x = 1 # this will be a variable for the index 1 of the tuple
nums_length = len(nums) # make a variable for the length of the list of tuple
for i in range(0, nums_length): # loop through each  of the tuples in the length of the list
    for j in range(0, nums_length-i-1): # nested loop to loop through the tuple
        if(nums[j][x] > nums[j + 1][x]): # condition statment for inside the tuple if the first value is greater than second value then swap
            temp = nums[j] # Set it in a temp variable for the position of the tuple to swap
            nums[j] = nums[j + 1] # swapping the next value
            nums[j + 1] = temp # swap conducted

print(nums)

############################Sort Function####################################

nums = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
nums.sort(key = lambda y: y[1]) # using the built in function to sort the second value of the tuple
print(nums)




