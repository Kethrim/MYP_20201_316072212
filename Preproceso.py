#%%s
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import pickle

#Creamos una clase que preprocesa las imágenes para usar el tensor.
class Preproceso(object):
    def __init__(self):
        self.DATADIR = "datos" #carpeta de imagenes
        self.CATEGORIES = ["jirafa","otros"] #carpetas con imágenes
        self.IMG_SIZE = 50 #tamaño de la imagen
        self.training_data = []
        self.labels = [] #arreglo
        self.features = []

    #Procesa las imágenes para que la red pueda leerlas.
    def load_training (self):
        for category in self.CATEGORIES:
            path = os.path.join(self.DATADIR, category)
            class_num = self.CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array,(self.IMG_SIZE, self.IMG_SIZE))  
                    self.training_data.append([new_array,class_num])
                except Exception as e:
                    pass

    #Divide en etiquetas e imágenes y las prepara.
    def split_and_prepare(self):
        random.shuffle(self.training_data) #desordena las tuplas
        for features, label in self.training_data:
            self.features.append(features)
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.IMG_SIZE, self.IMG_SIZE,1)
        self.features = self.features/255.0 #Normaliza el vector

    #Serialización de las imágenes y las tuplas.
    def write_out(self):
        pickle_out = open("X.pickle", "wb")
        pickle.dump(self.features, pickle_out)
        pickle_out.close()

        pickle_out = open("Y.pickle", "wb")
        pickle.dump(self.labels, pickle_out)
        pickle_out.close()

pr = Preproceso()
pr.load_training()
pr.split_and_prepare()
pr.write_out()

#%%
