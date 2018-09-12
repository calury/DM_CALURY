#-*- coding:UTF-8 -*-
"""
"""
#@filename: map
#@author: liuxh
#@date: 2018/9/12 17:06
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#
# Map = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0)
# Map.drawmapboundary(fill_color = 'aqua')
# Map.fillcontinents(color = 'coral', lake_color = 'aqua')


map = Basemap(projection = 'aeqd', lon_0 = 10, lat_0 = 50)

map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'coral', lake_color = 'aqua')
map.drawcoastlines()

# Map.drawcoastlines()

plt.show()

plt.savefig('test.png')
