from utilities import manage_data, string_similarity, mycluster


def test():
    words = manage_data.load_csv(csv_name="castelli-e-torri-in-campania.csv", column="Provincia")
    matrix, time = string_similarity.matrix_lev(words=words)
    print("Tempo di esecuzione LEVENSTHEIN DISTANCE:", time)

    n_cluster = int(input('Inserire numero di cluser\n'))
    modello, clusters, time_clustering = mycluster.agglomerative_propagation(matrix=matrix,
                                                                            n_cluster=n_cluster, words=words)
    # manage_data.save_matrix("nomematrice", matrix=matrix)
    print("\nTempo di esecuzione AGGLOMERATIVE:", time_clustering, "\n\n\n")

    manage_data.show_clusters(cluster=clusters)

    print("\n\nTempo totale di esecuzione:", time+time_clustering)