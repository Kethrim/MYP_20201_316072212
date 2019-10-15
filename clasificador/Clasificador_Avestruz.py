from matplotlib import pyplot as plt
from tensorflow import keras
import cv2
import os
import numpy as np


class Clasificador_Avestruz(object):
    """Clase para hacer la comparación de una imagen con una avestruz"""

    def __init__(self):
        """
            Constructor de la clase
            Carga el modelo de la Avestruz para poder utilizarlo al evaluar
        """
        self.model = keras.models.load_model("modelos/Modelo_Avestruz.h5")

    def preparar_imagen(self, img):
        """
            Metodo para pixelar y pasar a escala de grises la imagen a probar
            
            @param img --Ruta de la imagen que se va a comparar
            @type img --String
            @return cv2.array
        """
        arreglo_imagenes = cv2.imread(img ,cv2.IMREAD_GRAYSCALE)
        nuevo_arreglo = cv2.resize(arreglo_imagenes,(50, 50))
        return nuevo_arreglo.reshape(-1,50,50,1) /255

    def evaluar(self, ruta):
        """
            Metodo para evaluar si la imagen es una avestruz o no

            @param ruta --Ruta de la imagen que se evaluara
            @type ruta --String
            @return True si es avestruz y False en otro caso    
        """
        img = self.preparar_imagen(ruta)
        prediccion = self.model.predict(img)
        maximo = np.argmax(prediccion)
        return maximo == 0