# 1) Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
# that prints these two pieces of information, and a method called open_restaurant() 
# that prints a message indicating that the restaurant is open.

# 2) Update the above program by creating three different instances from the class, 
# and call describe_restaurant() for each instance.

class Restaurant(): # Define the Class
    """Class for a restaurant.""" # These will help in discribing what is going on without using comments

    def __init__(self, name, cuisine_type): # provide the two perameters and one prefix perameter using the init method  
        """Initialize name and cuisine_type."""
        self.name = name.title() # use the prefix self that takes the value in the perameter 
        self.cuisine_type = cuisine_type # and assign it a variable along with title casing.

    def describe_restaurant(self): # create a method using the prefix perameter
        """Display description of the restaurant."""
        msg = f"{self.name} serves the most amazing {self.cuisine_type}." # create a variable for the message that will describe the restaurant
        print(f"{msg}") # Display the message

    def open_restaurant(self): # Create a method using the prefix perameter
        """Display a message to the restaurant is open."""
        msg = f"{self.name} is open." # create a variable for the message
        print(f"{msg}") # Display the message

big_bobs = Restaurant("Big Bob's BBQ Babyback Ribs", "BBQ Ribs") # create an instance in the restaurant class
print(big_bobs.name) # Display the restaurant name
print(big_bobs.cuisine_type) # Display the restaurant cusine_type

big_bobs.describe_restaurant() # call the method within the class
big_bobs.open_restaurant() # call the method within the class

print()
burgatory = Restaurant("burgatory", "Cheese Burgers") # create an instance in the restaurant class
print(burgatory.name) # Display the restaurant name
print(burgatory.cuisine_type) # Display the restaurant cusine_type

burgatory.describe_restaurant() # call the method within the class
burgatory.open_restaurant() # call the method within the class

print()
garden_of_eatin = Restaurant("the garden of eat'n", "Salads") # create an instance in the restaurant class
print(garden_of_eatin.name) # Display the restaurant name
print(garden_of_eatin.cuisine_type) # Display the restaurant cusine_type

garden_of_eatin.describe_restaurant() # call the method within the class
garden_of_eatin.open_restaurant() # call the method within the class
