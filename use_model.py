from PIL import Image
from tensorflow import keras
import random
from tensorflow.keras import layers
import tensorflow as tf
import os
import numpy as np

def foto_to_vec():
    image = Image.open('dataset_numbers\\numbers\\2\\dan2.jpg').convert('L')
    data = np.asarray(image).astype('float32')
    return data

model = keras.models.load_model('model_bleh')
zero_matrix = np.zeros((1,24,24))

data = foto_to_vec()
data = np.expand_dims(data, axis=0)
x = model.predict(data)


print(x)