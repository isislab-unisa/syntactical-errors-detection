from fuzzywuzzy import fuzz as fw
import pyxdameraulevenshtein as lev
import numpy as np
import time as t

_PESO_PARTIAL_RATIO = 1.1
_HIGH_LEV_DIFFERENCE = 20
_LOW_LEV_DIFFERENCE = 5
_HIGH_AVERAGE_FUZZY = 85
_LOW_AVERAGE_FUZZY = 75
_HIGH_SUBSTRING_FUZZY = 90
_LOW_SUBSTRING_FUZZY = 85


def single_fuzzmatch(w1: str, w2: str):

    fuz1 = fw.ratio(w1, w2)
    fuz2 = fw.partial_ratio(w1, w2)
    fuz3 = fw.token_set_ratio(w1, w2)

# il coefficiente del 'partial ratio' va modificato (se non addirittura ridotto) in caso di città
# perchè molte città, anche diverse, hanno sottostringhe e token simili o uguali
# ES: Nocera Superiore e Nocera Inferiore

    fuzAverage = (fuz1 + fuz2*_PESO_PARTIAL_RATIO + fuz3)//3
    return -fuzAverage


def single_lev(w1: str, w2: str):
    w1.lower()
    w2.lower()
    return lev.damerau_levenshtein_distance(w1, w2)


def matrix_fuzzmatch(words: list):
    start = t.time()
    matrix = np.array([[single_fuzzmatch(w1, w2) for w1 in words] for w2 in words])
    end = t.time()
    return matrix, end-start


def matrix_lev(words: list):
    start = t.time()
    matrix = np.array([[single_lev(w1, w2) for w1 in words] for w2 in words])
    end = t.time()
    return matrix, end-start


def single_wombocombo(w1: str, w2: str, dictionary):
    lev_d = single_lev(w1, w2)
    if lev_d == 0:
        return lev_d

    if dictionary.get(w1.lower()) is not None and dictionary.get(w2.lower()) is not None and w1.lower() != w2.lower():
        return lev_d + _HIGH_LEV_DIFFERENCE

    fuz1 = fw.ratio(w1, w2)
    fuz2 = fw.partial_ratio(w1, w2)
    fuz3 = fw.token_set_ratio(w1, w2)

# il coefficiente del 'partial ratio' va modificato (se non addirittura ridotto) in caso di città
# perchè molte città, anche diverse, hanno sottostringhe e token simili o uguali
# ES: Nocera Superiore e Nocera Inferiore

    fuzAverage = (fuz1 + fuz2 + fuz3)//3
    fuzsum = (fuz2 + fuz3) // 2

    if (fuzAverage > _HIGH_AVERAGE_FUZZY) or (fuzsum >= _HIGH_SUBSTRING_FUZZY):
        return 0

    if (fuzAverage < _LOW_AVERAGE_FUZZY) or (fuzsum < _LOW_SUBSTRING_FUZZY):
        lev_d = lev_d + _HIGH_LEV_DIFFERENCE

    return lev_d + _LOW_LEV_DIFFERENCE


def wombo_combo(words: list, dictionary):
    start = t.time()
    matrix = np.array([[single_wombocombo(w1, w2, dictionary) for w1 in words] for w2 in words])
    end = t.time()
    return matrix, end-start


def perfect_matching(words, dictionary):

    w = np.array([x.lower() if isinstance(x, str) else x for x in words])

    n_matching = 0

    for word in np.unique(w):
        if dictionary.get(word) is not None:
            n_matching += 1
    if n_matching == 0:
        n_matching = 1
    return n_matching, len(np.unique(words))
