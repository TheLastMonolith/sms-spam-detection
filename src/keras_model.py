import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

# We will use Keras' Sequential model from Tensorflow
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Embedding
from tensorflow.keras.callbacks import EarlyStopping

data = pd.read_csv('../data/raw/SMSSpamCollection', sep='\t', names=['label', 'message'])

# data cleaning
import html
# Define a function to decode HTML entities
def decode_html_entities(text):
    return html.unescape(text)
data['message'] = data['message'].apply(decode_html_entities)

# label encoder
data['label'] = data['label'].map( {'spam': 1, 'ham': 0} )

# train-test split
X = data['message'].values
y = data['label'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# feature engineering and pre-processing
# prepare tokenizer
t = Tokenizer()
t.fit_on_texts(X_train)

# integer encode the documents
encoded_train = t.texts_to_sequences(X_train)
encoded_test = t.texts_to_sequences(X_test)

vocab_size = len(t.word_index) + 1

# pad documents to a max length of 10 words
max_length = 10
padded_train = pad_sequences(encoded_train, maxlen=max_length, padding='post')
padded_test = pad_sequences(encoded_test, maxlen=max_length, padding='post')

# define the model
model = Sequential()
model.add(Embedding(vocab_size, 30, input_length=max_length))
model.add(Flatten())
model.add(Dense(500, activation='relu'))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# model fitting
early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)

# fit the model
model.fit(x=padded_train,
          y=y_train,
          epochs=50,
          validation_data=(padded_test, y_test), verbose=1,
          callbacks=[early_stop]
          )

# save the model
model.save("../models/keras_model-0.1.0")

# save the tokenizer (pre-processing step)
with open('../models/keras_tokenizer-0.1.0.pkl', 'wb') as output:
   pickle.dump(t, output, pickle.HIGHEST_PROTOCOL)