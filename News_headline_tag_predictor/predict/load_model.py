from json import load
from keras.models import model_from_json
import pickle 
    
def model_parms() : 
    #load model 
    json_file = open('model/model.json','r') 
    loaded_model = json_file.read() 
    loaded_model = model_from_json(loaded_model)
    json_file.close() 

    #load model weights 
    loaded_model.load_weights("model/model.h5")
    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics='accuracy')
    
    #load tokenizer 
    tokenizer = None 
    with open(r'model/tokenizer.pickle','rb') as handle : 
        tokenizer = pickle.load(handle)

    model = loaded_model 
    
    return model, tokenizer 



