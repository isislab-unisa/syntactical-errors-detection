from utilities import manage_data, mycluster, silhouette, string_similarity
import numpy as np

"""
Tutti i vari test sui singoli dataset e sulle singole colonne seguono sempre lo stesso schema
- Caricare il dizionario
- Caricare la colonna desiderata dal dataset
- calcolare/caricare la matrice delle distanze
- calcolare i limiti (inferiore e superiore) del numero di cluster
- (Opzionale) snellire il range tramite uso della silhouette
- Eseguire il mio algoritmo di verifica di ottimalità del numero di cluster
"""

def test_regioni_terremoti():
    regione = manage_data.load_regions()
    words = manage_data.load_csv(csv_name="terremoti.csv", column="Regione")
    matrix, time = string_similarity.wombo_combo(words)
    n_cluster, total= string_similarity.perfect_matching(words, regione)
    n_cluster_silhouette = silhouette.silhouette_agglomerative(matrix, n_cluster, total)
    esiti = []
    for i in n_cluster_silhouette:
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append(mycluster.check_clusters(clusters, regione))
    return esiti

def test_province_castelli():
    province = manage_data.load_province()
    words = manage_data.load_csv(csv_name="castelli-e-torri-in-campania.csv", column="Provincia")
    matrix, time = string_similarity.wombo_combo(words)
    n_cluster, total= string_similarity.perfect_matching(words, province)
    n_cluster_silhouette = silhouette.silhouette_agglomerative(matrix, n_cluster, total)
    esiti = []
    for i in n_cluster_silhouette:
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, province), i))
    return esiti
