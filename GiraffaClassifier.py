#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import pickle

class GiraffaClassifier(object):
  def __init__(self):
    self.model = keras.models.load_model('model.h5')

  #Prepara la imagen para poder usar el tensor.
  def __prepare_img__(self, route):
    img_array = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array,(50, 50))
    return np.array(new_array).reshape(1,50,50,1) / 255

  # Determina si dada una ruta de una imagen, lo que contiene es una jirafa o no.
  def is_Giraffa(self, route, show=False):
    img_array = self.__prepare_img__(route)
    predictions = self.model.predict(img_array)
    max = np.argmax(predictions) #0 si es una jirafa, 1 si no lo es.
    cat = ["Soy una jirafa. :) ","No soy una jirafa. :("]
    result = cat[max]
    if show:
      plt.figure()
      plt.title(result)
      plt.imshow(np.array(img_array).reshape(50,50))
      plt.grid(False)
      plt.show()
    if(max == 1):
       return False
    else:
       return True


g = GiraffaClassifier()
g.is_Giraffa('datos/pruebas/perrito.jpg',True)
#%%