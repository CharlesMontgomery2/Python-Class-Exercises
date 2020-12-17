################################### PE 10 Part 2 #######################################

# 2) Plot first 10 square number sequence in a graph by calculating the values automatically. 
# Use scatter points to plot.
# Hint:
# To be plotted: 1, 4, 9, 16, 25, 36, 49, 64, 81, and 100

##########################################################################################

from matplotlib import pyplot as plt # import the functions

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # create the list of the first 10 numbers
squared_nums = [i ** 2 for i in nums] # squared the numbers by using a simple list comprehension
print(squared_nums)

plt.style.use('classic') # choose classic style
fig, ax = plt.subplots() # create the layout of the plotted points
ax.scatter(nums, squared_nums, s=50) # plotted dots must have the x and y axis and give it the size of dot

ax.set_title("First 10 Squared Numbers", fontsize=24) # set title and style
ax.set_xlabel("Values", fontsize=14) # set x axis and style
ax.set_ylabel("Squared Values", fontsize=14) # set y axis and style

ax.tick_params(axis='both', which='major', labelsize=14) # set the boarder and points giving the size
plt.show() # display the graph


