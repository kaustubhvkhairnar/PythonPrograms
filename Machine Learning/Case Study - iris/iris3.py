import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import numpy as np;


from sklearn import tree;
from sklearn.datasets import load_iris;

iris = load_iris();

print("Feature names of iris dataset");
print(iris.feature_names);

print("Target names of dataset");
print(iris.target_names);


test_index = [1,51,101];

train_target = np.delete(iris.target,test_index);
train_data = np.delete(iris.data,test_index,axis = 0);

test_target = iris.target[test_index];
test_data = iris.data[test_index];

clf = tree.DecisionTreeClassifier();

clf = clf.fit(train_data,train_target);

print("Values that removed");
print(test_target);

print("Result of testing");
print(clf.predict(test_data));

from six import StringIO;
import pydotplus;

dot_data = StringIO();
tree.export_graphviz(clf,out_file = dot_data,feature_names = iris.feature_names,class_names = iris.target_names,filled = True,rounded = True,impurity = False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue());

graph.write_pdf("DecisionTreeIRIS.pdf");




















