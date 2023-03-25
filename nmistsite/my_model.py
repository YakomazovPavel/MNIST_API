import os
import numpy as np
from tensorflow import keras

# from tensorflow.keras.datasets import mnist
# import matplotlib.pyplot as plt

# if __name__ == '__main__':
#     os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#     model = keras.models.load_model("my_model")
#     print('')



# Преобразование в массив NUMPY
def nparray_list(x: list):
    y = np.zeros(shape=(28, 28))
    for nomer_stroki in range(0, 28):
        for nomer_kletki_v_stroke in range(0, 28):
            y[nomer_stroki][nomer_kletki_v_stroke] = x[nomer_stroki][nomer_kletki_v_stroke]
    return y


def raspoznavanie(x):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    model = keras.models.load_model("my_model")
    y = np.expand_dims(x, axis=0)
    # print(y.shape)
    res = model.predict(y)
    return res