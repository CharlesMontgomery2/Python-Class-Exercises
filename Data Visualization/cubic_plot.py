################################## PE 10 ###################################################

# 1) A number raised to the third power is a cube.
# Plot the first five cubic numbers by calculating the values automatically.
# Use can use either line or scatter points to plot. 
# Hint:
# To be plotted: 1, 8, 27, 64, 125

#############################################################################################

from matplotlib import pyplot as plt # import the functions

nums = [0, 1, 2, 3, 4, 5] # create a list of the first five integers plus the 0 to show the table correctly
cubed_nums = [i**3 for i in nums] # cube the numbers by using a simple list comprehension
print(cubed_nums) # print the cubed numbers to make sure the numbers line up with the graph

plt.style.use('classic') # choose classic style 
fig, ax = plt.subplots() # create the layout of the plotted points

ax.plot(cubed_nums, linewidth=5) # use the specified list for the graph and line width

ax.set_title("First Five Cubic Numbers", fontsize=24) # set title and style
ax.set_xlabel("values", fontsize=14) # set x axis and style
ax.set_ylabel("Cubic Values", fontsize=14) # set y axis and style

ax.tick_params(axis='both', labelsize=14) # set the boarder and points giving the size 
plt.show() # display the graph
