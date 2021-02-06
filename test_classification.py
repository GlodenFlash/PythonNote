"""
    对新闻的类别进行判断
    用测试集进行验证，并给出测试集的准确率

    __author__ = 'Peter'
    __datetime__ = 2021.2.6

"""

import jieba
import os
import warnings

from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

warnings.filterwarnings('ignore')

def cut_word(file_path):
    '''
    对文本进行切词

    :param file_path:txt文件路径
    :return: 用空格分词的字符串
    '''
    text_with_space = ''
    text = open(file_path,'r',encoding = 'gb18030').read()
    text_cut = jieba.cut(text)
    for word in text_cut:
        text_with_space += word + " "

    return text_with_space


def loadfile(file_dir,target_list,labels_list):
    '''
    使用迭代对整个路径进行遍历，将数据按分类整合到列表中

    :param file_dir: 保存txt的目录
    '''
    file_list = os.listdir(file_dir)
    for a in file_list:
        a_name = file_dir + '/' + a
        if os.path.isdir(a_name):
            loadfile(a_name,target_list,labels_list)
        elif os.path.isfile(a_name):
            target_list.append(cut_word(a_name))
            if a_name.find('女性') != -1:
                labels_list.append('女性')
            if a_name.find('校园') != -1:
                labels_list.append('校园')
            if a_name.find('文学') != -1:
                labels_list.append('文学')
            if a_name.find('体育') != -1:
                labels_list.append('体育')


word_list_train = []
labels_list_train = []
word_list_test= []
labels_list_test = []

# # 第一步：加载停用词
stop_words = open('text classification/stop/stopword.txt', 'r', encoding='utf-8').read()
stop_words = stop_words.encode('utf-8').decode('utf-8-sig') # 列表头部\ufeff处理
stop_words = stop_words.split('\n') # 根据分隔符分隔

# # 第二部：对文档进行分词，将数据导入
loadfile('text classification/train/',word_list_train,labels_list_train)
loadfile('text classification/test/',word_list_test,labels_list_test)


# 第三步：计算分词权重
# 一个单词在50%的文档都出现过了，就不做分词统计
tf = TfidfVectorizer(stop_words = stop_words,max_df = 0.5)
train_features = tf.fit_transform(word_list_train)

# 上面用fir_transform，这里用transform
test_features = tf.transform(word_list_test)

# 第四步：生成朴素贝叶斯分类器
clf = MultinomialNB(alpha = 0.001).fit(train_features,labels_list_train)

# 第五步：使用生成的分类器做预测
predicted_labels = clf.predict(test_features)

print(metrics.accuracy_score(labels_list_test,predicted_labels))