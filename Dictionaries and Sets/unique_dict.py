################################# Print all unique values in a dictionary #####################################

SampleData = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}] # create a list of dictionaries
unique_dict = set() # creating an empty set
for d in SampleData: # looping through the list
   for val in d.values(): # looping through the values in the list
      unique_dict.add(val) # adding the values to the list that have not been added

print("Unique Values: ", unique_dict) # displays the unique values
