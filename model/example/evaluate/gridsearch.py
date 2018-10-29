#-*- coding:UTF-8 -*-
"""网格搜索
"""
#@filename: gridsearch
#@author: liuxh
#@date: 2018/10/26 15:52

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

#前者适用，离散全量搜索
#后者适用，连续范围，搜索指定次数。
