#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import pickle

#Clase que dada una ruta te dice si esa imagen es una jirafa o no.
class GiraffaClassifier(object):
  def __init__(self):
    self.modelo = keras.models.load_model('model.h5')

  #Prepara la imagen para poder usar el tensor (es lo mismo que hacemos en preproceso).
  def __prepare_img__(self, route):
    arreglo_de_imagenes = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
    nuevo_arreglo = cv2.resize(arreglo_de_imagenes,(50, 50))
    return np.array(nuevo_arreglo).reshape(1,50,50) / 255

  # Determina si dada una ruta de una imagen, lo que contiene es una jirafa o no.
  def esJirafa(self, route):
    arreglo_de_imagenes = self.__prepare_img__(route)
    predicciones = self.modelo.predict(arreglo_de_imagenes)
    print(predicciones)
    max = np.argmax(predicciones) #0 si no es una jirafa, 1 si lo es.
    cat = ["No soy una jirafa. :( ","Soy una jirafa. :)"]
    result = cat[max]
    plt.figure()
    plt.title(result)
    plt.imshow(np.array(arreglo_de_imagenes).reshape(50,50))
    plt.grid(False)
    plt.show()
    if(max == 0):
      return False
    else:
      return True




g = GiraffaClassifier()
#g.esJirafa("datos/jirafasss/_92895352_gettyimages-493199410.jpg")
# g.esJirafa('datos/pruebas/perrito.jpg')
#g.esJirafa('datos/pruebas/jirafa.jpg')
# g.esJirafa('datos/pruebas/vaca.jpg')
# g.esJirafa('datos/pruebas/avestruz.jpg')
# g.esJirafa('datos/pruebas/Conejo.jpg')
# g.esJirafa('datos/pruebas/bisonte.jpg')
#%%