'''
任务详情

现有 iris 数据集中的花萼长度数据一份，已保存为 csv 格式，请按下方要求先对数据进行清洗整理，再进行相关统计分析。

利用 numpy 读取 csv 文件数据，命名为 iris，并以 ndarry 形式展示出来（阅读参考文章①）

找出原数据中最小值和最大值出现的位置（任务提示：numpy 中 argmax 和 argmin 函数可以定位到最大值和最小值的索引位置。阅读参考文章②）

利用 numpy 找出花萼最小值与最大值（阅读参考文章②）

将 iris 原数据进行从小到大排序，并以 ndarray 形式展示出来（任务提示：排序函数为 sort。阅读参考文章③）

去除该组数据中的重复值（任务提示：去重函数为 np.unique()。阅读参考文章④）

请利用 numpy 计算出该组花萼的平均长度（任务提示：平均函数为 np.mean()。阅读参考文章⑤）

用numpy计算出该组数据的标准差和方差（任务提示：标准差可以衡量数据的波动性。阅读参考文章⑥）

求出所有花瓣累积总和（阅读参考文章⑦）

对已排序的 iris 数据进行累积求和运算（任务提示：累积求和与求和有区别，累积求和是前几个数相加成新的元素从而组成新的数组。阅读参考文章⑧⑨）

统计花萼长度比平均值 5.84 高的有多少（任务提示：例如 (arr>1).sum() 可统计大于1的个数）
'''
#1.
import numpy as np
with open("iris.csv",'r',encoding='utf-8') as f:
    iris=np.loadtxt(f,delimiter=',')
    print(iris)

#2.    
print('\n最大元素出现的位置为：',iris.argmax())
print('最小元素出现的位置为：',iris.argmin())

#3.
print("\n最小值为：",iris.min())
print("最大值为：",iris.max())

#4.
iris.sort()
print("\n排序后为：\n",iris)

#5.
print("\n去重后为：\n",np.unique(iris))

#6.
print("\n平均长度为：\n",np.mean(iris))

#7.
print("\n标准差为：",iris.std())
print("方差为：",iris.var())

#8.
print("\n所有花瓣累积总和为：",iris.sum())

#9.
print("\n累积求和的数组为：\n",iris.cumsum())

#10.
print("\n统计比平均值高的有",(iris>5.84).sum(),"个")