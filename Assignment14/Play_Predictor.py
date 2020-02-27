import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def PlayPredictor(data_path):

    #Step1: Load Data
    data = pd.read_csv(data_path,index_col = 0)
    print("Size of actual dataset",len(data))

    #Step2 : Clean data
    feature_names = ['Weather','Temperature']
    
    print("Names of Features :",feature_names)

    weather = data.Wether
    temperature = data.Temperature
    play = data.Play

    le = preprocessing.LabelEncoder()
    
    #converting string labels into numeric values i.e. numbers
    weather_encoded =  le.fit_transform(weather)
    print("Weather LIST")
    print(weather_encoded)
    
    #converting string labels into numeric values i.e. numbers
    temp_encoded = le.fit_transform(temperature)
    label = le.fit_transform(play)
    print("Temperature List")
    print(temp_encoded)
    print("PLAY LIST")
    print(label)
    
    #combining weather and temp into single list of tuples
    features  = list(zip(weather_encoded,temp_encoded))
    
    #Step3 : Train Data
    model = KNeighborsClassifier(n_neighbors = 3)

    #Train model using training dataset
    model.fit(features,label)
    
    #Test data
    print("Predicted Data")
    predicted = model.predict([[0,2]])
    print(predicted)
    
def  main():
    
    print("Play predictor application using KNN algorithm")
    
    PlayPredictor('Play_Predictor.csv')

if __name__ == "__main__":
    main()
