import unittest
from clasificador.clasificadorCuyo import ClasificadorCuyo as c_cuyo

class cuyoPruebas(unittest.TestCase):

    def test_es_cuyo(self):
        identificador = c_cuyo()
        self.assertTrue(identificador.es_cuyo('revision/1_cuyo.jpg'))
        self.assertTrue(identificador.es_cuyo('revision/2_cuyo.jpg'))

    def test_no_es_cuyo(self):
        identificador = c_cuyo()
        self.assertFalse(identificador.es_cuyo('revision/141.perro2.jpg'))
        self.assertFalse(identificador.es_cuyo('revision/1.153-204034-hippo-dead-river-south-ethiopia_700x400.jpeg'))

if __name__ == '__main__':
    unittest.main()