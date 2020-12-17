# 4) Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

###################################################################################

user_msgs = ["Hello how are you?", "I am Ron Burgundy?"] # create a list with messages

def show_messages(msgs): # create a function with a perameter
    """Dislpay the text messages"""
    for msg in msgs: # loop through each message in the list
        text = f"{msg}" # create a variable for each message being looped
        print(text) # display the message in the list 

show_messages(user_msgs) # call the function and using the list variable name as the perameter