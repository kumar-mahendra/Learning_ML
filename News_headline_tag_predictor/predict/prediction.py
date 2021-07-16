
import load_model 
import preprocessing_input as pp_input 
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

model, tokenizer = load_model.model_parms() 

def predict_label(text) : 
    if (text == '') : 
        return 'None'
    text = pp_input.clean_sentence(text) 
    max_length = 100 
    text = tokenizer.texts_to_sequences(text)
    padded_text = pad_sequences(text,padding= 'post',maxlen = max_length, truncating='post')
    labels = { 0 : 'Health', 1 : 'India', 2 : 'Entertainment', 3 : 'Sports', 4 : 'World', 5 : 'Tech' }
    prediction = list(model.predict(padded_text)[0])
    sorted_pred = sorted(prediction,reverse=True)
    ans = ''
    for i in range(3) : 
        index = prediction.index(sorted_pred[i])
        label = labels[index]
        ans = ans + label + ' > '
    return ans[:-2]


