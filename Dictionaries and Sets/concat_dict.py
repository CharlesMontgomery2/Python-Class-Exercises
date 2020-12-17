################### Concatinating dictionaries together ##############################

dic1 = {1:10, 2:20} # dictionaries that needs to be concatinated (dic1, dic2, dic3)
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = {} # create an empty dictionary
for d in (dic1, dic2, dic3): # loop through each dictionary
    dic4.update(d) # and using the update function to add each item of each dictionary to the new dictionary
print (dic4) # Display the new dictionary