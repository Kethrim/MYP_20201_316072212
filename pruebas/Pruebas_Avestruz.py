import unittest
from clasificador.Clasificador_Avestruz import Clasificador_Avestruz

class Pruebas_Avestruz(unittest.TestCase):
    """Pruebas unitarias de la clase Clasificador_Avestruz"""
    
    def __init__(self):
        """Constructor, crea el clasificador de Avestruz"""
        clasifica = Clasificador_Avestruz()
        
    def prueba_es_Avestruz(self):
        """Metodo que prueba si una imagen es una avestruz"""
        self.assertTrue(clasifica.evaluar("../revision/Avestruz.jpg"))
    
    def prueba_no_es_Avestruz(self):
        """Metodo que prueba si una imagen no es una avestruz"""
        self.asserFalse(clasifica.evaluar("../revision/Cuyo.jpg"))
        

if __name__ == '__main__':
    unittest.main()