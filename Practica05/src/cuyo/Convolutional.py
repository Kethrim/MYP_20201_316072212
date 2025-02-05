#%%
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pickle

class Convolutional(object):
    def __init__(self, newModel = False):
        self.IMAGENES = pickle.load(open("X.pickle", "rb"))
        self.ETIQUETAS = np.array(pickle.load(open("Y.pickle", "rb")))

        if newModel:
            self.model = keras.models.load_model('modelos/modeloCuyo.h5')
        else:
            # Declaramos las capas de la red
            self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(50, 50)),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(2, activation=tf.nn.softmax)
            ])

            # Compilar el modelo con algunos parametros basicos
            self.model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    def entrena(self):
        self.model.fit(self.IMAGENES, self.ETIQUETAS, epochs=50)

    def guarda_modelo(self):
        self.model.save('modelos/modeloCuyo.h5')

c = Convolutional(True)
c.entrena()
c.guarda_modelo()
#%%
