import numpy as np 
import pandas as pd 
dataset = pd.read_csv('Social_Network_Ads.csv') 
X = dataset.iloc[:, 1:4] 
y = dataset.iloc[:, 4] 

from sklearn.preprocessing import OrdinalEncoder 
encoder = OrdinalEncoder() 
X = encoder.fit_transform(X) 

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1000) 

from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test) 

from sklearn.svm import SVC 
classifier = SVC(kernel = 'linear', random_state = 0) 
classifier.fit(X_train, y_train) 
y_pred = classifier.predict(X_test) 

from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test, y_pred)


## Save model in pickle files 
import pickle 
filename = 'Encoder.sav' 
pickle.dump(encoder, open(filename, 'wb')) 

filename = 'Scaler.sav' 
pickle.dump(scaler, open(filename, 'wb')) 

filename = 'Prediction.sav' 
pickle.dump(classifier, open(filename, 'wb'))