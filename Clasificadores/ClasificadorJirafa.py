#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import os

#Clase que dada una ruta te dice si esa imagen es una jirafa o no.
class ClasificadorJirafa(object):
  def __init__(self):
    self.modelo = keras.models.load_model('Modelos/modeloJirafa.h5')

  #Prepara la imagen para poder usar el tensor (es lo mismo que hacemos en preproceso).
  def __prepare_img__(self, route):
    arreglo_de_imagenes = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
    nuevo_arreglo = cv2.resize(arreglo_de_imagenes,(50, 50))
    return np.array(nuevo_arreglo).reshape(1,50,50,1) / 255

  # Determina si dada una ruta de una imagen, lo que contiene es una jirafa o no.
  def esJirafa(self, route):
    arreglo_de_imagenes = self.__prepare_img__(route)
    predicciones = self.modelo.predict(arreglo_de_imagenes) #Probabilidad de ser jirafa y de no serlo
    print(predicciones)
    max = np.argmax(predicciones) #0 si es una jirafa, 1 si no lo es.
    cat = ["Soy una jirafa. :) ","No soy una jirafa. :("]
    result = cat[max]
    if (max == 0):
      self.__muestraResultado__(result, np.array(arreglo_de_imagenes).reshape(50,50))
      return True
    else:
      return False
  
  #Muestra una imagen con un título.
  def __muestraResultado__(self, titulo, imagen):
    plt.figure()
    plt.title(titulo)
    plt.imshow(imagen)
    plt.grid(False)
    plt.show()

#Clasificamos todas las imágenes de prueba.
j = ClasificadorJirafa()  
for imagen in os.listdir("pruebas"):
  ruta = os.path.join("pruebas",imagen)  
  j.esJirafa(ruta)


#%%