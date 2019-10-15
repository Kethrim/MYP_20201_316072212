#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import os

#Clase que dada una ruta te dice si esa imagen es una pingüino o no.
class clasificadorPinguino(object):
  """
  Clasifica imágenes en si son pinguinos o no.
  """
  def __init__(self):
    try:
      self.modelo = keras.models.load_model('modelos/pingu_model2.h5')
    except Exception as e:
      print("ERROR: No existe el modelo.")

  #Prepara la imagen para poder usar el tensor (es lo mismo que hacemos en preproceso).
  def __prepare_img__(self, ruta):
    """
    Prepara una imagen para que la red pueda identificar si es o no una pingüino.
    
    @type ruta: string
    @param ruta: imagen que se preparará.
    """
    arreglo_de_imagenes = cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)
    nuevo_arreglo = cv2.resize(arreglo_de_imagenes,(50, 50))      
    return np.array(nuevo_arreglo).reshape(1,50,50,1) / 255

  # Determina si dada una ruta de una imagen, lo que contiene es una pingüino o no.
  def esPinguino(self, ruta):
    """"
    Determinada que dada una ruta, la imagen sea una pingüino.
    
    @type ruta: string
    @param ruta: imagen que desea comprobar.
    @return booleano que inidica si es pingüino o no.
    """
    try:
      arreglo_de_imagenes = self.__prepare_img__(ruta)
      predicciones = self.modelo.predict(arreglo_de_imagenes) 
      max = np.argmax(predicciones) 
    except Exception as e:
      return False
    if (max == 2):
      return True
    else:
      return False


#%%
