#!/usr/bin/env python

"""
Plot 1D matrix of random floats
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# set theme
sns.set_theme(style="darkgrid")

# generate random floats
rng = np.random.default_rng()
z = rng.random(1000)
print(z)

# plot random floats
ax = sns.displot(
    z,
    color='black',
    discrete=False,
    binwidth=0.01,
    binrange=(0, 1),
    height=2,
    aspect=5/1
    )
plt.savefig(
    'random-floats.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0
    )

