#-*- coding:UTF-8 -*-
"""
"""
#@filename: basic1
#@author: liuxh
#@date: 2018/9/11 11:08

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# plt.rcParams['font.sas-serig']=['SimHei']    #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False     #用来正常显示负号


# labels = np.array(['a','b','c','d','e','f']) # 标签
# dataLenth = 6 # 数据长度
# data = np.array([1,4,3,6,4,8]) # 数据
#
#
# N = 20
# theta = np.linspace(0.0,2*np.pi,N,endpoint = False)
# radii = 10*np.random.rand(N)
# width = np.pi / 4*np.random.rand(N)
#
# ax = plt.subplot(111,projection = "polor")
# bars = ax.bar(theta,radii,width=width,bottom=0.0)
#
# for r,bar in zip(radii,bars):
#     bar.set_facecolor(plt.cm.viridis(r/10.0))
#     bar.set_alpha(0.5)
#
# plt.show


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()