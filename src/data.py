import numpy as np
import keras.datasets.mnist as mnist
from keras.utils import to_categorical

def load_data():
    (train_x, train_y), (test_x, test_y) = mnist.load_data()

    # Normalización y reshape
    train_x = train_x.reshape(60000, 28*28).astype('float32') / 255
    test_x = test_x.reshape(10000, 28*28).astype('float32') / 255

    # Convertir etiquetas a one-hot encoding
    train_y = to_categorical(train_y, 10)
    test_y = to_categorical(test_y, 10)

    return train_x, train_y, test_x, test_y
