from sklearn.cluster import AgglomerativeClustering as AC
import distance
import time
import numpy as np
from fuzzywuzzy import fuzz as fw
import pandas as pd
import tabulate

def similarity(word1, word2):
    """    if lev == -1:
            lev = distance.levenshtein(w1, w2)"""
    w1 = word1
    w2 = word2
    w1.lower()
    w2.lower()
    lev = distance.levenshtein(w1, w2)
    if lev <2:
        return lev

    fuz1 = fw.ratio(w1, w2)
    fuz2 = fw.partial_ratio(w1, w2)
    fuz3 = fw.token_set_ratio(w1, w2)

# il coefficiente del 'partial ratio' va modificato (se non addirittura ridotto) in caso di città
# perchè molte città, anche diverse, hanno sottostringhe e token simili o uguali
# ES: Nocera Superiore e Nocera Inferiore

    fuzAverage = (fuz1 + fuz2*1.2 + fuz3)/3
    fuzsum = (fuz2 + fuz3)/2

    if (fuzAverage >= 75) or (fuzsum>= 85):
        return 0

    if(fuzAverage<75) or (fuzsum < 65):
        lev = lev+10

    return lev


def show_clusters(cluster):
    cluster_set = {}
    for cl in cluster:
        if len(cl)==0:
            continue
        # data[cl[0]] = pd.Series(cl[1:])
        cluster_set[cl[0]] = cl
    data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in cluster_set.items()]))
    data = data.replace(np.nan, '', regex=True)

    print(tabulate.tabulate(data, headers="keys", tablefmt="orgtbl"))

def agglomerative():
    data = pd.read_csv("impianti_sportivi.csv", error_bad_lines=False, sep=";", nrows=400)

    words = data['Denominazione'].to_numpy()

    for i, s in enumerate(words):
        if isinstance(s, float):
            words[i] = "Non specificato"
            words[i] = words[i].lower().replace(" ", "")
        print(words[i])

    start = time.time()

    lev_similarity = np.array([[similarity(w1, w2) for w1 in words] for w2 in words])

    end = time.time()

    print("TIME OF EXECUTION:", end - start)

    n_cluster = int(input('Inserire numero di cluser\n'))

    cluster = AC(affinity="precomputed", n_clusters=n_cluster, linkage="complete")
    cluster.fit(lev_similarity)

#    print(cluster.labels_)

    print("\n\n CLUSTERS \n\n")

    clusters = []

    for index in range(0, n_cluster):
        lista = []
        clusters.append(lista)

    for index in range(0, len(words)):
        clusters[cluster.labels_[index]].append(words[index])

    show_clusters(clusters)

agglomerative()