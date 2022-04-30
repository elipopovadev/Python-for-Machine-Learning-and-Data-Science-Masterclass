import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = x ** 4

fig = plt.figure(figsize=(10, 8), dpi=400)
axes1 = fig.add_axes([0, 0, 2, 2])
axes1.plot(x, y, label='X vs X', color='green', marker='o',
           markersize=10, markerfacecolor='red', linestyle='-.')

axes1.set_xlim(0, 8)
axes1.set_ylim(0, 8000)
axes1.set_xlabel("X label")
axes1.set_ylabel("Y label")
axes1.set_title("String title")
axes1.legend()


a = np.arange(1, 5)
b = a * 100

axes2 = fig.add_axes([0.3, 0.3, 0.6, 0.6])
axes2.plot(a, b, label='Label', color='blue')

axes2.set_xlim(1, 2)
axes2.set_ylim(0, 500)
axes2.set_xlabel("X label")
axes2.set_ylabel("Y label")
axes2.set_title("String title")
axes2.legend(loc='lower right')  # locate the label
# axes2.legend(loc = (1.1,0.5)) # outside
