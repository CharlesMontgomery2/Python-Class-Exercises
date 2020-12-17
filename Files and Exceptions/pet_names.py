# 4) Make two files, cats.txt and dogs.txt. 
# Store at least three names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing.

filenames = ["cats.txt", "dogs.txt", "birds.txt"] # create a list of files

for filename in filenames: # for loop the files
    print(f"\nReading file: {filename}") # Display each of the files in the list
    try:
        with open(filename) as file: # open the file
            contents = file.read() # read all of the file
            print(contents) # Display the contents within the file
    except FileNotFoundError:
        print("Sorry, file not found.") # display a message if the file is not found from the list of files