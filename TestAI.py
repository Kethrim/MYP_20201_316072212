#%%
from matplotlib import pyplot as plt
from tensorflow import keras
import cv2
import os
import numpy as np

class OstrichClassifier(object):
    def __init__(self):
        self.model = keras.models.load_model("model.h5")

    def prepare_image(self, img):
        img_array = cv2.imread(img ,cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array,(50, 50))
        return new_array.reshape(-1,50,50,1) /255

    def evaluate(self):
        img = self.prepare_image(os.path.join("test_img","Ostrich.jpg"))
        prediction = self.model.predict(img)
        max = np.argmax(prediction)
        options = ["Avestruz", "Otro"]
        result = options[max]
        plt.figure()
        plt.title(result)
        plt.imshow(np.array(img[0]).reshape(50,50))
        plt.show()
