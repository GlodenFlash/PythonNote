#coding=utf-8
import numpy as np

# 创建多维数组
# a = np.array([1,2,3])
# b = np.array([[1,2,3],[4,5,6],[7,9,8]])
# b[1,1] = 10
# print(a.shape)
# print(b.shape)
# print(a.dtype)
# print(b)


# Python中的结构体
# persontype = np.dtype({
#     'names':['name','age','chinese','math','english'],
#     'formats':['S32','i','i','i','f']
# })
# peoples = np.array([("Zhangfei",32,100,100,100),('LiuBei',24,90,80,99),('Guanyu',10,60,92,88)]
#                    ,dtype=persontype)
# ages = peoples[:]['age']
# print(ages)
# print(np.mean(ages))
# chinese = peoples[:]['chinese']
# print(chinese)
# print(np.mean(chinese))


# 算数运算
# x1 = np.arange(1,11,2)
# x2 = np.linspace(1,9,5)
# print(x1,x2)
# print(np.add(x1,x2))
# print(np.subtract(x1,x2))
# print(np.multiply(x1,x2))
# print(np.divide(x1,x2))
# print(np.power(x1,x2))
# print(np.remainder(x1,x2))
# print(np.mod(x1,x2))


# 统计函数
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.amin(a))
# print(np.amin(a,0))
# print(np.amin(a,1))
#
# print('-'*50)
# print(np.ptp(a))
# print(np.ptp(a,0))
# print(np.ptp(a,1))


# 排序
# c = np.array([[6,5,4,10],[100,2,3,1]])
# print(np.sort(c))
# print(np.sort(c,axis=None))
# print('-'*50)
# print(np.sort(c,axis=0))
# print(np.sort(c,axis=1))