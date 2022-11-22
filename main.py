# draw a bar graph
import matplotlib.pyplot as plt
import numpy as np

# data to plot
mass = [2, 4, 6, 8, 10]
abundance = [79.2, 16.7, 0, 0, 4.2]

# create plot
fig, ax = plt.subplots()
index = np.arange(len(mass))
bar_width = 0.1

# set height of y-axis as 100
plt.ylim(0, 100)

# make image 1000 * 400
fig.set_size_inches(4, 6)

# add horizontal grid lines
ax.yaxis.grid(True)

# set vertical axis label frequency as 10
ax.set_yticks(np.arange(0, 100, 10))

rects1 = plt.bar(index, abundance, bar_width, color='#20D6C7')

plt.xlabel('Mass')
plt.ylabel('Abundance (%)')
plt.title('Relative Abundance of Isotopes')
plt.xticks(index + bar_width, mass)

# allign x-axis labels to the center
plt.tight_layout()

# save image as png
plt.savefig('isotopes.png')