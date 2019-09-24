from utilities import manage_data, string_similarity, mycluster, silhouette


def test_pro():
    words = manage_data.load_csv(csv_name="terremoti.csv", column="Provincia")
    province = manage_data.load_province()
    matrix = manage_data.load_matrix("terremoti_provincia_wombo.npy")
    n_matching, total_words = string_similarity.perfect_matching(words, province)
    n_cluster_silhouette = silhouette.silhoutte_kmeans(matrix, n_matching, total_words, words)
    return n_cluster_silhouette
   # model, clusters, time = mycluster.kmeans(matrix, n_matching, words)
    #if not mycluster.check_clusters(clusters, province): return False
    #return mycluster.collapse(clusters, province)


def test_reg():
    words = manage_data.load_csv(csv_name="terremoti.csv", column="Regione")
    regione = manage_data.load_regions()
    matrix, time = string_similarity.wombo_combo(words)
    n_matching, total_words = string_similarity.perfect_matching(words, regione)
    n_cluster_silhouette = silhouette.silhoutte_kmeans(matrix, n_matching, total_words, words)
    return n_cluster_silhouette
