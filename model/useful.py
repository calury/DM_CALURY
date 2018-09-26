#-*- coding:UTF-8 -*-
"""
"""
#@filename: useful
#@author: liuxh
#@date: 2018/9/10 17:17

import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['font.sas-serig']=['SimHei']    #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False     #用来正常显示负号


# 定义plot_feature_importances函数来画出条形图
def plot_feature_importances(feature_importances, title, feature_names):
    # 将重要性值标准化
    feature_importances = 100.0 * \
        (feature_importances / max(feature_importances))

    # 将得分从高到低排序
    # np.argsort()方法返回值是得分的从低到高的索引
    # np.filpud()方法作用是将得分的索引反转为从高到低
    index_sorted = np.flipud(np.argsort(feature_importances))
    # print(index_sorted)

    # 让X轴上的坐标居中显示
    pos = np.arange(0, index_sorted.shape[0]*3, 3) + 0.5
    # print(pos)

    # 画条形图
    plt.figure(figsize=(12, 6))
    plt.bar(pos, feature_importances[index_sorted], align='center', width=2)
    plt.xticks(pos, feature_names[index_sorted])
    plt.ylabel('Relative Importance')
    plt.title(title)
    plt.show()


plot_feature_importances(
    dt_regressor.feature_importances_,
    'Decision Tree regressor',
    housing_data.feature_names)
plot_feature_importances(
    ab_regressor.feature_importances_,
    'AdaBoost regressor',
    housing_data.feature_names)



#探索变量相关性
fig, ax = plt.subplots(figsize=(15,15))
sns.heatmap(dataframe[dataframe["Type"] == "h"].corr(), annot=True)



corr_matrix = np.corrcoef(housing_df[housing_colnames].values.T)
# to control figure size
fig, ax = plt.subplots()
fig.set_size_inches(11.7, 8.27)
sns.set(font_scale=1.5)
# plot heatmap of correlations
hm = sns.heatmap(corr_matrix, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=housing_colnames,
                 xticklabels=housing_colnames)
plt.show()



# tight_layout( )
for col in col_list:
        i += 1
        plt.subplot(6,2,i)
        plt.plot(housing_df[col], housing_df['MEDV'], marker='.', linestyle='none')
        plt.title(title % (col))
        plt.tight_layout()



#变量分析图
fig,ax = plt.subplots(2,2,figsize=(14,8))
ax1,ax2,ax3,ax4 = ax.flatten()
sns.distplot(train['ps_car_13'],bins=120,ax=ax1)
sns.boxplot(x='ps_car_13',y='target',data=train,ax=ax2)
sns.violinplot(x='ps_car_13',y='target',data=train,ax=ax3)
sns.pointplot(x='ps_car_13',y='target',data=train,ax=ax4)












