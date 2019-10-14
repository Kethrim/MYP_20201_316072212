from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import pickle

class ClasificadorCuyo(object):
  ''' Clase que identifica si en una imagen hay un cuyo
  Utilizado un modelo de tensorflow se verifica si el modelo es un cuyo
  '''

  def __init__(self):
    ''' Contructor que usa un modelo en la carpeta:
    - modelos/modeloCuyo.h5

    'No encuentro el modelo' : OSError
        Si el modelo no se encuentra en la ruta
    '''
    try:
      self.model = keras.models.load_model('modelos/modeloCuyo.h5')
    except OSError as ose:
      print('No encuentro el modelo, verifica que exista modelos/modeloCuyo.h5')

  def __prepara_img__(self, ruta):
    ''' Recibe la ruta relativa de una imagen y la convierte en un arrelgo numpy

    Parametros
    ----------
    ruta : str
        La ruta de la imagen

    Regresa
    -------
    arrelgoNum : np.array
        Un arreglo compatible con el modelo con el shape (1,50,50) y
        normalizado
    None 
        Si hubo un error al cargar la imagen
    '''
    try:
      img_array = cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)
      new_array = cv2.resize(img_array,(50, 50))

      return np.array(new_array).reshape(1,50,50) / 255
    except Exception as e:
      print('Error con la imagen!')

  def es_cuyo(self, ruta, mostrar=False):
    ''' Recibe la ruta relativa de una imagen e indica si la imagen:

    Parametros
    ----------
    ruta : str
        La ruta de la imagen

    mostrar : bool, opcional
        Por default, no se muestra la imagen, de otra manera
        se abre una ventana

    Regresa
    -------
    resultado : bool
        Regresa ´True´ si hemos encontrado un cuyo como protagonista o
        si la imagen tiene uno o mas cuyos
    '''
    img_array = self.__prepara_img__(ruta)
    prediccion = self.model.predict(img_array)
    max = np.argmax(prediccion[0])
    if mostrar:
      cases = ["Soy un cuyo c:","No soy un cuyo :c"]
      result = cases[max]
      plt.figure()
      plt.title(result)
      plt.imshow(np.array(img_array).reshape(50,50))
      plt.show()
    return 0 == max