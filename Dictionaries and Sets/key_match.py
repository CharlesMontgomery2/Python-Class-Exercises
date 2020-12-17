############## Match key values in two dictionaries #####################################

print("Dogs") # Display the title of the code
d1 = {"Name": "Bruno", "Age": 5, "Breed": "Bulldog"} # create a dictionary
d2 = {"Name": "Bruno", "Age": 2, "Breed": "Pitbull"} #Create another dictionary

for (key, value) in set(d1.items()) & set(d2.items()): # Loop throught the set in each dictionary using the item function to return all
                                                       # dictionaries with the same keys and values.
    print("%s: %s is present in both d1 and d2" % (key, value)) # using %s to make the display code more readable is like
                                                                #  "{0}, {1}", (a, b) in C# language
# meaning the first %s (s stands for string), is represented as the key and the second %s is represented as value as shown after 
# the quotes inside its own perenthesis.