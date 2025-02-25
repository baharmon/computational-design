"""
Import White Sands raster
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2023, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# import modules
import pathlib
import os
import rasterio as rio
from rasterio.plot import show
from matplotlib import pyplot
from matplotlib import colors, cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import seaborn as sns

# set theme
sns.set_theme(
    style="white",
    font_scale=1.25
    )

# set path
datapath = pathlib.Path(__file__).parent.resolve()
dataset = os.path.join(
    datapath,
    'output.mean.tif'
    )

# read raster
elevation = rio.open(dataset)
array = elevation.read()

# plot raster
fig, ax = pyplot.subplots(figsize=(12, 12))
show(elevation, ax=ax, cmap='mako')

# create legend
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.1)
ax.ticklabel_format(useOffset=False, style='plain')
fig.colorbar(
    cm.ScalarMappable(
        norm=colors.Normalize(
            vmin=np.nanmin(array),
            vmax=np.nanmax(array)
            ),
        cmap='mako'),
    cax=cax,
    ax=ax
    )

# save as image
fig.set_size_inches(8.5, 8.5)
pyplot.tight_layout()
fig.savefig(
    'white-sands-dem.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.2
    )



