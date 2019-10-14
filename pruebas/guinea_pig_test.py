import unittest
from clasificador.GuineaPigClassifier import GuineaPigClassifier as c_cuyo

class cuyoPruebas(unittest.TestCase):

    def test_es_cuyo(self):
        identificador = c_cuyo()
        self.assertTrue(identificador.is_guineaPig('revision/1_cuyo.jpg'))
        self.assertTrue(identificador.is_guineaPig('revision/2_cuyo.jpg'))

if __name__ == '__main__':
    unittest.main()