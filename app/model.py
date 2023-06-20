import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load pickled model and tokenizer
model = tf.keras.models.load_model("models/keras_model-0.1.0")
with open('models/keras_tokenizer-0.1.0.pkl', 'rb') as input:
    tokenizer = pickle.load(input)

def spam_predict(sms, tokenizer_proc=tokenizer, max_length=10):
    '''
    Classifies a text/sms as ham or spam
    sms: (list) input text in a list
    tokenizer_proc: (tokenizer obj) the type of tokenizer to pre-process the input text/sms
    max_length: (int, def=10) length of padding to ensure the input text/sms have the same shape
    '''
    predict_label = {0:'Ham', 1:'Spam!'}

    sms_proc = tokenizer_proc.texts_to_sequences(sms) # ensure text is in a list format 
    sms_proc = pad_sequences(sms_proc, maxlen=max_length, padding='post')
    pred = (model.predict(sms_proc) > 0.5).astype("int32").item()
    
    output = predict_label[pred]
    return output
# print(tf.__version__)