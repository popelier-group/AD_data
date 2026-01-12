import os
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [-167.7, -163.7],  # C5
    [64.4, 67.8],  # C7ax
    [-78.3, -81.7]   # C7eq
])

errors = np.array([
    [0.03, 1.26],  # C5
    [0.04, 0.77],  # C7ax
    [0.18, 1.11]   # C7eq
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
#ax.set_yscale('log')
#ax.set_ylim(0,7)
ax.set_ylabel("$\phi$ Dihedral angle ($\deg$)")
ax.legend(loc="lower right", ncols=1)

plt.tight_layout()
plt.savefig("phi_all_confs.png",dpi=300)
plt.show()
