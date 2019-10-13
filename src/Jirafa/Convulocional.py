#%%
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras

#Lirerías de apoyo.
import numpy as np
import matplotlib.pyplot as plt
import pickle

class Convulocional(object):
    '''
    Entrena a la red neuronal.
    '''
    def __init__(self, nuevoModelo = False):
        '''
        Usa un modelo para entrenar.
        @type nuevoModelo: boolean
        @param nuevoModelo: si ya existe el modelo pasar True, de no ser así se crea uno.
        '''
        #Abrimos los archivos que contienen las imágenes y las etiquetas
        self.IMAGENES = pickle.load(open("X_Jirafa.pickle", "rb"))
        self.ETIQUETAS = pickle.load(open("Y_Jirafa.pickle", "rb"))

        #Si ya hay un modelo creado solo lo cargamos.
        if nuevoModelo:
            self.modelo = keras.models.load_model('Modelos/modeloJirafa.h5')
        else: #Creamos el modelo.
            # Declaramos las capas de la red.
            self.modelo = keras.Sequential([
            keras.layers.Flatten(input_shape=(50, 50,1)), #Dimensiones de la imagen declaradas en preproceso.
            keras.layers.Dense(128, activation=tf.nn.relu), #128 nodos
            keras.layers.Dense(2, activation=tf.nn.softmax) #2 etiquetas
            ])
            # Compilar el modelo con algunos parametros basicos
            self.modelo.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    #Entrena el modelo y lo guarda en un archivo .h5
    def entrenaYGuarda(self):
        '''
        Entrena a la red 20 veces y lo guarda en Modelos/modeloJirafa.h5.
        '''
        self.modelo.fit(self.IMAGENES, self.ETIQUETAS, epochs=20) #ejecuta el entrenamiento 20 veces.
        self.modelo.save('Modelos/modeloJirafa.h5') #guarda el modelo en esa ruta.

#Entrenamos la red y la guardamos.
# c = Convulocional(True)
# c.entrenaYGuarda()
#%%
