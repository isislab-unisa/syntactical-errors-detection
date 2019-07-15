import unittest
from utilities import manage_data


class TestStringSimilarity(unittest.TestCase):

    "impossibile replicare la creazione di tutti gli elementi del dizionario"
    def test_load_regioni(self):
        regioni = {"basilicata":"basilicata",
                    "campania": "campania",
                    "lazio": "lazio",
                    "lombardia": "lombardia",
                    "piemonte": "piemonte",
                    "puglia": "puglia"}

        regioni_loaded = manage_data.load_regions(path="../elenco comuni.csv")

        for regioneKey, regioneValue in regioni.items():
            regione = regioni_loaded.get(regioneKey)
            self.assertEqual(regione, regioneValue)

    def test_load_province(self):
        province = {"salerno": "salerno",
                    "milano": "milano",
                    "roma": "roma",
                    "palermo": "palermo",
                    "torino": "torino",
                    "bari": "bari"}

        province_loaded = manage_data.load_province(path="../elenco comuni.csv")

        for provinciaKey, provinciaValue in province.items():
            provincia = province_loaded.get(provinciaKey)
            self.assertEqual(provincia, provinciaValue)

    def test_save_load_matrix(self):
        matrix = [[0, 5, 2],
                  [5, 0, 3],
                  [2, 3, 0]]

        manage_data.save_matrix(filename="../Test/testMatrix.npy", matrix=matrix)
        loaded_matrix = manage_data.load_matrix("../Test/testMatrix.npy")

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.assertEqual(matrix[i][j], loaded_matrix[i][j])