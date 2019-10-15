import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import pickle

#Importar ruta de Imagenes

class Preparacion_Avestruz(object):
    """Clase para preparar las imagenes con las que se entrenara la red"""
    def __init__(self, *args, **kwargs):
        """Metodo constructor"""
        self.DATADIR = "data" #carpeta de carpetas
        self.CATEGORIAS = ["Avestruz", "Otros"] #carpetas con imágenes
        self.TAM_IMG = 50 #tamaño de la imagen
        self.datos_entrenados = []
        self.labels = []
        self.features = []

    def cargar_entrenamiento(self):
        """Metodo para vectorizar las imagenes con las que se entrenara la red"""
        #Recorremos cada carpeta dentro de Data
        for categoria in self.CATEGORIAS:
            ruta = os.path.join(self.DATADIR, categoria)
            class_num = self.CATEGORIAS.index(categoria)
            #Recorrer todas las imagenes dentro de la carpeta que apunta category
            for img in os.listdir(ruta):
                try:
                    arreglo_img = cv2.imread(os.path.join(ruta, img),cv2.IMREAD_GRAYSCALE)
                    nuevo_arreglo = cv2.resize(img_array,(self.TAM_IMG, self.TAM_IMG))
                    self.training_data.append([nuevo_arreglo,class_num])
                except Exception as e:
                    pass

    def separar_y_preparar(self):
        """Metodo para pasar las listas de imagenes vectorizadas a un arreglo numpy"""
        random.shuffle(self.training_data)
        for features, label in self.datos_entrenados:
            self.features.append(features)
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.TAM_IMG, self.TAM_IMG,1)
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
