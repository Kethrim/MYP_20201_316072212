#%%s
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import pickle

class Preproceso(object):
    '''
    Preprocesa las imágenes que poder usar tensorFlow.
    '''
    def __init__(self):
        self.DATADIR = "datos" #carpeta de imagenes
        self.CATEGORIES = ["Pinguinos", "Otros"] #carpetas con imágenes
        self.IMG_SIZE = 50 #tamaño de la imagen
        self.training_data = []
        self.labels = [] #arreglo de etiquetas
        self.features = []

    def load_training (self):
        '''
        Obtiene las imágenes de las subcarpetas y las procesa para que la red pueda usarlas.
        '''
        for category in self.CATEGORIES:
            path = os.path.join(self.DATADIR, category)
            class_num = self.CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    #La imagen pasa a escala de grises.
                    img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_GRAYSCALE)
                    #Modificamos el tamaño de la imagen.
                    new_array = cv2.resize(img_array,(self.IMG_SIZE, self.IMG_SIZE))  
                    self.training_data.append([new_array,class_num])
                except Exception as e:
                    pass

    def split_and_prepare(self):
        '''
        Divide en etiquetas e imágenes.
        '''
        random.shuffle(self.training_data) #desordena las tuplas
        for features, label in self.training_data:
            self.features.append(features)                      
            self.labels.append(label)
        self.features = np.array(self.features).reshape(-1,self.IMG_SIZE, self.IMG_SIZE,1)
        self.features = self.features/255.0 #Normaliza el vector
   
    def write_out(self):
        '''
        Serialización de las imágenes y etiquetas en un archivo de bytes.
        '''
        pickle_out = open("X_Pinguino.pickle", "wb")
        pickle.dump(self.features, pickle_out)
        pickle_out.close()

        pickle_out = open("Y_Pinguino.pickle", "wb")
        pickle.dump(self.labels, pickle_out)
        pickle_out.close()

#Preprocesamos las imágenes. 
# pr = Preproceso()
# pr.load_training()
# pr.split_and_prepare()
# pr.write_out()

#%%
