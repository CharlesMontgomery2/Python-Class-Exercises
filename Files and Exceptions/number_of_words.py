## 1) Write a Python program that takes a text file as input and returns the number of words of a given text file.

file = open("count.txt") #create a variable to open a file that was previously created
print(file.read()) # Display the file that reads all lines
count = open("count.txt") # create a count variable that is the file making a different variable to prevent confusion
words = count.read().split() # create a word variable that will count each word in the text by using the split() method
print("Number of words:", len(words)) # display the number of words by using the len function.
