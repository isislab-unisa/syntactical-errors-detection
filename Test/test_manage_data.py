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

        regioni_loaded = manage_data.load_regions()

        for regioneKey, regioneValue in regioni.items():
            regione = regioni_loaded.get(regioneKey)
            self.assertEqual(regione, regioneValue)

    def test_load_province(self):
        province = {"salerno":"salerno",
                    "milano": "milano",
                    "roma": "roma",
                    "palermo": "lombardia",
                    "piemonte": "piemonte",
                    "puglia": "puglia"}

        province_loaded = manage_data.load_regions()

        for provinciaKey, provinciaValue in province.items():
            provincia = province_loaded.get(provinciaKey)
            self.assertEqual(provincia, provinciaValue)
