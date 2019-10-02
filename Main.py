#%%
from matplotlib import pyplot as plt 
from tensorflow import keras
from keras.preprocessing import image

import Preprocess
import os
import cv2
import numpy as np
import pickle

#Here i load the model
model = keras.models.load_model('model.h5')

train_images = pickle.load(open("X.pickle", "rb"))
train_labels = pickle.load(open("Y.pickle", "rb"))

i = 1
predictions = model.predict(train_images)
max = np.argmax(predictions[i])
cat = ["Hola!, soy un cuyo c:","No soy un cuyo :c"]
result = cat[max]

plt.figure()
plt.title(result)
plt.imshow(np.array(train_images).reshape(-1,50,50)[i])
plt.colorbar()
plt.grid(False)
plt.show()
    #plt.savefig(img+".png")


#%%
