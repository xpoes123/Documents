import tensorflow as tf
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "File Directory towards our Training data"
Train_data = open("File Directory Towards our Training Data (Not found yet)")
#Node reference
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

#Amount of attemps
batch_size = 100

#place holders to confirm later
x = tf.placeholder('float')
y = tf.placeholder('float')

#Running our session, might be put later? Not sure where this goes
with tf.Session as sess:
    sess.run(tf.global_variables())


#Attempt at creating layers
def neural_network_model(data):
    x = 1000 #not yet decided, and I have no idea...
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([x, n_nodes_hl1])),
                       'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                    'biases': tf.Variable(tf.random_normal([n_classes]))}

    # (input_data *weights)+biases

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights'])+ output_layer['biases']

    return output


#Our training progress
def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, #Static, doesnt currently do anything
                                                                 labels = y))
    optimizer = tf.train.AdamOptimizer().minimize(cost) #Training thingything




