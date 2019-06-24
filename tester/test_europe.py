from utilities import manage_data, mycluster, string_similarity
import pandas as pd
import numpy as np


def francia_comuni_musei():

    data = pd.read_csv("europa/francia/comuni francia.csv", error_bad_lines=False, sep=";", encoding="UTF-8")
    comuni = np.unique(data["Column6"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/musei_francia.csv", column="Commune", nrows=1000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total+1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti


def francia_comuni_contributi():
    data = pd.read_csv("europa/francia/comuni francia.csv", error_bad_lines=False, sep=";", encoding="UTF-8")
    comuni = np.unique(data["Column4"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/contributi-francia-2017.csv", column="inom", nrows=1000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total+1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti


def francia_treni():
    data = pd.read_csv("europa/francia/comuni francia.csv", error_bad_lines=False, sep=";", encoding="UTF-8")
    comuni = np.unique(data["Column6"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/treni francia.csv", column="COMMUNE_COMPTEUR", nrows=1000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total+1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti


# più risultati ottimi per mix comuni / contee e per più città in una cella
# in questi casi considerare il numero di cluster più alto
def eng_school():
    data = pd.read_csv("europa/uk/comuni UK.csv", error_bad_lines=False, sep=",", encoding="UTF-8")
    comuni = np.unique(data["Town"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/uk1.csv", column="Column8", nrows=1000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti

