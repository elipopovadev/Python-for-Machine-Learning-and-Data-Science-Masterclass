import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
y = 2 * x

plt.plot(x, y)
plt.title('String title')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xlim(1, 10)
plt.ylim(2, 20)
plt.show()
