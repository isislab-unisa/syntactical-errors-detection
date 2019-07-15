import pandas as pd
import tabulate
import numpy as np


def show_clusters(cluster):
    cluster_set = {}
    for cl in cluster:
        if len(cl)==0:
            continue
        # data[cl[0]] = pd.Series(cl[1:])
        cluster_set[cl[0]] = cl
    data = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in cluster_set.items()]))
    data = data.replace(np.nan, '', regex=True)

    print("\ndimensioni: ", data.shape, "\n\n", tabulate.tabulate(data, headers="keys", tablefmt="orgtbl"))


def load_matrix(filename: str):
    return np.load(filename)


def save_matrix(filename: str, matrix):
    np.save(filename, matrix)


def load_csv(csv_name, column, nrows=0, encoding="windows-1252"):

    if nrows == 0:
        data = pd.read_csv(csv_name, error_bad_lines=False, sep=";", encoding=encoding)
    else:
        data = pd.read_csv(csv_name, error_bad_lines=False, sep=";", nrows=nrows, encoding=encoding)

    words = data[column].to_numpy()

    for i, s in enumerate(words):
        if isinstance(s, float):
            words[i] = "Non specificato"
    return words


def load_regions(path="elenco comuni.csv"):
    data = pd.read_csv(path, error_bad_lines=False, sep=";", encoding="ISO-8859-1")
    regions = np.unique(data["Regione"].to_numpy())
    regions = np.array([x.lower() if isinstance(x, str) else x for x in regions])
    return dict(zip(regions, regions))


def load_province(path="elenco comuni.csv"):
    data = pd.read_csv(path, error_bad_lines=False, sep=";", encoding="ISO-8859-1")
    province = np.unique(data["Provincia"].to_numpy())
    province = np.array([x.lower() if isinstance(x, str) else x for x in province])
    return dict(zip(province, province))


def load_comuni(path="elenco comuni.csv"):
    data = pd.read_csv(path, error_bad_lines=False, sep=";", encoding="ISO-8859-1")
    comuni = np.unique(data["Comune"].to_numpy())
    comuni = np.array([x.lower() if isinstance(x, str) else x for x in comuni])
    return dict(zip(comuni, comuni))
