import unittest
from Clasificador import clasificador

#Prueba de una serie de imágenes para saber qué animal son.
class test_clasificador(unittest.TestCase):
    '''
    Prueba de clasificador.
    '''

    def test_EsJirafa(self):
        """
        Verifica que una serie de imágenes sean reconocidas como jirafas.
        """
        self.idJ = clasificador()
        self.assertEqual('Es una jirafa!', self.idJ.queAnimalEs("revision/jirafa_prueba.jpg"))
        self.assertEqual('Es una jirafa!', self.idJ.queAnimalEs("revision/jirafa2_prueba.jpg"))

    def test_EsHipopotamo(self):
        """
        Verifica que una serie de imágenes sean reconocidas como hipopótamos.
        """
        self.idH = clasificador()
        self.assertEqual('Es un hipopotamo!', self.idH.queAnimalEs('revision/1.153-204034-hippo-dead-river-south-ethiopia_700x400.jpeg'))
        self.assertEqual('Es un hipopotamo!', self.idH.queAnimalEs('revision/hipo_prueba.jpg'))
        self.assertEqual('Es un hipopotamo!', self.idH.queAnimalEs('revision/Hippo.jpg'))
    
    def test_EsAvestruz(self):
        """
        Verifica que una serie de imágenes sean reconocidas como avestruces.
        """
        self.idA = clasificador()
        self.assertEqual('Es un avestruz!', self.idA.queAnimalEs('revision/avestruz_prueba.jpeg'))
        self.assertEqual('Es un avestruz!', self.idA.queAnimalEs('revision/Avestruz.jpg'))
    
    def test_EsCuyo(self):
        """
        Verifica que una serie de imágenes sean reconocidas como cuyos.
        """
        self.idC = clasificador()
        self.assertEqual('Es un cuyo!', self.idC.queAnimalEs('revision/1_cuyo.jpg'))
        self.assertEqual('Es un cuyo!', self.idC.queAnimalEs('revision/2_cuyo.jpg'))
        self.assertEqual('Es un cuyo!', self.idC.queAnimalEs('revision/cuyo_prueba.jpg'))
        self.assertEqual('Es un cuyo!', self.idC.queAnimalEs('revision/Cuyo.jpg'))

    def test_EsPinguino(self):
        """
        Verifica que una serie de imágenes sean reconocidas como pinguinos.
        """
        self.idP = clasificador()
        self.assertEqual('Es un pinguino!', self.idP.queAnimalEs('revision/pingu_prueba.jpg'))
    
    
    def test_NoEs(self):
        """
        Rectifica que un un animal diferente a un avestruz, un cuyo, un pinguino, una jirafa un hipopótamo no seas reconocidos como uno de ellos..
        """
        self.id = clasificador()
        self.assertEqual('No es ningún animal.', self.id.queAnimalEs('revision/141.perro2.jpg'))
        self.assertEqual('No es ningún animal.', self.id.queAnimalEs('revision/elefante.jpg'))

    def test_rutaInvalida(self):
        """
        Checa que una ruta inválida no rompa el programa.
        """
        self.idR = clasificador()
        self.assertEqual('Ingresa una nueva ruta.', self.idR.queAnimalEs('rutaInvalida'))

if __name__ == "__main__":
    uniitest.main()