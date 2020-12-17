##################### Generate a dictionary that contains a number (between 1 and n) in the form (x, x*x) ########################

n = 5 # given the number of items in the dictionary
dict = {} # create an empty dictionary

for x in range(1, n+1): # loop through each number in the range to the n variable and incrimenting it by 1

    dict[x] = x*x # using the math equation to add it to the value for the specific key that has been incrimented 

print(dict) # display the dictionary