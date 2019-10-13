
import unittest
from clasificador.hippo_classifier import HippoClassifier 

class hippo_prueba(unittest.TestCase):
    
    def load_model(self):
        hipo=HippoClassifier("hgggg")
        self.assertFalse(hipo.model)
    
    def is_not_hipo(self):
        hipo=HippoClassifier("modelos/hippo_model.h5")
        self.assertFalse(hipo.is_hippo('revision/141.perro2.jpg'))
    
    
    def is_hipo(self):
        hipo=HippoClassifier("modelos/hippo_model.h5")
        self.assertEqual(True,self.assertTrue(hipo.is_hippo('revision/1.153-204034-hippo-dead-river-south-ethiopia_700x400.jpeg')))
        
    
    def load_image(self):
        hipo=HippoClassifier("modelos/hippo_model.h5")
        a=hipo.pre_img("pruebas")
        self.assertTrue(len(a)!=0)
 

if __name__ == '__main__':
    unittest.main()


