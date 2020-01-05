from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
def WinePredictor():
    wine = datasets.load_wine()
    
    print("Features")
    print(wine.feature_names)
    
    print("Targets(Species Label)")
    print(wine.target_names)
    
    print("First 5 Records")
    print(wine.data[0:5])
    
    print("Wine Labels")
    print(wine.target)
    
    #To split the data in two sets as :
    #70%  = Training & 30% = Testing
    X_train,X_test,y_train,y_test = train_test_split(wine.data,wine.target,test_size = 0.3) 
    
    #Creating KNN classifier
    knn = KNeighborsClassifier(n_neighbors = 3)
    
    #Training
    knn.fit(X_train,y_train)
    
    #Prediction for test dataset
    y_pred = knn.predict(X_test)
    
    #Accuracy
    print("Accuracy",metrics.accuracy_score(y_test,y_pred))
    
if __name__ == "__main__":
    WinePredictor()