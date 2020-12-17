# 2) Write a while loop that prompts users for their name. 
# When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

file = "guest_book.txt" # create a txt file

print("Enter 'quit' when you are finished.") # create a quit statement for user to end loop
while True:  # while statement is true will continue to loop
    name = input("\nWhat's your name? ") # loop this statement
    if name.lower() == 'quit': # if the user enters the word quit
        break # the loop will break out
    else:
        with open(file, 'a') as f: # else open file 
            f.write(name + "\n") # to write / add name in a new line
        print(f"Hi {name.title()}, you've been added to the guest book.") # Display a welcome guest message
file = open("guest_book.txt") # create an open file variable 
print("Names on the guest list are: \n", file.read()) # Display all guests in the list