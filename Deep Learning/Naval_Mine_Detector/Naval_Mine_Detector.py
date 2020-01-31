import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore',category=RuntimeWarning)
import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


###################################################
#                                           read_dataset FUNCTION                                                   #
###################################################	
#Reading the dataset
def read_dataset():
	df = pd.read_csv("sonar.csv");
	print("Data loaded successfully")
	
	#Features
	X = df[df.columns[0:60]].values
	
	#Labels
	y = df[df.columns[60]]
	
	encoder = LabelEncoder()
	
	encoder.fit(y)
	y = 	encoder.transform(y)
	Y = one_hot_encode(y)

	return (X,Y)
###################################################
#                                     one_hot_encode FUNCTION                                                    #
###################################################	
def one_hot_encode(labels):
    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode = np.zeros((n_labels,n_unique_labels))
    one_hot_encode[np.arange(n_labels),labels] = 1
    return one_hot_encode

###################################################
#                                 multilayer_perceptron FUNCTION                                               #
###################################################	
	
# Model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activations
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with sigmoid activations
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.sigmoid(layer_2)
    # Hidden layer with sigmoid activations
    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    layer_3 = tf.nn.sigmoid(layer_3)
    # Hidden layer with RELU activations
    layer_4 = tf.add(tf.matmul(layer_3, weights['h4']), biases['b4'])
    layer_4 = tf.nn.relu(layer_4)
    # Output layer with linear activations
    out_layer = tf.matmul(layer_4, weights['out']) + biases['out']
    return out_layer

	
###################################################
#                                                   MAIN FUNCTION                                                       #
###################################################	
def main():			
	X,Y = read_dataset()
	
	#Shuffling the dataset 
	X,Y = shuffle(X,Y,random_state = 1)
	
	train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size=0.30,random_state=415)
	
	# Inspect the shape of the train and test datasets
	print("train_x.shape",train_x.shape)
	print("train_y.shape",train_y.shape)
	print("test_x.shape",test_x.shape)
	print("test_y.shape",test_y.shape)

	learning_rate = 0.3
	
	training_epochs = 1000
	
	cost_history = np.empty(shape=[1],dtype=float)
	
	n_dim = X.shape[1]
	print("Number of columns",n_dim)
	
	n_class = 2
	
	model_path = "Kaustubh"
	
	n_hidden_1 = 60
	n_hidden_2 = 60
	n_hidden_3 = 60
	n_hidden_4 = 60
	
	#Placeholder For Inputs
	x = tf.compat.v1.placeholder(tf.float32,[None,n_dim])
	#Placeholder For Outputs
	yp = tf.compat.v1.placeholder(tf.float32,[None,n_class])
	
	# Model parameters
	W = tf.Variable(tf.zeros([n_dim,n_class]))
	b = tf.Variable(tf.zeros([n_class]))

	weights = {
		'h1' : tf.Variable(tf.random.truncated_normal([n_dim,n_hidden_1])),
		'h2' : tf.Variable(tf.random.truncated_normal([n_hidden_1,n_hidden_2])),
		'h3' : tf.Variable(tf.random.truncated_normal([n_hidden_2,n_hidden_3])),
		'h4' : tf.Variable(tf.random.truncated_normal([n_hidden_3,n_hidden_4])),
		'out' : tf.Variable(tf.random.truncated_normal([n_hidden_4,n_class]))
	}
	
	biases = {
		'b1' :  tf.Variable(tf.random.truncated_normal([n_hidden_1])),
		'b2' :  tf.Variable(tf.random.truncated_normal([n_hidden_2])),
		'b3' :  tf.Variable(tf.random.truncated_normal([n_hidden_3])),
		'b4' :  tf.Variable(tf.random.truncated_normal([n_hidden_4])),
		'out' :  tf.Variable(tf.random.truncated_normal([n_class])),
	}
	
	# Initialization
	init = tf.compat.v1.global_variables_initializer()

	saver = tf.compat.v1.train.Saver()
	
	# Call your model defined
	y = multilayer_perceptron(x, weights, biases)

	# Define the cost function and optimizer
	cost_function = tf.reduce_mean(tf.compat.v2.nn.softmax_cross_entropy_with_logits(logits=y, labels=yp))
	training_step = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)

	# Launch the graph
	sess = tf.compat.v1.Session()
	sess.run(init)
	
	mse_history = []
	accuracy_history = []

	# Calculate the cost and the accuracy for each epoch
	for epoch in range(training_epochs):
		sess.run(training_step, feed_dict={x:train_x, yp:train_y})
		cost = sess.run(cost_function,feed_dict={x:train_x, yp:train_y})
		cost_history = np.append(cost_history, cost)
		correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(yp,1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		#print("Accuracy: ", (sess.run(accuracy, feed_dict={x:test_x, yp:test_y})))
		pred_y = sess.run(y,feed_dict={x:test_x} )
		mse = tf.reduce_mean(tf.square(pred_y - test_y))
		mse_ = sess.run(mse)
		accuracy = (sess.run(accuracy,feed_dict={x:train_x, yp:train_y}))
		accuracy_history.append(accuracy)
		print('epoch: ', epoch,' - ', 'cost: ', cost, " - MSE: ", mse_, "- Train Accuracy: ", accuracy)
    
	save_path = saver.save(sess, model_path)
	print("Model saved in file: %s", save_path)	
	
	plt.plot(accuracy_history)
	plt.title("ACCURACY HISTORY")
	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.show()

	plt.plot(range(len(cost_history)),cost_history)
	plt.title("LOSS CALCULATION")
	plt.axis([0,training_epochs,0,np.max(cost_history)/100])
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.show()
	
	# Print the final mean square error
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(yp, 1))
	accuracy = tf.reduce_mean(tf.square(pred_y - test_y))
	print("Test Accuracy: ", (sess.run(y, feed_dict={x:test_x, yp:test_y} )))

	# Print the final mean square error
	pred_y = sess.run(y, feed_dict={x:test_x})	
	mse = tf.reduce_mean(tf.square(pred_y- test_y))
	print("MSE: %.4f" % sess.run(mse))
	
if __name__ == "__main__":
	main()
	
	
	
