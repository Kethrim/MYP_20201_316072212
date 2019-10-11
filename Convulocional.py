#%%
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras

#Lirerías de apoyo.
import numpy as np
import matplotlib.pyplot as plt
import pickle

#Clase que entrena a la red neuronal.
class Convulocional(object):
    def __init__(self, nuevoModelo = False):
        #Abrimos los archivos que contienen las imágenes y las etiquetas
        self.IMAGENES = pickle.load(open("X.pickle", "rb"))
        self.ETIQUETAS = pickle.load(open("Y.pickle", "rb"))

        #Si ya hay un modelo creado solo lo cargamos.
        if nuevoModelo:
            self.modelo = keras.models.load_model('model.h5')
        else: #Creamos el modelo.
            # Declaramos las capas de la red.
            self.modelo = keras.Sequential([
            keras.layers.Flatten(input_shape=(50, 50)), #Dimensiones de la imagen declaradas en preproceso.
            keras.layers.Dense(128, activation=tf.nn.relu), #128 nodos
            keras.layers.Dense(2, activation=tf.nn.softmax) #2 etiquetas
            ])

            # Compilar el modelo con algunos parametros basicos
            self.modelo.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    #Entrena el modelo y lo guarda en un archivo .h5
    def entrenaYGuarda(self):
        self.modelo.fit(self.IMAGENES, self.ETIQUETAS, epochs=100) #ejecuta el entrenamiento 100 veces.
        self.modelo.save('model.h5') #guarda el modelo en "model.h5"

c = Convulocional()
c.entrenaYGuarda()
#%%
