from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import pickle

#Clase que indica si el contenido de una imagen es un hipopotamo
class HippoClassifier(object):
    def __init__(self,model):
        #Carga el modelo de hippo clasifier
        self.model = self.load(model)
        #Tipo de animales que se pueden clasificar
        self.Data=["Hipopotamo","Otro animal"]
    
    #Prepara una imagen recibida convirtiendola en una arreglo np
    def pre_img(self, route): 
        """ recibe la direccion de una imagen y la convierte 
            a un arreglo de numpy.
            
            @type  route: string 
            @param route: ruta de la imagen
            @return: np.array
        """
        try:
            #se procesa la imagen para
            img_array = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array,(50, 50))
        except Exception as e:
            #si no se encontro la ruta de la imagen o esta dañada, se regresa un arreglo vacio
            return [] 
        return np.array(new_array).reshape(1,50,50,1) / 255
    
    def prueba(self,pictures,labels):
        test_loss, test_acc = self.model.evaluate(pictures, np.array(labels), verbose=2)
        print('\nTest accuracy:', test_acc)
        
        
    #Carga el modelo entrenado
    def load(self,model):
        """recibe la direccion del modelo entrenado y lo trata de abrir
           regresa el modelo entrenado o false si ocurrio un error.
            
            @type  model: string 
            @param model: rutal modelo
            @return: Keras.model | False
        """
        try:
            model=keras.models.load_model(model)
            return model
        except Exception:
            print("ocurrio un error al leer el modelo")
            return False
            
    #Regresa true o false si es un hipopotamo o no
    def is_hippo(self, img_route):   
        """recibe la ruta de una imagen, la evalua y regresa True si su contenido
           es un hipopotamo, False en otro caso
           
            @type  img_route: string 
            @param img_route: ruta de la imagen
            @return: True | False
        """
        img = self.pre_img(img_route)
        if(len(img) != 0):
            predictions = self.model.predict(img)
            max = np.argmax(predictions)
            if(max==6):
                return True
            else:
                return False
        else:
            print("Ocurrio un error al leer la imagen")
            

#%%
