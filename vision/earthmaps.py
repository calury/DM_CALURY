#-*- coding:UTF-8 -*-
"""
"""
#@filename: maps
#@author: liuxh
#@date: 2018/9/12 17:21
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)

plt.show()