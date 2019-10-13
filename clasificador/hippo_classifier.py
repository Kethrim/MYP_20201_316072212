#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import pickle

#Clase que indica si el contenido de una imagen es un hipopotamo
class HippoClassifier(object):
    def __init__(self):
        #Carga el modelo de hippo clasifier
        self.model = keras.models.load_model('hippo_model.h5')
        #Tipo de animales que se pueden clasificar
        self.Data=["Hipopotamo","Otro animal"]
    
    #Prepara una imagen recibida convirtiendola en una arreglo np
    def pre_img(self, route):
        try:
            img_array = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array,(50, 50))
        except Exception as e:
            return [] 
        return np.array(new_array).reshape(1,50,50,1) / 255

    #Regresa true o false si es un hipopotamo o no
    def is_hippo(self, img_route):   
        img = self.pre_img(img_route)
        if(len(img) != 0):
            predictions = self.model.predict(img)
            max = np.argmax(predictions)
            if(max==0):
                return False
            else:
                return True
        else:
            print("Ocurrio un error al leer la imagen")
            

#%%
