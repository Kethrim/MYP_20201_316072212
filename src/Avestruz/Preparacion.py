import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import pickle

#Importar ruta de Imagenes

class Preprocess(object):
    """Clase para preparar las imagenes con las que se entrenara la red"""
    def __init__(self, *args, **kwargs):
        """Metodo constructor"""
        self.DATADIR = "../../Data" #carpeta de carpetas
        self.CATEGORIES = ["Avestruz", "Otros"] #carpetas con imágenes
        self.IMG_SIZE = 50 #tamaño de la imagen
        self.training_data = []
        self.labels = []
        self.features = []

    def cargar_entrenamiento (self):
        """Metodo para vectorizar las imagenes con las que se entrenara la red"""
        #Recorremos cada carpeta dentro de Data
        for category in self.CATEGORIES:
            path = os.path.join(self.DATADIR, category)
            class_num = self.CATEGORIES.index(category)
            #Recorrer todas las imagenes dentro de la carpeta que apunta category
            for img in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array,(self.IMG_SIZE, self.IMG_SIZE))
                    self.training_data.append([new_array,class_num])
                except Exception as e:
                    pass

    def separar_y_preparar(self):
        """Metodo para pasar las listas de imagenes vectorizadas a un arreglo numpy"""
        random.shuffle(self.training_data)
        for features, label in self.training_data:
            self.features.append(features)
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.IMG_SIZE, self.IMG_SIZE,1)
        self.features = self.features/255.0
        self.labels = np.array(self.labels)

    def guardar(self):
        """Metodo para guardar las imagenes preparadas para el entrenamiento"""
        pickle_out = open("../Imagenes y Etiquetas/X.pickle", "wb")
        pickle.dump(self.features, pickle_out)
        pickle_out.close()

        pickle_out = open("../Imagenes y Etiquetas/Y.pickle", "wb")
        pickle.dump(self.labels, pickle_out)
        pickle_out.close()