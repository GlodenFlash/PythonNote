#encoding=utf-8
import numpy as np

'''
假设一个团队里有5名学员，成绩如下表所示。
1.用NumPy统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
2.总成绩排序，得出名次进行成绩输出。
'''


persontype = np.dtype({
    'names':['name','chinese','english','math'],
    'formats':['S32','i','i','i']
})

team = np.array([("zhangfei",100,65,30),
                 ("guanyu",76,95,98),
                 ("zhaoyun",93,79,56),
                 ("huangzhong",90,88,77),
                 ("dianwei",80,65,90),
                 ],dtype=persontype)

chinese = team[:]['chinese']
math = team[:]['math']
english = team[:]['english']
print('语文: AVG:',np.mean(chinese),' MIN:',np.min(chinese),' MAX:',np.max(chinese),' 标准差:',np.std(chinese),' 方差:',np.var(chinese))
print('英语: AVG:',np.mean(english),' MIN:',np.min(english),' MAX:',np.max(english),' 标准差:',np.std(english),' 方差:',np.var(english))
print('数学: AVG:',np.mean(math),' MIN:',np.min(math),' MAX:',np.max(math),' 标准差:',np.std(math),' 方差:',np.var(math))

# 排序方法1
print('按语文成绩排序：')
print(np.sort(team,order='chinese'))
print('按英语成绩排序：')
print(np.sort(team,order='english'))
print('按数学成绩排序：')
print(np.sort(team,order='math'))


# 排序方法2
print('按语文成绩排序：')
ranking_chinese = sorted(team,key=lambda x:x[1], reverse=False)
print(ranking_chinese)
print('按英语成绩排序：')
ranking_english = sorted(team,key=lambda x:x[2], reverse=False)
print(ranking_english)
print('按数学成绩排序：')
ranking_math = sorted(team,key=lambda x:x[3], reverse=False)
print(ranking_math)




# reverse = True 降序，False 升序
# lambda 匿名函数，对三科成绩之和进行排序
ranking = sorted(team,key=lambda x:x[1]+x[2]+x[3], reverse=False)
