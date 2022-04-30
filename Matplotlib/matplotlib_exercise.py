import matplotlib.pyplot as plt
import numpy as np


# Task 1: Import what you need from Matplotlib to plot out graphs
m = np.linspace(0, 10, 11)
c = 299792458
E = m * (c*c)

fig, axes = plt.subplots()
axes.plot(m, E, color="red", linewidth=4)
axes.set_xlabel('Mass in Grams')
axes.set_ylabel('Energy in Joules')
axes.set_title('E=mc^2')
axes.set_xlim(xmin=0, xmax=10)

# How to plot logarithmic scale on y axis
axes.set_yscale('log')

# How to set a grid on y axis
axes.yaxis.grid(True, which='minor')


# Task 2: Figure out how to plot both curves on the same Figure
labels = ['1 Mo', '3 Mo', '6 Mo', '1 Yr', '2 Yr',
          '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr']
july16_2007 = [4.75, 4.98, 5.08, 5.01, 4.89,
               4.89, 4.95, 4.99, 5.05, 5.21, 5.14]
july16_2020 = [0.12, 0.11, 0.13, 0.14, 0.16,
               0.17, 0.28, 0.46, 0.62, 1.09, 1.31]

fig = plt.figure(figsize=(5, 4), dpi=400)
axes1 = fig.add_axes([0, 0, 1, 1])

axes1.plot(labels, july16_2007, label='july16_2007')  # for first curve
axes1.set_ylim(ymin=0, ymax=5.5)

axes1.plot(labels, july16_2020,  label='july16_2020')  # for second curve
axes1.legend(loc=[1.05, 0.5])  # the legend is set out of the plot


# Task 3: Create two different plots
fig1, axes2 = plt.subplots(nrows=2, ncols=1, dpi=200, figsize=(10, 6))
axes2[0].plot(labels, july16_2007)
axes2[0].set_xlabel('july16_2007', loc='center')
axes2[1].plot(labels, july16_2020)
axes2[1].set_xlabel('july16_2020', loc='center')

fig1.tight_layout()


# Task 4: How to add two y axis and changed their color
x = labels
y1 = july16_2007
y2 = july16_2020

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y1, color='blue')
ax2.plot(x, y2, color='red')

ax1.set_ylabel('2007', color='blue')
ax2.set_ylabel('2020', color='red')

ax2.spines['left'].set_color('blue')
ax2.spines['right'].set_color('red')
