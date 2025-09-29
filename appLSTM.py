## Importing Lib's
import pickle
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

## Loading Models
model=load_model('next_word_LSTM.h5')

## Loading Tokenizer
with open('token.pickle','rb') as handle:
    token = pickle.load(handle)

## Function to Predict Next Word
def predict_next_word(model, token, text, max_seq_len):
    token_list = token.texts_to_sequences([text])[0]
    if len(token_list) >= max_seq_len:
        token_list = token_list[-(max_seq_len-1):]
    token_list = pad_sequences([token_list],padding='pre',maxlen=max_seq_len-1)
    predicted = model.predict(token_list,verbose=0)
    predicted_word_index = np.argmax(predicted,axis=1)
    for word,index in token.word_index.items():
        if index == predicted_word_index :
            return word
    return None

## Stremlit App
st.title("Next Word Prediction With LSTM RNN")
input_text =  st.text_input("Enter the sequence of Words","To be or not to")
if st.button("Predict Next Word"):
    max_seq_len = model.input_shape[1] + 1
    next_word = predict_next_word(model=model, token=token, text=input_text, max_seq_len=max_seq_len)
    st.write(f"Next Word Predicted : {next_word}")

