#Librerias ocupadas
from matplotlib import pyplot as plt
from tensorflow import keras
import cv2
import os
import numpy as np


class Clasificador_Avestruz(object):
    """Clase para hacer la comparación con la Avestruz"""
    def __init__(self):
        """Constructor de la clase"""
        self.model = keras.models.load_model("modelos/Model_Ostrich.h5")

    def preparar_imagen(self, img):
        """Metodo para pixelar y pasar a escala de grises la imagen a probar"""
        arreglo_imagenes = cv2.imread(img ,cv2.IMREAD_GRAYSCALE)
        nuevo_arreglo = cv2.resize(arreglo_imagenes,(50, 50))
        return nuevo_arreglo.reshape(-1,50,50,1) /255

    def evaluar(self, ruta):
        """Metodo para evaluar si la imagen es una avestruz o no"""
        img = self.preparar_imagen(ruta)
        prediccion = self.model.predict(img)
        maximo = np.argmax(prediccion)
        #print(maximo == 0)
        return maximo == 0
        
        
        #De aqui en adelante todo es para dibujar la imagen
        #plt.figure()
        #plt.title(resultado)
        #plt.imshow(np.array(img[0]).reshape(50,50))
        #plt.show()
