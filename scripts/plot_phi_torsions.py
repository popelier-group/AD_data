import os
import numpy as np
import matplotlib.pyplot as plt

data = [
    [4.2, 3.8, 5.1, 5.0],   # Group 1
    [3.5, 4.1, 4.9, 5.0],   # Group 2
    [4.8, 3.9, 5.3, 5.0]    # Group 3
]

data = np.array(data)

n_groups, n_bars = data.shape
x = np.arange(n_groups)
width = 0.8 / n_bars   # total cluster width = 0.8

fig, ax = plt.subplots()

for i in range(n_bars):
    ax.bar(
        x + i * width,
        data[:, i],
        width=width,
        label=f"Bar {i+1}"
    )

ax.set_xticks(x + width * (n_bars - 1) / 2)
ax.set_xticklabels([f"Group {i+1}" for i in range(n_groups)])
ax.legend()

plt.show()
