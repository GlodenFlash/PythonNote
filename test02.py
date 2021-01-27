"""
    Pandas
"""

import pandas as pd
from pandas import Series ,DataFrame

# Series 序列的创建和用法
# x1 = Series([1,2,3,4])
# x2 = Series(data=[1,2,3,4],index=['a','b','c','d'])
# print(x1)
# print(x2)
#
# d = {'a':1,'b':2,'c':3,'d':4}
# x3 = Series(d)
# print(x3)


# DataFrame
# data = {'Chinese':[66,95,102,43,30],'English':[45,43,56,7,88],'Math':[44,77,89,87,99]}
# df1 = DataFrame(data)
# df2 = DataFrame(data,index=['Zhangfei','Guanyu','Zhaoyun','Huangzhong','Dianwei'],columns=['English','Math','Chinese'])
# print(df1)
# print(df2)


# 读取xlsx文件和写xlsx文件
# score = DataFrame(pd.read_excel('test02.xlsx'))
# score.to_excel('test02_write.xlsx')
# print(score)



data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])

# # 删除
# df2 = df2.drop(columns=['Math'])
# print(df2)
# df2 = df2.drop(index='ZhangFei')
# print(df2)
#
# # 重命名
# df2.rename(columns = {'Chinese':'YuWen','English':'YingYu'},inplace = True)
# print(df2)
#
# # 去掉重复行
# df2 = df2.drop_duplicates()
#
# # 查找空值
# print(df2.isnull())
# print(df2.isnull().any())


# # 使用apply函数对数据进行清洗
# df2['Chinese'] = df2['Chinese'].apply(lambda x:x*2)

# # 使用apply函数对数据进行清洗2
# def plus(df,n,m):
#     df['new1'] = (df[u'Chinese']+df[u'English'])*m
#     df['new2'] = (df[u'Chinese']+df[u'English'])*n
#     return df
# df3 = df2.apply(plus,axis=1,args=(2,3,))
# print(df3)

# # 统计函数
# print(df2.count())
# print(df2[u'Chinese'].max())
# print(df2['English'].describe())



# data_result1 = DataFrame({'name':['ZhangFei','GuanYu','a','b','c'],'data1':[0,1,2,3,4]})
# data_result2 = DataFrame({'name':['ZhangFei','GuanYu','A','B','C'],'data2':range(5)})
#
# # 数据表合并1:基于指定项连接  （基于name项连接，求交集）
# data_result3 = pd.merge(data_result1,data_result2,on = 'name')
#
# # 数据表合并2:inner内连接 （相同的键是name，基于name连接）
# data_result4 = pd.merge(data_result1,data_result2,how='inner')
#
# # 数据表合并3:left左连接 （基于第一个DataFrame,第二个作为补充）
# data_result5 = pd.merge(data_result1,data_result2,how='left')
#
# # 数据表合并4:right右连接 （基于第二个DataFrame,第一个作为补充）
# data_result6 = pd.merge(data_result1,data_result2,how='right')
#
# # 数据表合并5:out外连接 （两个DataFrame的并集）
# data_result7 = pd.merge(data_result1,data_result2,how='outer')


# 使用pandasql操作数据库
from pandasql import sqldf,load_meat,load_births
df10 = DataFrame({'name':['ZhangFei','GuanYu','A','B','C'],'data2':range(5)})
pysqldf = lambda sql:sqldf(sql,globals())
sql = "select * from df10 where name = 'ZhangFei'"
print(pysqldf(sql))