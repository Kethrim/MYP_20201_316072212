import unittest
from clasificador.Clasificador_Avestruz import Clasificador_Avestruz as ca

class Pruebas_Avestruz(unittest.TestCase):
    """Pruebas unitarias de la clase Clasificador_Avestruz"""

    def test_es_Avestruz(self):
        """Metodo que prueba si una imagen es una avestruz"""
        clasifica = ca()
        self.assertTrue(clasifica.evaluar("revision/Avestruz.jpg"))

    def test_no_es_Avestruz(self):
        """Metodo que prueba si una imagen no es una avestruz"""
        clasifica = ca()
        self.assertFalse(clasifica.evaluar("revision/Cuyo.jpg"))
        self.assertFalse(clasifica.evaluar("revision/albaca.jpg"))
        self.assertFalse(clasifica.evaluar("revision/Hippo.jpg"))


if __name__ == '__main__':
    unittest.main()
