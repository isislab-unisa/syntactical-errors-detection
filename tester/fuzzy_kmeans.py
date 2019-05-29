from utilities import manage_data, string_similarity, mycluster


def test():
    words = manage_data.load_csv(csv_name="superiori.csv", column="TIPOLOGIA ISTITUTO")
    matrix, time = string_similarity.matrix_fuzzmatch(words=words)
    print("Tempo di esecuzione FUZZ MATCHING:", time)

    n_cluster = int(input('Inserire numero di cluser\n'))
    modello, clusters, time_clustering = mycluster.kmeans(matrix=matrix, n_cluster=n_cluster, words=words)
    # manage_data.save_matrix("nomematrice", matrix=matrix)
    print("\nTempo di esecuzione KMeans:", time_clustering, "\n\n\n")

    manage_data.show_clusters(cluster=clusters)

    print("\n\nTempo totale di esecuzione:", time+time_clustering)