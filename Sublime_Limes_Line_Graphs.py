# Sublime Limes' Line Graphs Project 

# In this project, I will act as a data analyst for an online lime retailer called Sublime Limes. People all over the world can use this product to get the freshest, best-quality limes delivered to their door. 
# One of the product managers at Sublime Limes would like to gain insight into the customers and their sales habits. Using Matplotlib, I’ll create some different line graphs (or maybe, lime graphs) to communicate this information effectively.

# 1. Create a figure of width 12 and height 8.

from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# create your figure here

plt.figure(figsize=(12,8))

# 2. I will be making two charts in one figure, laid out side-by-side. In other words, the figure will have one row and two columns.

# Write the command to create the left subplot (the one that would correspond to the plot with a star in our example figure), and I will save this subplot in a variable called ax1.

ax1 = plt.subplot(1,2,1)

# 3. Write the command to create the right subplot (the one that would correspond to the plot with a square in our example figure).

# Save this subplot in a variable called ax2.

ax2 = plt.subplot(1,2,2)

#Page visits over time

# 4. In the left subplot, we are going to plot the total page visits over the past year as a line.

# First, let’s create the list of x-values, which is range(len(months)). Store this in a variable called x_values.

# Make sure this happens after the line where you created ax1, but before the line where you’ve created ax2, so that the plot goes in the subplot on the left.

plt.figure(figsize=(12,8))
ax1 = plt.subplot(1,2,1)
x_values = range(len(months))

# 5. Plot the total page visits against these x_values as a line.Give the line markers that will help show each month as a distinct value.

plt.plot(x_values, visits_per_month, marker='o')

# 6. Label the x-axis and y-axis with descriptive titles of what they measure.

plt.xlabel("Months")
plt.ylabel("Page visits")

# 7. Set the x-axis ticks to be the x_values.

ax1.set_xticks(x_values)

# 8. Label the x-axis tick labels to be the names stored in the months list.

ax1.set_xticklabels(months)

# Plotting multiple lime species

# 9. In the subplot on the right, we are going to plot three lines on the same set of axes. The x-values for all three lines will correspond to the months, so we can use the list of x_values we used for the last plot.

# On one plot, create the three lines:

# number of key limes sold vs x_values
# number of Persian limes sold vs x_values
# number of blood limes sold vs x_values

ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, marker='o')
plt.plot(x_values, persian_limes_per_month,marker='o')
plt.plot(x_values, blood_limes_per_month, marker='o')

# 10. Give each line a specific color of your choosing.

ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, color= 'lime', marker='o')
plt.plot(x_values, persian_limes_per_month,color='orange', marker='o')
plt.plot(x_values, blood_limes_per_month, color='red', marker='o')

# 11. Add a legend to differentiate the lines, labeling each lime species.

plt.legend(['Key', 'Persian', 'Blood'])

# 12. Set the x-axis ticks to be the x_values, and the tick labels to be the months list.

plt.xlabel("Month")
plt.ylabel("Limes sold")
ax2.set_yticks(x_values)
ax2.set_yticklabels(months)

# Labeling and saving

# 13. Add a title to each of the two plots you’ve created, and adjust the margins to make the text you’ve added look better.

# Under ax1 object for our first graph:
plt.title('Page Visits per Month')

# Under ax1 object for our first graph:
plt.title('Lime Sales per Month')

# 14. Now, save your figure as a png with a descriptive file name.

plt.subplot_adjust(top=0.95, wspace=0.35)
plt.savefig("sublime_limes_line_graph.png")

# All code together:

import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12,8))
ax1 = plt.subplot(1,2,1)
x_values = range(len(months))
plt.plot(x_values, visits_per_month, marker='o')
plt.xlabel("Month")
plt.ylabel("Visitors")
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)
plt.title('Page visits per Month')

ax2 = plt.subplot(1,2,2)
plt.plot(x_values, key_limes_per_month, color= 'lime', marker='o')
plt.plot(x_values, persian_limes_per_month,color='orange', marker='o')
plt.plot(x_values, blood_limes_per_month, color='red', marker='o')
plt.legend(['Key Limes', 'Persian Limes', 'Blood Limes'])
plt.xlabel("Month")
plt.ylabel("Limes sold")
ax2.set_yticks(x_values)
ax2.set_yticklabels(months)
plt.title('Lime sales per month')

plt.show()

plt.subplot_adjust(top=0.95, wspace=0.35)
plt.savefig("sublime_limes_line_graph.png")

# In this project I used Matplotlib, a Python library which helps data rpofessinal to render any kind of data, to create two line graphs from a given data set. Not only did I render the data, but 
# I used effective labels, legents and formating to maximise readability and presentation.