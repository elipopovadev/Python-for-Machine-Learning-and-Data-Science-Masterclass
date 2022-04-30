import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = x ** 4
a = np.arange(1, 5)
b = a * 100

fig, axes = plt.subplots(nrows=2, ncols=2, dpi=200, figsize=(5, 10))
axes[0][0].plot(a, b)
axes[1][0].plot(x, y)
axes[0][0].set_xlabel("X label")
axes[0][0].set_ylabel("Y label")
axes[0][0].set_title("Title 1")

fig.suptitle("Figure level", fontsize=16)

plt.tight_layout()  # to solve a problem with space
# fig.subplots_adjust(left =, right = , bottom = , top = , wspace = , hspace = ) # manual spacing
