import unittest
import Finanse_App


class TestWczytaj(unittest.TestCase):
    pw = "abc"
    A = Finanse_App.User("Bronia", pw, "Admin")
    A.obecny = "GBronia_1-6-2016.txt"
    A.aktualizuj()

    def testPW(self):
        self.assertEqual(self.A.password, hash(self.pw))

    def testDzisiejszy(self):
        self.assertEqual(self.A.dzisiejszy[9], "ON\n")

    def testObecny(self):
        self.assertTrue(self.A.obecny == "GBronia_1-6-2016.txt")

    def testCalyGrafik(self):
        self.assertIsInstance(self.A.calyGrafik["Czwartek"][9], str)
        self.assertIsInstance(self.A.calyGrafik["Poniedzialek"][9], str)
        self.assertIsInstance(self.A.calyGrafik["Wtorek"][9], str)
        self.assertIsInstance(self.A.calyGrafik["Sroda"][9], str)
        self.assertIsInstance(self.A.calyGrafik["Piatek"][9], str)
