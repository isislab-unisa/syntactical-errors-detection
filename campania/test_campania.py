from utilities import manage_data, mycluster, string_similarity
import pandas as pd
import numpy as np
import time as t
comuni = manage_data.load_comuni()



def allievi_ritirati():
    end = t.time()
    words = manage_data.load_csv(csv_name="campania/2017-Allievi-Ritirati.csv", column="ComuneResidenza")
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti


def agriturismi_napoli():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Agriturismi-Napoli.csv", column="COMUNE AZIENDA")
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def albo_coop_sociali():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Albo-Regionale-Cooperative-Sociali.csv", column="ComuneSedeLegale", encoding="UTF-8")
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def associazioni_giovanili():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Associazioni-Giovanili.csv", column="Città", encoding="UTF-8")
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def elenco_comunita_minori():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Elenco-Comunita-Minori.csv", column="Comune", encoding="UTF-8")
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def elenco_parafarmacie():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Elenco-Parafarmacie.csv", column="DESCRIZIONECOMUNE", encoding="UTF-8")
    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def elenco_enti_spettacolo():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Elenco_enti_Spettacolo_e_Cinema.csv", column="SedeLegale", encoding="UTF-8")
    for i, w in enumerate(words):
        words[i] = manage_data.rimuovi_provincia(w)

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def fattorie_didattiche():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Fattorie-didattiche.csv", column="Sede operativa", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def immobili():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Immobili-demaniali.csv", column="Comune")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)
    return esiti

def dataset1():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/dataset01.csv", column="Città")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti


def dataset2():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/dataset02.csv", column="Comune")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def dataset3():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/dataset03.csv", column="Comune_ubicazione_studio_medico_struttura", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def indirizzi():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Indirizzi-Regione-Campania.csv", column="Comune", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def istituti():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Istituti-Scolastici-Superiori.csv", column="COMUNE", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti



def medicina_generale():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Medici-Medicina-Generale.csv", column="ComuneStudioMedico_Struttura", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def patrimonio():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Patrimonio-indisponibile.csv", column="Comune", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def pediatri():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Pediatri-Libera-Scelta.csv", column="ComuneStudioMedico_Struttura", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def registro_volontariato():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Registro-Volontariato.csv", column="Comune", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

def territorio():
    end = t.time()

    words = manage_data.load_csv(csv_name="campania/Territorio-Regione-Campania.csv", column="Comune", encoding="UTF-8")

    matrix, time = string_similarity.wombo_combo(words, comuni)
    n_cluster, total = string_similarity.perfect_matching(words, comuni)
    esiti = []
    for i in range(n_cluster, total + 1):
        model, clusters, time = mycluster.agglomerative_propagation(matrix, i, words)
        esiti.append((mycluster.check_clusters(clusters, comuni), i))

    end = t.time() - end
    print("Tempo 1: ", end)

    return esiti

