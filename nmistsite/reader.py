import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train[0].shape)
#
# Стандартизация входных данных
x_train = x_train / 255
x_test = x_test / 255

# Преобразование выходных значений в векторы по категориям

y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

# Формирование структуры нейронной сети

model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
# print(model.summary())

# Компиляция нейронной сети с оптимизацией по Adam
# и критерием - категориальная кросс-энтропия

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# history = model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)
history = model.fit(x_train, y_train_cat, epochs=8, verbose=0)
results = model.evaluate(x_test, y_test_cat)
# plt.plot(history.history['loss'])
# plt.grid(True)
# plt.show()
# plt.savefig("mygraph1.png")


model.save("my_model")


# def raspoznavanie(arr):
#     x = np.expand_dims(arr, axis=0)
#     res = model.predict(x)
#     return res
#
#
# raspoznavanie(x_test[1])
