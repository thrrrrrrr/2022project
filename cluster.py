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
    
    print("类中的高频关键词:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print("聚类%d:" % i)
        for ind in order_centroids[i, :10]:
            print (' %s' % terms[ind])
        print
    
    save(model)

def save(model):
    #将结果保存
    with open('cluster0.csv', 'a+', encoding='utf-8', newline='') as f0:
        with open('cluster1.csv', 'a+', encoding='utf-8', newline='') as f1:
            with open('cluster2.csv', 'a+', encoding='utf-8', newline='') as f2:
                writer0 = csv.writer(f0)
                writer1 = csv.writer(f1)
                writer2 = csv.writer(f2)
                for i,item in enumerate(items):
                    if(model.labels_[i] == 0):
                        writer0.writerow([str(item)])
                    if (model.labels_[i] == 1):
                        writer1.writerow([str(item)])
                    if (model.labels_[i] == 2):
                        writer2.writerow([str(item)])
                f0.close()
                f1.close()
                f2.close()


if __name__ == '__main__':

    #读取csv文件，获取所有的标题


    cluster()


