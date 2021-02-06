'''
    对文档中的四句话单词进行分析
'''

from sklearn.feature_extraction.text import TfidfVectorizer
# 创建TfidfVectorizer类
tfidf_vec = TfidfVectorizer()

documents = [ 'this is the bayes document',
              'this is the second second document',
              'and the third one',
              'is this the document']
# 对文档进行拟合,得到tfidf矩阵
tfidf_matrix = tfidf_vec.fit_transform(documents)
# print(tfidf_matrix)

# 输出文档中所有不重复的词
print('不重复的词：',tfidf_vec.get_feature_names())

# 输出每一个单对应的id
print("每个单词对应的ID:",tfidf_vec.vocabulary_)

# 输出每个单词在每个文档中的TF-IDF值
print('每个单词的tfidf值:',tfidf_matrix.toarray())
