import tensorflow as tf
from tensorflow import keras

import numpy as np
import pickle

train_data_pkl_file = open('pkl_files/train_data.pkl', 'rb')
train_label_pkl_file = open('pkl_files/train_label.pkl', 'rb')
dict_pkl_file = open('pkl_files/kodict.pkl', 'rb')

train_data = pickle.load(train_data_pkl_file)
train_label = pickle.load(train_label_pkl_file)
kodict = pickle.load(dict_pkl_file)

train_data_pkl_file.close()
train_label_pkl_file.close()
dict_pkl_file.close()

vocab_size = len(kodict)

train_data_num = 20000
partial_train_num = 13000

test_data = train_data[train_data_num:]
test_label = train_label[train_data_num:]

train_data = train_data[:train_data_num]
train_label = train_label[:train_data_num]

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value = 0, padding = 'post', maxlen = 256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value = 0, padding = 'post', maxlen = 256)

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.summary()

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='binary_crossentropy',
              metrics=['accuracy'])

x_val = train_data[partial_train_num:]
partial_x_train = train_data[:partial_train_num]

y_val = train_label[partial_train_num:]
partial_y_train = train_label[:partial_train_num]

epochs = 50

model.fit(partial_x_train,
                    partial_y_train,
                    epochs=epochs,
                    batch_size=512,
                    validation_data=(x_val, y_val),
                    verbose=1)

results = model.evaluate(test_data, test_label)

model.save('good_bad_' + str(epochs) + '_epochs.h5')

print(results)