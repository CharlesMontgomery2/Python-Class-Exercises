####################### Combine two dictionary adding values for common keys ################################
## This algorythm is the only one that I could get that will display the correct output that was disctribed in the question

from collections import Counter # using the import internal function Counter in Python to add the common keys together
d1 = {'a': 100, 'b': 200, 'c':300} # dictionary 1
d2 = {'a': 300, 'b': 200, 'd':400} # dictionary 2
d = Counter(d1) + Counter(d2) # creating a variable that has the sum of the counter of each dictionary
print(d) # displays the results



######################################################
## this method is used without using the internal imported Python function but was not the correct output that was dictated in the question
## I could have made a function that was named Counter but may have took a long time to make.
d1 = {'a': 100, 'b': 200, 'c':300} # dictionary 1
d2 = {'a': 300, 'b': 200, 'd':400} # dictionary 2
for key in d2: # Loop through the keys in dictionary 2
    if key in d1: # creating a conditional statement for keys in dictionary 1
        d2[key] = d2[key] + d1[key] # if key from d2 is in d1 then it will add the key values together
    else:
        d1.update(d2)  # will update d1 with the results of d1 added to d2    
print(d1) # displaying d1


