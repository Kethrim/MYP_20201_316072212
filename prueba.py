#%%
from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow y tf.keras
import tensorflow as tf
from tensorflow import keras

# Librerias de ayuda
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images.shape
test_images.shape

# plt.figure() #prepara la imagen
# plt.imshow(train_images[0]) # mostramos la imagen en el lugar n del arreglo
# plt.colorbar() # agregamos la barra de color
# plt.grid(False)
# plt.show() # mostrar la imagen en jupyter

train_images = train_images / 255.0

test_images = test_images / 255.0 #normalizar la imagen

#mostrar 25 imágenes con sus respectivas etiquetas
# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

#crear el modelo
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), #es del tamaño del arreglo
    keras.layers.Dense(128, activation='relu'), #128 nodos
    keras.layers.Dense(10, activation='softmax') #10 clases o etiquetas
])

#Cosas que ayudan durante la compilación del modelo y su entrenamiento
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Entrenar el modelo
#labels son etiquetas
model.fit(train_images, train_labels, epochs=20)

#Probar la red con imágenes diferentes a las que teníamos (las del test) y ver que tan eficiente es
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# print('\nTest accuracy:', test_acc)

#Hacemos predicciones sobre las imágenes de prueba
predictions = model.predict(test_images)
np.argmax(predictions[0]) #tomar el nodo con mayor prob
#%%