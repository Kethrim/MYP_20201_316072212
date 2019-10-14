import unittest
from clasificador.clasificadorJirafa import clasificadorJirafa as jirafa

#from Clasificadores.ClasificadorJirafa import ClasificadorJirafa as jirafa
#Prueba de una serie de imágenes para saber si son una jirafa o no. 
class test_clasificadorJirafa(unittest.TestCase):
    '''
    Prueba de clasificadorJirafa.
    '''
    def test_EsJirafa(self):
        """
        Verifica que dos imágenes de jirafas seas reconocidas como jirafas.
        """
        id = jirafa()
        self.assertTrue(id.esJirafa("revision/jirafa_prueba.jpg"))
        self.assertTrue(id.esJirafa("revision/jirafa2_prueba.jpg"))
    
    def test_NoEsJirafa(self):
        """
        Rectifica que un avestruz, un cuyo, un pinguino y un hipopótamo no seas reconocidos como jirafas.
        """
        id = jirafa()
        self.assertFalse(id.esJirafa("revision/avestruz_prueba.jpeg"))
        self.assertFalse(id.esJirafa("revision/cuyo_prueba.jpg"))
        self.assertFalse(id.esJirafa("revision/hipo_prueba.jpg"))
        self.assertFalse(id.esJirafa("revision/pingu_prueba.jpg"))

if __name__ == "__main__":
    uniitest.main()