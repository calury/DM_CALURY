# -*- coding: utf-8 -*-
"""
词云
@author: liuxh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import jieba
from scipy.misc import imread
from collections import defaultdict
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator

back_color = imread("test.jpg")  # 解析该图片
wc = WordCloud(background_color='white',
               max_words=1000,
               mask=back_color,
               max_font_size=100,
               stopwords=STOPWORDS.add('苟利国'),
               font_path="C:/Windows/Fonts/STFANGSO.ttf",
               random_state=42
               )

article = ""
with open("article1.txt", encoding="utf-8") as f:
    for line in f:
        article += line.strip()

words = jieba.cut(article)
words1 = []

for word in words:
    words1.append(word)
words2 = " ".join(words1)


wc.generate(words2)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('19th.png')





