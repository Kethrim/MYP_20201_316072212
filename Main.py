#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import os

class clasificador(Object):
    """
    Clasifica una imagen en las categorías: 
    Avestruz
    Cuyo
    Hipopótamo
    Jirafa
    Pingüino
    """
    def __prepara_img__(self, ruta):
    """
    Prepara una imagen para que la red pueda usarla.
    @type ruta: string
    @param ruta: imagen que se preparará.
    """
    arreglo_de_imagenes = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    nuevo_arreglo = cv2.resize(arreglo_de_imagenes,(50, 50))
    return np.array(nuevo_arreglo).reshape(1,50,50,1) / 255

    def queAnimalEs(self, ruta):
        #Aquí podemos importar cada clasificador y usar cada método que tenemos, será más fácil pues ese método regresa un booleano
        return False
