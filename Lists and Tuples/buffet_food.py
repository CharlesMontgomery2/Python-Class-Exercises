foods = ("chicken strips", "spaghetti", "pizza", "prime rib", "salad") # created  a tuple for foods in a buffet
for food in foods: # looped through the tuple for each of the foods
    print(food) # Displays each of the items per line in the tuple

print() # empty print statment will give a blank line and will allow an empty space between the 2 lists

try:            # I went witha try catchf error handling statement so that my code will continue to run after an error is displayed
    foods.append("icecream") # this throws the error because tuples can't be appended this way
finally: # finally will run the next code below
    foods = ("chicken strips", "spaghetti", "fried rice", "prime rib", "mashed potatoes") # changed the tuple
    for food in foods:# looped through the tuple for each of the foods
        print(food)# Displays each of the items per line in the tuple
