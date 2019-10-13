#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import os

#Clase que dada una ruta te dice si esa imagen es una jirafa o no.
class ClasificadorJirafa(object):
  def __init__(self):
    self.modelo = keras.models.load_model('/home/ket/Escritorio/PythonWebAI/Modelos/modeloJirafa.h5')

  #Prepara la imagen para poder usar el tensor (es lo mismo que hacemos en preproceso).
  def __prepare_img__(self, route):
    arreglo_de_imagenes = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
    nuevo_arreglo = cv2.resize(arreglo_de_imagenes,(50, 50))
    return np.array(nuevo_arreglo).reshape(1,50,50,1) / 255

  # Determina si dada una ruta de una imagen, lo que contiene es una jirafa o no.
  def esJirafa(self, route):
    arreglo_de_imagenes = self.__prepare_img__(route)
    predicciones = self.modelo.predict(arreglo_de_imagenes)
    print(predicciones)
    max = np.argmax(predicciones) #0 si es una jirafa, 1 si no lo es.
    cat = ["Soy una jirafa. :) ","No soy una jirafa. :("]
    result = cat[max]
    if (max == 0):
      plt.figure()
      plt.title(result)
      plt.imshow(np.array(arreglo_de_imagenes).reshape(50,50))
      plt.grid(False)
      plt.show()
      return False
    else:
      return True


j = ClasificadorJirafa()    
for imagen in os.listdir("/home/ket/Escritorio/PythonWebAI/pruebas"):
  ruta = os.path.join("/home/ket/Escritorio/PythonWebAI/pruebas",imagen)  
  j.esJirafa(ruta)


#%%