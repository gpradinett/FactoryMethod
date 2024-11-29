import unittest
from  biciomoto import BiciCreator, MotoCreator, MotoProduct

class TestFactoryMethod(unittest.TestCase):
    def test_bici_creator(self):
        creator = BiciCreator()
        product = creator.factory_method()
        self.assertEqual(product.operation(), "{Bici Creada}")
        self.assertEqual(product.get_features(), "Características: pedal, Color: rojo")
    
    def test_moto_creator(self):
        creator = MotoCreator()
        product = creator.factory_method()
        self.assertEqual(product.operation(), "{Moto Creada}")
        self.assertEqual(product.get_features(), "Características: Motor, Color: Negro")

    def test_invalid_moto(self):
        with self.assertRaises(ValueError):
            MotoProduct(color="Blanco", caracteristica="100")
