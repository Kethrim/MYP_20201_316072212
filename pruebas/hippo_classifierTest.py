#%%
import unittest
from clasificador.hippo_classifier import HippoClassifier 

#Clase de pruebas unitarias de la clase hippo_classifier.py
class hippo_prueba(unittest.TestCase):
    
    #REvisa ue se cargue correctamente el modelo
    def test_load_model(self):
        hipo=HippoClassifier("Ruta invalida")
        self.assertFalse(hipo.model)
    
    #revisa si el modelo detecta que le contenido de una imagen no es un hipoptamo
    def test_is_not_hipo(self):
        hipo=HippoClassifier("modelos/hippo_model.h5")
        self.assertFalse(hipo.is_hippo('revision/141.perro2.jpg'))
    
   #revisa si el modelo detecta que le contenido de una imagen es un hipopotamo
    def test_is_hipo(self):
        hipo=HippoClassifier("modelos/hippo_model.h5")
        self.assertEqual(True,hipo.is_hippo('revision/1.153-204034-hippo-dead-river-south-ethiopia_700x400.jpeg'))
        
    #Revisa que se cache el error cuando se introduce una imagen erronea
    def test_load_image(self):
        hipo=HippoClassifier("modelos/hippo_model.h5")
        a=hipo.pre_img("Ruta invalida")
        self.assertTrue(len(a)==0)
 

if __name__ == '__main__':
    unittest.main()



#%%
