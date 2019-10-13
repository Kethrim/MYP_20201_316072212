import unittest
from Clasificadores.ClasificadorJirafa import ClasificadorJirafa as jirafa
#from Clasificadores.ClasificadorJirafa import ClasificadorJirafa as jirafa
#Prueba de una serie de imágenes para saber si son una jirafa o no. 
class test_ClasificadorJirafa(unittest.TestCase):
    '''
    Prueba de ClasificadorJirafa.
    '''
    def test_EsJirafa(self):
        """
        Verifica que dos imágenes de jirafas seas reconocidas como jirafas.
        """
        id = jirafa()
        self.assertTrue(id.esJirafa("Pruebas/test_Imagenes/jirafa_prueba.jpg"))
        self.assertTrue(id.esJirafa("Pruebas/test_Imagenes/jirafa2_prueba.jpg"))
    
    def test_NoEsJirafa(self):
        """
        Rectifica que un avestruz, un cuyo, un pinguino y un hipopótamo no seas reconocidos como jirafas.
        """
        id = jirafa()
        self.assertFalse(id.esJirafa("Pruebas/test_Imagenes/avestruz_prueba.jpeg"))
        self.assertFalse(id.esJirafa("Pruebas/test_Imagenes/cuyo_prueba.jpg"))
        self.assertFalse(id.esJirafa("Pruebas/test_Imagenes/hipo_prueba.jpg"))
        self.assertFalse(id.esJirafa("Pruebas/test_Imagenes/pingu_prueba.jpg"))

if __name__ == "__main__":
    uniitest.main()