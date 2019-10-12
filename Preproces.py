#%%
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import pickle
class Preprocess(object):

    def __init__(self, *args, **kwargs):
        self.DATADIR = "Data" #carpeta de carpetas
        self.CATEGORIES = ["Avestruz", "Otros"] #carpetas con imágenes
        self.IMG_SIZE = 50 #tamaño de la imagen
        self.training_data = []
        self.labels = []
        self.features = []

    def load_training (self):
        for category in self.CATEGORIES:
            path = os.path.join(self.DATADIR, category)
            class_num = self.CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    #img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_GRAYSCALE)
                    #new_array = cv2.resize(img_array,(self.IMG_SIZE, self.IMG_SIZE))
                    new_array = get_array_numpy(path, img)
                    self.training_data.append([new_array,class_num])
                except Exception as e:
                    pass

    def split_and_prepare(self):
        random.shuffle(self.training_data)
        for features, label in self.training_data:
            self.features.append(features)
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.IMG_SIZE, self.IMG_SIZE,1)
        self.features = self.features/255.0
        self.labels = np.array(self.labels)

    def write_out(self):
        pickle_out = open("X.pickle", "wb")
        pickle.dump(self.features, pickle_out)
        pickle_out.close()

        pickle_out = open("Y.pickle", "wb")
        pickle.dump(self.labels, pickle_out)
        pickle_out.close()

#%%
