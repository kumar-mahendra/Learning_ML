# Step-1 Import required libaries

import pandas as pd
import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Step-2 : load dataset
dataset = pd.read_csv('newsfile.csv')
dataset.drop_duplicates(keep="first",inplace=True)            # remove duplicates
news_dataset = dataset.sample(30000)  #randomly select 5000 rows
training_data,testing_data =  train_test_split(news_dataset,test_size=0.3)   # 70/30 train-test split

# # plotting categories vs their count
# categories = training_data['news_category'].unique()
# cat_counts = dict.fromkeys(categories,0)

# for t in training_data['news_category'] :
#     cat_counts[t] +=1 
# # plt.plot(categories,cat_counts.values())                     # Avoid Plotting As long as it is not necessary
# # plt.show()

# # print(cat_counts.values())
# plt.bar(categories,cat_counts.values())
# plt.title('Training Data Distribution')
# plt.show()

# categories2 = testing_data['news_category'].unique()
# cat_counts2 = dict.fromkeys(categories,0)

# for t in training_data['news_category'] :
#     cat_counts2[t] +=1 

# # print(cat_counts2.values())
# plt.bar(categories2,cat_counts2.values())
# plt.title('Testing Data Distribution')
# plt.show()


#  Global variables 
epochs = 25
max_len = 100
embd_size = 6


# Step-3 : Tokenization 
def tokenization_(training_headings, testing_headings, max_length=max_len,vocab_size = 5000):
    tokenizer = Tokenizer(num_words = vocab_size, oov_token= '<oov>')
    #Tokenization and padding

    tokenizer.fit_on_texts(training_headings)
    word_index = tokenizer.word_index
    training_sequences = tokenizer.texts_to_sequences(training_headings)
    training_padded = pad_sequences(training_sequences,padding= 'post',maxlen = max_length, truncating='post')


    testing_sequences = tokenizer.texts_to_sequences(testing_headings)
    testing_padded = pad_sequences(testing_sequences,padding= 'post',maxlen = max_length, truncating='post')

    return tokenizer,training_padded,testing_padded

# Step 4 : make X_train, Y_train, X_test, Y_test
tokenizer,X_train,X_test = tokenization_(training_data['news_headline'], testing_data['news_headline'])
labels = {  
            'health':[1,0,0,0,0,0],'india':[0,1,0,0,0,0],'entertainment':[0,0,1,0,0,0],
            'sports':[0,0,0,1,0,0],'world':[0,0,0,0,1,0],     'tech'    :[0,0,0,0,0,1]   
         }
Y_train = np.array([labels[y] for y in training_data['news_category']]) 
Y_test = np.array([labels[y] for y in testing_data['news_category'] ])

## Step-5 : Build Neural network Model

def build_model( n, vocab_size, embedding_size):   #n = length of each input vector 

    #Sequential model 
    model = tf.keras.models.Sequential()

    # Implementing word-embeddings
    model.add(tf.keras.layers.Embedding(vocab_size,embedding_size, input_length=n))

    model.add(tf.keras.layers.GlobalAveragePooling1D()) 

    # model.add(tf.keras.layers.Dense(100,activation='relu'))

    #output layer
    model.add(tf.keras.layers.Dense(6,activation = 'softmax'))  # since, 6 possible tags as outcome are possible

    #compile the model
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics='accuracy')

    #model summary
    print(model.summary())              

    return model
  
model = build_model(max_len,7000,embd_size)

# Step-6 : Train model
history = model.fit(X_train,Y_train,
                    validation_data = (X_test,Y_test),
                    epochs = epochs)



# Saving the model in HDF5 file format 
model.save('model.h5')

print("\n*******************   MODEL SAVED TO DISK SUCCESSFULLY.  ******************************")

# Plotting the output 
plt.style.use('ggplot')

## Plotting validation vs testing data accuracy and loss

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()


loss, accuracy = model.evaluate(X_train,Y_train, verbose=False)
print("Training Accuracy: {:.4f}".format(accuracy))
loss, accuracy = model.evaluate(X_test,Y_test, verbose=False)
print("Testing Accuracy:  {:.4f}".format(accuracy))
plot_history(history)



