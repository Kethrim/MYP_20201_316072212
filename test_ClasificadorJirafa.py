import unittest
from Clasificadores.ClasificadorJirafa import ClasificadorJirafa as jirafa
#Prueba de una serie de imágenes para saber si son una jirafa o no. 
class test_ClasificadorJirafa(unittest.TestCase):

    def test_EsJirafa(self):
        id = jirafa()
        self.assertTrue(id.esJirafa("test_Imagenes/jirafa_prueba.jpg"))
        self.assertTrue(id.esJirafa("test_Imagenes/jirafa2_prueba.jpg"))
        self.assertFalse(id.esJirafa("test_Imagenes/avestruz_prueba.jpeg"))
        self.assertFalse(id.esJirafa("test_Imagenes/cuyo_prueba.jpg"))
        self.assertFalse(id.esJirafa("test_Imagenes/hipo_prueba.jpg"))
        self.assertFalse(id.esJirafa("test_Imagenes/pingu_prueba.jpg"))

if __name__ == "__main__":
    uniitest.main()