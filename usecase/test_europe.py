from utilities import manage_data, mycluster, string_similarity
import pandas as pd
import numpy as np

def france_converter(comuni):

    data = pd.read_csv("europa/francia/comuni francia.csv", error_bad_lines=False, sep=";", encoding="UTF-8")
    new_comuni = np.unique(data["Column6"].to_numpy())
    new_comuni = dict(zip(comuni, new_comuni))
    return new_comuni


def francia_regioni_monumenti():

    data = pd.read_csv("europa/francia/regions-old.csv", error_bad_lines=False, sep=",", encoding="UTF-8")
    regions = np.unique(data["Regions"].to_numpy())
    regions = np.array([x.lower() if isinstance(x, str) else x for x in regions])
    regions = dict(zip(regions, regions))
    words = manage_data.load_csv(csv_name="europa/monumenti_francia.csv", column="région", nrows=2000)
    matrix, time = string_similarity.wombo_combo(words, regions)
    n_cluster, total = string_similarity.perfect_matching(words, regions)
    esiti = []
    for i in range(n_cluster, total+1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, regions), i))
    return esiti




#TODO convertire  a fine esecuzione nel formato accentato


def francia_comuni_contributi():
    data = pd.read_csv("europa/francia/comuni francia.csv", error_bad_lines=False, sep=";", encoding="UTF-8")
    comuni = np.unique(data["Column6"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/contributi-francia-2017.csv", column="inom", nrows=1000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)


    esiti = []
    for i in range(n_cluster, total+1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    new_comuni = france_converter(comuni)
    for i, word in enumerate(words):
        word = word.lower()
        if new_comuni.get(word) is not None:
            words[i] = new_comuni.get(word)

    return esiti


def francia_trains():
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
    comuni2 = np.unique(data["County"].to_numpy())
    comuni2 = np.array([x.lower() if isinstance(x, str) else x for x in comuni2])
    comuni2 = dict(zip(comuni2, comuni2))

    comuni.update(comuni2)

    words = manage_data.load_csv(csv_name="europa/milk producer uk.csv", column="Address5", nrows=1000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti

def spain_contratti():
    data = pd.read_csv("europa/spagna/comuni spagna.csv", error_bad_lines=False, sep=";", encoding="windows-1252")
    comuni = np.unique(data["Column2"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/Contratos_por_municipios_2006.csv", column="Provincia", nrows=2000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti

def eire_counties():
    data = pd.read_csv("europa/irlanda/province.csv", error_bad_lines=False, sep=";", encoding="windows-1252")
    comuni = np.unique(data["Name"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/districts irlanda.csv", column="PROVINCE", nrows=2000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti


def holland_accidents():
    data = pd.read_csv("europa/Olanda/olanda.csv", error_bad_lines=False, sep=";", encoding="windows-1252")
    comuni = np.unique(data["Provincie"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    comuni = dict(zip(comuni, comuni))
    words = manage_data.load_csv(csv_name="europa/incidenti olanda.csv", column="PROVINCIE", nrows=2000)
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))
    return esiti
