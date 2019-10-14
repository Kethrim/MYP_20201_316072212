#%%

import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle

#Clase necesaria para entrenar el modelo de la red neuronal
class Convulutional(object):
    def __init__(self):
        """ Inicializa las variables necesarias para poder entrenar el modelo, 
            obtendra las imagenes ya procesadas del archivo X.pickle y las almacenara en self.pictures,
            asi mismo tambien obtiene sus etiquetas contenidas en Y.pickle y las almacena en self.labels
        """
        self.pictures = pickle.load(open("X.pickle", "rb"))
        self.labels = pickle.load(open("Y.pickle", "rb"))
        # Declaracion de las capas de la modelo
        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(50, 50,1)),
            keras.layers.Dense(128, activation=tf.nn.relu), #128 nodos
            keras.layers.Dense(2, activation=tf.nn.softmax) #2 etiquetas
            ])

        # Compila el modelo
        self.model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])
    #Entrena el modelo
    def Training(self):
        """ Entrenara al modelo con la imagenes preprocesadas contenidas en self.pictures,
             y con sus etiquetas contenidas en sel.labels, el proceso lo realizara un total de 200 veces
        """
        self.model.fit(self.pictures,np.array(self.labels), epochs=200)
        self.model.save('hippo_model.h5')

    

#%%
