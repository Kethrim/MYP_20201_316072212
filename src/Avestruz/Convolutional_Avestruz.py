#Librerias Importantes
import tensorflow as tf
from tensorflow import keras

#Librerias Auxiliares
import numpy as np
import matplotlib.pyplot as plt
import pickle

class Convolutional_Avestruz(object):
    """Clase para entrenar el modelo de la Red"""
    def __init__(self, newModel = False):
        """Metodo contructor que incializa las imagenes vectorizadas"""
        self.IMAGENES = pickle.load(open("../Imagenes y Etiquetas/X.pickle", "rb"))
        self.ETIQUETAS = pickle.load(open("../Imagenes y Etiquetas/Y.pickle", "rb"))
        
        #Condicion por si existe un modelo anterior, esto para mejorarlo y no crear otro
        if newModel:
            self.model = keras.models.load_model('../../modelos/Modelo_Avestruz.h5')
        else:
            # Declaramos las capas de la red
            self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(50, 50,1)),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax)
            ])

            # Compilar el modelo con algunos parametros basicos
            self.model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    def entrena(self):
        """Metodo para entrenar la clase y guardar el modelo en un archivo .h5"""
        self.model.fit(self.IMAGENES, self.ETIQUETAS, epochs=100)
        self.model.save('../../modelos/Modelo_Avestruz.h5')