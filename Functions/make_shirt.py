# 1) Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, msg): # create a function with the two perameters
    """Display shirt size and message."""
    print(f"\nShirt size is a {size.title()} and the shirt will say {msg}.") # what the function will display when called

make_shirt("medium", "'Hello Python'") # providing the perameters using positional arguments

make_shirt(msg = "'Hello World'", size = "small") # providing the perameters using keyword arguments

############################################################################


# 2) Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt_modified(size = "Large", msg = "'I love Python'"): # create a function with the two default perameters
    """Display shirt size and message."""
    print(f"\nShirt size is a {size.title()} and the shirt will say {msg}.") # what the function will display when called

make_shirt_modified() # since there are no perameters then this will display the default perameters
make_shirt_modified("medium") # This is one perameter that displays the default message