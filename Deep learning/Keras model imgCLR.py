from keras import backend as K
from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense
from keras.utils.vis_utils import plot_model

model = Sequential()

model.add(Dense(10, input_dim=4, activation=K.tanh))
model.add(Dense(8, activation=K.tanh))
model.add(Dense(6, activation=K.tanh))
model.add(Dense(4, activation=K.softmax))



model.compile(SGD( lr=0.1), loss = 'categorical_crossentropy', 
              metrics=['accuracy']
              )

model.summary

#plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
