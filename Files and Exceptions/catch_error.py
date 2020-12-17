# 3) One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
# When you try to convert the input to an int, you'll get a ValueError. 
# Write a program that prompts for two numbers. 
# Add them together and print the result. 
# Catch the ValueError if either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text instead of a number.

while True: # create a while loop to remain true

    try:
        num1 = input("Enter a number: ") # Create a statement prompting the user to enter a number
        num1 = int(num1) # convert the string into an integer

        num2 = input("Enter another number: ") # Create a statement prompting the user to enter a number
        num2 = int(num2) # convert the string into an integer
        
    except ValueError: # catches the error
        print("Sorry, you must enter a number, please try again.") # display a statement and loop to try again
        pass
    else:
        sum = num1 + num2 # create a sum variable of both numbers
        print(f"The sum of {num1} and {num2} is {sum}.") # Display the statement
        break # break out of the loop