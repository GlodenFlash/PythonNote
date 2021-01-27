#coding=utf-8
import pandas as pd
from pandas import DataFrame

data = {'Chinese':[66,95,95,90,80,80],'English':[65,85,92,88,90,90],'Math':[None,98,96,77,90,90]}
df2 = DataFrame(data,index=['ZhangFei','GuanYu','ZhaoYun','HuangZhong','DianWei','DianWei'],columns = ['Chinese','English','Math'])

# 去掉重复行
df2 = df2.drop_duplicates()

# 数据清洗
def sum_of_three(df):
    df['sum'] = df['Chinese']+df['English']+df['Math']
    return df

df2 = df2.apply(sum_of_three,axis = 1)
print(df2)

# 使用数学的平均值补全张飞的成绩
df2['Math'].fillna(df2['Math'].mean(),inplace=True)
df2 = df2.apply(sum_of_three,axis = 1)
print(df2)