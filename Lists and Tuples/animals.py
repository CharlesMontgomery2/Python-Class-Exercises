print("List of animals:") # displays the a statment for next line
animals = ["lion", "tiger", "bear", "zebra", "wolf", "elephant", "gerbil"] # Created a list of 7 animals
for animal in animals: # Loop through each animal in the variable list name animals
    print(animal) # prints each animal per line as it loops through the list
print("\nFirst three animals in the list are:") # displays the a statment for next line
for animal in animals[:3]: # Loops through the list to the 3rd index and will print only up to the 3rd not the 3rd index
    print(animal) # prints each animal per line as it loops through the list up to 3rd index
print("Oh My!")
print("\nThree animals from the middle of the list are:") # displays the a statment for next line
for animal in animals[2:5]: # Loops through the list starting at index 2 position 3 of the list and ends at index 5 after position 5
    print(animal) # displays the list of animals in postion 3, 4, and 5 which is index 2, 3, 4
print("\nLast three animals from the list are:") # displays the a statment for next line
for animal in animals[4:]: # Loops through the list starting at index 4 position 5 and will loop to the end of the list
    print(animal) 
