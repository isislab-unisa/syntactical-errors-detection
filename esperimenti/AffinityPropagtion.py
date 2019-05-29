import numpy as np
import sklearn.cluster as cluster
import distance
import pandas as pd

#data = pd.read_csv("impianti_sportivi.csv")

#per ciascuna parola, ne calcola la distanza di Levihstain con tutte le altre parole
#crea la matrice con una list compharison

words = "salerno alerno salern napoli firenze firenz napo napo salerno salerno salernooo napo napo2222".split(" ")
words = np.asarray(words)


lev_similarity = -1*np.array([[distance.levenshtein(w1, w2) for w1 in words] for w2 in words])


print(lev_similarity)

affprop = cluster.AffinityPropagation(affinity="precomputed", damping=0.85, preference=None)
affprop.fit(lev_similarity)

print("\n", affprop.labels_, "\n")

for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_== cluster_id)])
    cluster_str = ", ".join(cluster)
    print(" - *%s:* %s" % (exemplar, cluster_str))