# Recreating_Graphs_using_Matplotlib

# Bar Chart with Error

# 1. First, create a figure of width 10 and height 8.

from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

plt.figure(figsize=(10,8))

# 2. Plot the blue bars, which have the heights listed in past_years_averages.

plt.bar(range(len(past_years_averages)), past_years_averages)

# 3. Add error bars of cap size 5 and heights corresponding to the list error.

plt.bar(range(len(past_years_averages)), past_years_averages, yerr = error, capsize=5)

# 4. Set the axis to go from -0.5 to 6.5 on the x-axis and 70 to 95 on the y-axis.

plt.axis([-0.5, 6.5, 70, 95])

# 5. Create an ax object using plt.subplot(). Use ax to set the x-axis ticks to be range(len(years)) and the x-axis labels to be the years list.

ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)

# 6. Add the title "Final Exam Averages", x-axis label "Year", and y-axis label "Test average".

plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test average")

# 7. Save your figure to a file called my_bar_chart.png.

plt.savefig("my_bar_chart.png")

plt.show()

