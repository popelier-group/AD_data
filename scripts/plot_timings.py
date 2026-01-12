import os
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [4201.2, 22.7],  # C5
    [4528.8, 19.1],  # C7ax
    [4616.2, 21.6]   # C7eq
])

errors = np.array([
    [995.9, 1.8],  # C5
    [1312.6, 1.4],  # C7ax
    [1952.6, 6.5]   # C7eq
])

n_groups, n_bars = data.shape
x = np.arange(n_groups)
width = 0.8 / n_bars

plt.rcParams.update({
    "axes.linewidth": 1.2,
    "xtick.major.width": 1.2,
    "ytick.major.width": 1.2,
    "font.size": 12
})

methods  = ["GAUSSIAN", "FFLUX"]
colors   = ["green","blue"]
confs    = ["C5","C7ax","C7eq"]
fig, ax = plt.subplots(1,1, figsize=(4,4))

for i in range(n_bars):
    ax.bar(
        x + i * width,
        data[:, i],
        width=width,
        yerr=errors[:, i],
        capsize=4,
        #hatch='//',
        #color = colors[i],
        joinstyle="round",
        ecolor="black",
        #error_kw=dict(lw=2.2, capthick=1.2),
        zorder=3,
        #label=f"Bar {i+1}"
        label=methods[i]
    )

#for bars in ax.containers:
#    ax.bar_label(bars, fmt='%.1f', padding=3)

ax.set_xticks(x + width * (n_bars - 1) / 2)
ax.set_xticklabels([confs[i] for i in range(n_groups)])
ax.set_yscale('log')
ax.set_ylim(0,8000)
ax.set_ylabel("Optimization wall time (s)")
ax.legend(loc="center right", ncols=1)

plt.tight_layout()
plt.savefig("timings.png",dpi=300)
plt.show()
