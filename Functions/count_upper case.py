# 5) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

########################################################################################################

def upper_lower_count(str): # create a function with a peramter
    dic = {"UPPER CASE": 0, "lower case": 0} # create a dictionary that has the uppercasse value set at 0 and lower case value set at 0
    for case in str:  # loop through each charatcter in the string
        if case.isupper(): # condition statement for if the character has an upper case
            dic["UPPER CASE"] +=1 # incroment the value of upper by one
        elif case.islower(): # condition statement for if the character has an lower case
            dic["lower case"] +=1 # incroment the value of lower case by one
        else:
            pass 
    print("UPPER CASE", dic["UPPER CASE"]) # print the upper case with the values it found
    print("lower case", dic["lower case"]) # print the lower case with the values it found

str = "The quick Brow Fox" # variable name for the string
upper_lower_count(str) # call the function and put in the variable name for the string in the perameter.
 