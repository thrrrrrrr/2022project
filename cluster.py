import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster():
    #聚类 并统计高频词
     vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(items)
    true_k = 3
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

def save(model):
    #将结果保存


if __name__ == '__main__':

    #读取csv文件，获取所有的标题


    cluster()


