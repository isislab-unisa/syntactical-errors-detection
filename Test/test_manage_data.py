import unittest
from utilities import manage_data
from itertools import product

class TestStringSimilarity(unittest.TestCase):

    "impossibile replicare la creazione di tutti gli elementi del dizionario"
    def test_load_regioni(self):
        regioni = {"basilicata":"Basilicata",
                    "campania": "Campania",
                    "lazio": "Lazio",
                    "lombardia": "Lombardia",
                    "piemonte": "Piemonte",
                    "puglia": "Puglia"}

        regioni_loaded = manage_data.load_regions(path="../elenco comuni.csv")

        for regioneKey, regioneValue in regioni.items():
            regione = regioni_loaded.get(regioneKey)
            self.assertEqual(regione, regioneValue)

    def test_load_province(self):
        province = {"salerno": "Salerno",
                    "milano": "Milano",
                    "roma": "Roma",
                    "palermo": "Palermo",
                    "torino": "Torino",
                    "bari": "Bari"}

        province_loaded = manage_data.load_province(path="../elenco comuni.csv")

        for provinciaKey, provinciaValue in province.items():
            provincia = province_loaded.get(provinciaKey)
            self.assertEqual(provincia, provinciaValue)

    def test_load_comuni(self):
        comuni = {"salerno": "Salerno",
                    "lomello": "Lomello",
                    "roma": "Roma",
                    "palermo": "Palermo",
                    "torino": "Torino",
                    "scaldasole": "Scaldasole"}

        comuni_loaded = manage_data.load_comuni(path="../elenco comuni.csv")

        for comuneKey, comuneValue in comuni.items():
            comune = comuni_loaded.get(comuneKey)
            self.assertEqual(comune, comuneValue)

    def test_save_load_matrix(self):
        matrix = [[0, 5, 2],
                  [5, 0, 3],
                  [2, 3, 0]]

        manage_data.save_matrix(filename="../Test/testMatrix.npy", matrix=matrix)
        loaded_matrix = manage_data.load_matrix("../Test/testMatrix.npy")

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.assertEqual(matrix[i][j], loaded_matrix[i][j])

    def test_load_csv(self):
        test1 = [i for i in range(1, 101)]
        test2 = [i for i in range(1, 370)]
        test3 = ["a", "Non specificato", "Non specificato", "a", "a"]

        csv1 = manage_data.load_csv(csv_name="testCsv.csv", nrows=100, column="Test")
        csv2 = manage_data.load_csv(csv_name="testCsv.csv", column="Test")
        csv3 = manage_data.load_csv(csv_name="testCsv2.csv", column="Test")

        for i, t1 in enumerate(test1):
            self.assertEqual(t1, csv1[i])

        for i, t2 in enumerate(test2):
            self.assertEqual(t2, csv2[i])

        for i, t3 in enumerate(test3):
            self.assertEqual(t3, csv3[i])