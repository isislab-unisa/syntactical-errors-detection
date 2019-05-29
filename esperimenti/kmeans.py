from sklearn.cluster import KMeans
import distance
import time
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz as fw


def similarity(word1, word2):
    """    if lev == -1:
            lev = distance.levenshtein(w1, w2)"""
    w1 = word1
    w2 = word2
    w1.lower()
    w2.lower()
    lev = distance.levenshtein(w1, w2)
    if(lev <3): return lev

    fuz1 = fw.ratio(w1, w2)
    fuz2 = fw.partial_ratio(w1, w2)
    fuz3 = fw.token_set_ratio(w1, w2)
    fuzAverage = (fuz1 + fuz2*1.2 + fuz3)/3
    fuzsum = (fuz2 + fuz3)/2

    if (fuzAverage >= 75) or (fuzsum>= 85):
        return 0

    if(fuzAverage<70) or (fuzsum < 65):
        lev = lev+10

    return lev

def kmeans_test():
    data = pd.read_csv("superiori.csv",  error_bad_lines=False, sep=";")

    words = data['TIPOLOGIA ISTITUTO'].to_numpy()

    for i, s in enumerate(words):
        if isinstance(s, float):
            words[i] = "Non specificato"

    start = time.time()
    lev_similarity = np.array([[similarity(w1, w2) for w1 in words] for w2 in words])
    print(lev_similarity)
    end = time.time()

    print("TIME OF EXECUTION:", end - start)

    n_cluster = int(input('Inserire numero di cluser\n'))

    kmean = KMeans(n_cluster)
    kmean.fit(lev_similarity)

    clusters = []

    for index in range(0, n_cluster):
        lista = []
        clusters.append(lista)

    for index in range(0, len(words)):
        clusters[kmean.labels_[index]].append(words[index])

    i = 1
    for cluster in clusters:
        print("Cluster ", i, cluster)
        i = i + 1

