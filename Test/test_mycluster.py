import unittest
from utilities import manage_data, mycluster, string_similarity
import numpy as np


#testing clustering controllando i due vettori degli indici

class TestMyCluster(unittest.TestCase):

    def test_find_samples(self):
        province = manage_data.load_province("../elenco comuni.csv")
        words1 = ["Saler", "Saler", "Salern", "Salerr", "alerno"]
        words2 = ["Saler", "Saler", "Salern", "Salerr", "alerno", "Salerno"]
        res1 = "Saler"
        res2 = "Salerno"

        sample1 = mycluster.find_samples(words1, np.unique(words1), province)
        sample2 = mycluster.find_samples(words2, np.unique(words2), province)

        self.assertEqual(res1.lower(), sample1.lower())
        self.assertEqual(res2.lower(), sample2.lower())


    def test_propose_correction_general(self):
        province = manage_data.load_province("../elenco comuni.csv")

        clusters = [["Saler", "Saler", "Salern", "Salerr", "alerno", "Salerno"],
                    ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                    ["Milan", "Milan", "Milan", "Milan"],
                    ["Salerno", "Milan", "Salern", "Milan", "Milan"],
                    ["Salern", "Milan", "Salern", "Milan", "Milan"]]

        res = [["Salerno", "Salerno", "Salerno", "Salerno", "Salerno", "Salerno"],
               ["Napoli", "Napoli", "Napoli", "Napoli", "Napoli"],
               ["Milano", "Milano", "Milano", "Milano"],
               ["Salerno", "Milano", "Salerno", "Milano", "Milano"],
               ["Salerno", "Milano", "Salerno", "Milano", "Milano"]]

        correction = mycluster.propose_correction_general(clusters, province)
        print(correction)
        print("\n")
        print(res)
        for i, cluster in enumerate(res):
            for j, element in enumerate(cluster):
                print(correction[i][j].lower(), element.lower())
                self.assertEqual(correction[i][j].lower(), element.lower())

    def test_collapse(self):

        province = manage_data.load_province("../elenco comuni.csv")
        clusters1 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                 ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                 ["Milan", "Milan", "Milan", "Milan"]]

        clusters2 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                 ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                 ["Milan", "Milan", "Milan", "Milan"],
                 ["Salerno"]]

        res1 = mycluster.collapse(clusters1, province)
        res2 = mycluster.collapse(clusters2, province)

        self.assertTrue(res1)
        self.assertFalse(res2)

    def test_split(self):

        province = manage_data.load_province("../elenco comuni.csv")
        clusters1 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                 ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                 ["Milan", "Milan", "Milan", "Milan"]]

        clusters2 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                 ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                 ["Milan", "Milan", "Milan", "Milan", "Salerno"]]

        clusters3 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                 ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                 ["Milano", "Milano", "Milano", "Milano", "Salerno"]]

        res1 = mycluster.split(clusters1, province)
        res2 = mycluster.split(clusters2, province)
        res3 = mycluster.split(clusters3, province)

        self.assertTrue(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)

    def test_check_clusters(self):
        province = manage_data.load_province("../elenco comuni.csv")
        clusters1 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                     ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                     ["Milan", "Milan", "Milan", "Milan"]]

        clusters2 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                     ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                     ["Milan", "Milan", "Milan", "Milan", "Salerno"]]

        clusters3 = [["Saler", "Saler", "Salern", "Salerr", "Salerno", "Salerno"],
                     ["Napoli", "Napoli", "Napol", "Napo", "Napoli"],
                     ["Milan", "Milan", "Milan", "Milan"],
                     ["Salerno"]]

        res1, msg = mycluster.check_clusters(clusters1, province)
        res2, msg = mycluster.check_clusters(clusters2, province)
        res3, msg = mycluster.check_clusters(clusters3, province)

        self.assertTrue(res1)
        self.assertFalse(res2)
        self.assertFalse(res3)
