from sklearn.datasets import load_iris;

iris = load_iris();

print("Feature names of iris dataset");
print(iris.feature_names);

print("Target names of dataset");
print(iris.target_names);

print("First 10 elements od dataset");

for i in range(10):
    print("ID :%d , Label: %s , Feature : %s"%(i,iris.data[i],iris.target[i]));