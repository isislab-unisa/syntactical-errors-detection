from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering as AC
import time as t
import numpy as np

from utilities import string_similarity


def kmeans(matrix, n_cluster: int, words: list):
    kmean = KMeans(n_cluster, max_iter=1000, algorithm="full")

    start = t.time()

    kmean.fit(matrix)

    clusters = []

    for index in range(0, n_cluster):
        lista = []
        clusters.append(lista)

    for index in range(0, len(words)):
        clusters[kmean.labels_[index]].append(words[index])

    end = t.time()

    return kmean, clusters, end-start


def agglomerative_propagation(matrix, n_cluster: int, words: list):

    start = t.time()
    affinity = AC(affinity="precomputed", n_clusters=n_cluster, linkage="complete")
    affinity.fit(matrix)

    clusters = []

    for index in range(0, n_cluster):
        lista = []
        clusters.append(lista)

    for index in range(0, len(words)):
        clusters[affinity.labels_[index]].append(words[index])

    end = t.time()

    return affinity, clusters, end-start


def find_samples(column: list, uniques, dictionary):
    maxcount=0
    maxw = ""
    column = [x.lower() for x in column]

    for w in uniques:
        w = w.lower()
        if w in dictionary:
            return w
        count = column.count(w)
        if count > maxcount:
            maxcount = count
            maxw = w
    return maxw


def collapse(clusters, dictionary):
    samples = []
    dictionary = [x.lower() for x in dictionary]
    for i, group in enumerate(clusters):
        samples.append(find_samples(group, np.unique(group), dictionary))

    for i, w1 in enumerate(samples):
        for j, w2 in enumerate(samples):
            if i == j: continue
            w1 = w1.lower()
            w2 = w2.lower()
            if w1 in dictionary and w2 in dictionary and w1 != w2:
                continue
            if string_similarity.single_wombocombo(w1, w2) == 0:
                print(w1, " e ", w2, " simili ma in cluster diversi")
                return False


#  samples.pop(j)
#  clusters[i].append(clusters[j])
# clusters[j].pop(j)

    return True


# controlla la coesistenza in un cluster di più elementi che hanno perfect matching nel dizionario
# in definitiva verifica la necessità o meno di avere altre colonne
def split(clusters, dictionary):
    flag = True
    present = ""
    dictionary = [x.lower() for x in dictionary]

    for i, group in enumerate(clusters):
         g = np.unique(group)
         for w in g:
             w = w.lower()
             if w in dictionary:
                if flag:
                    flag = False
                    present = w
                else:
                    print(w, "e", present, "nello stesso cluster!!!")
                    return False
         flag = True



    return flag


def check_clusters(clusters, dictionary):
    if not split(clusters, dictionary):
        return False, "Aumentare il n° di cluster"

    if not collapse(clusters, dictionary):
        return False, "Diminuire il n° di cluster"

    return True, "Numero esatto di cluster"
