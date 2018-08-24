import os

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pickle
from konlpy.tag import Komoran

komoran = Komoran()

pkl_file = open('pkl_files/kodict.pkl', 'rb')
kodict = pickle.load(pkl_file)
pkl_file.close()
kodict_size = len(kodict)

epochs = 50

model = keras.models.load_model('good_bad_' + str(epochs) + '_epochs.h5')

model.summary()

with open('prediction_input.txt', encoding = 'utf-8') as p_input:
    input_lines = p_input.readlines()
p_input.close()

prediction_input = []

for line in input_lines:
    p_list = []
    morph_list = komoran.morphs(line)
    for m in morph_list:
        if m in kodict:
            p_list.append(kodict[m])
    prediction_input.append(p_list)

prediction_input = keras.preprocessing.sequence.pad_sequences(prediction_input, value = 0, padding = 'post', maxlen = 256)

prediction = model.predict_classes(prediction_input)

for i in range(len(prediction)):
    print(input_lines[i])
    if(prediction[i] == 1):
        print("GOOD")
    else:
        print("BAD")
    print("*"*80)