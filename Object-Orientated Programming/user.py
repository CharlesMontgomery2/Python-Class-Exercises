# 1)  Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user's information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

# Create 2 instances representing different users, and call both methods for each user.

####################################################################################################

class User(): # parent class
    """Make a user profile."""

    def __init__(self, first_name, last_name, username, email, phone_number, language): # provide perameters and prefix perameter using the init method
        """Initialize the user."""
        self.first_name = first_name.title() # use the prefix self that takes the value in the perameter for the following
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.language = language.title()

    def describe_user(self): # create a method using the prefix perameter
        """Display user's information."""
        print(f"\n{self.first_name} {self.last_name}") # display user info that will describe the user with the following info
        print("-----------------")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Phone Number: {self.phone_number}")
        print(f"  Language: {self.language}")

    def greet_user(self): # create a method using the prefix perameter
        """Display greeting"""
        welcome = f"\nWelcome back, {self.username}!" # create a variable for the message
        print(welcome) # Display the message

chucky = User("chucky", "lee ray", "Charles_Lee_Ray1", "chuckydoll@goodguy.com", "123-456-7890", "English") # must add all arguments
chucky.describe_user() # call the method
chucky.greet_user() # call the method

print("/////////////////////////////////////////////////////////////////") # make a new line and create seperation

andy = User("andy", "Barclay", "Andy_Barclay1", "andy.w.b@goodguy.com", "555-867-5309", "English")
andy.describe_user()
andy.greet_user()

print("/////////////////////////////////////////////////////////////////")

#########################################################################################################

# 2)  Write a program to show how multilevel inheritance works

#########################################################################################################

class Admin(): # parent class
    """Make a admin profile."""

    def __init__(self, first_name, last_name, email, phone_number): # same as the first parent class wiothout the welcome message
        """Initialize the admin."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.phone_number = phone_number

    def describe_user(self):
        """Display admin information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Phone Number: {self.phone_number}")

class sys_accounts(User,Admin): # child class derived from both parent classes
    """Make a child class."""

    def __init__(self, first_name, last_name, userid, username, email, phone_number, language): # creating a multiple inheritance is similar to creating a parent class
        """Initialize the admin.""" 
        self.userid = userid # instead of making all the prefix variables you can just make the ones that are not in any parent class used
        User.__init__(self, first_name, last_name, username, email, phone_number, language) # Here is where you inherant the parent class
        Admin.__init__(self, first_name, last_name, email, phone_number) # second parent class inherited
        print(f"\n{self.first_name} {self.last_name}") # display the info that will be described with the following info
        print("-----------------")
        print(f"  userid: {self.userid}")
        print(f"  Email: {self.email}")
        print(f"  Phone Number: {self.phone_number}")

sys_accounts("sam", "witwicky", "12345", "ladiesman217", "ladiesman217@transformers.com", "555-123-7855", "English") # must add all arguments if there are no defaults 

print("/////////////////////////////////////////////////////////////////")     