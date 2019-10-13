#Librerias ocupadas
from matplotlib import pyplot as plt
from tensorflow import keras
import cv2
import os
import numpy as np


class OstrichClassifier(object):
    """Clase para hacer la comparación con la Avestruz"""
    def __init__(self):
        """Constructor de la clase"""
        self.model = keras.models.load_model("../Modelos/Model_Ostrich.h5")

    def prepare_image(self, img):
        """Metodo para pixelar y pasar a escala de grises la imagen a probar"""
        img_array = cv2.imread(img ,cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array,(50, 50))
        return new_array.reshape(-1,50,50,1) /255

    def evaluate(self, path):
        """Metodo para evaluar si la imagen es una avestruz o no"""
        img = self.prepare_image(path)
        prediction = self.model.predict(img)
        max = np.argmax(prediction)
        options = ["Avestruz", "Otro"]
        result = options[max]
        
        #De aqui en adelante todo es para dibujar la imagen
        plt.figure()
        plt.title(result)
        plt.imshow(np.array(img[0]).reshape(50,50))
        plt.show()