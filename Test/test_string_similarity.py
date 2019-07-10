import unittest
from utilities import string_similarity


class TestStringSimilarity(unittest.TestCase):

    def test_single_wombocombo(self):
        dictionary = {"torino":"torino", "milano":"milano", "salerno":"salerno", "salernoo":"salernoo"}
        word1 = ["Torino", "Torinooo", "Milano", "Salerno"]
        word2 = ["Torino", "Torino", "Salerno", "Salernoo"]
        result = [0, 0, 24, 21]
        for i in range(0, 4):
            lev = string_similarity.single_wombocombo(word1[i], word2[i], dictionary)
            self.assertEqual(lev, result[i])

    def test_wombocombo(self):
        dictionary = {"torino":"torino", "milano":"milano", "salerno":"salerno", "salernoo":"salernoo"}
        word = ["Torino", "Torino", "Torinooo", "Milano", "Salerno", "Salernoo"]
        result = [[0,  0,  0, 24, 25, 26],
                  [0,  0,  0, 24, 25, 26],
                  [0,  0,  0, 31, 32, 31],
                  [24, 24, 31,  0, 24, 25],
                  [25, 25, 32, 24,  0, 21],
                  [26, 26, 31, 25, 21,  0]]

        matrix, time = string_similarity.wombo_combo(word, dictionary)

        for i in range(0,6):
            for j in range(0,6):
                self.assertEqual(result[i][j], matrix[i][j])

    def test_perfect_matching(self):
        dictionary = {"torino": "torino", "milano": "milano", "salerno": "salerno", "salernoo": "salernoo"}
        word = ["Torino", "Torino", "Torinooo", "Milano", "Salerno", "Salernoo"]

        minres = 4
        maxres= 5

        min, max = string_similarity.perfect_matching(word, dictionary)

        self.assertEqual(min, minres)
        self.assertEqual(max, maxres)

    def test_single_fuzzy(self):
        word1 = "Barack Obama"
        word2 = "Barack H. Obama"

        res = (-1)*string_similarity.single_fuzzmatch(word1, word2)

        self.assertGreaterEqual(res, string_similarity.HIGH_AVERAGE_FUZZY)

