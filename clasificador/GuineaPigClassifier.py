from matplotlib import pyplot as plt 
from tensorflow import keras
import cv2
import numpy as np
import pickle

class GuineaPigClassifier(object):
  def __init__(self):
    self.model = keras.models.load_model('modelos/guinea_pig_model.h5')

  def __prepare_img__(self, route):
    img_array = cv2.imread(route,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array,(50, 50))
    return np.array(new_array).reshape(1,50,50) / 255

  def is_guineaPig(self, route, show=False):
    img_array = self.__prepare_img__(route)
    predictions = self.model.predict(img_array)
    max = np.argmax(predictions[0])
    cases = ["Soy un cuyo c:","No soy un cuyo :c"]
    result = cases[max]
    if show:
      plt.figure()
      plt.title(result)
      plt.imshow(np.array(img_array).reshape(50,50))
      plt.show()
    return 0 == max