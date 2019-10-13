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
    def Training(self,pictures,labels):
        self.model.fit(pictures,labels, epochs=200)
        self.model.save('hippo_model.h5')

    

#%%
