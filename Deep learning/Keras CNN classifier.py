from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

classifier = Sequential()
#first cnn layer
classifier.add(Conv2D(16, (2,2), 
                      input_shape= (64, 64, 3), 
                      activation = 'relu'))
classifier.add(MaxPooling2D(pool_size =(2,2)))

#second cnn layer
classifier.add(Conv2D(16, (2,2),
                      activation = 'relu'))
classifier.add(MaxPooling2D(pool_size =(1,1)))


#flattening
classifier.add(Flatten())

#connections
classifier.add(Dense(128, activation = 'relu'))
classifier.add(Dense(1, activation = 'sigmoid'))


#compile layers
classifier.compile(optimizer='adam', 
                   loss='binary_crossentropy', 
                   metrics =['accuracy'])

TR_Data = ImageDataGenerator(1./255, 
                             shear_range=.2, 
                             zoom_range=.2, 
                             horizontal_flip=True)

TS_Data = ImageDataGenerator(1./255)

train_set= TR_Data.flow_from_directory ('D:/programs/AI/Datasets/MahmoudTR',
                                       target_size= (64, 64),
                                       batch_size= 2,
                                       class_mode= 'binary')

test_set= TS_Data.flow_from_directory ("D:/programs/AI/Datasets/test",
                                       target_size= (64, 64),
                                       batch_size= 2,
                                       class_mode= 'binary')

classifier.fit_generator(train_set, 
                         steps_per_epoch=5, 
                         epochs = 2,
                         validation_data=test_set,
                         validation_steps=500)

import numpy as np
from tensorflow.keras.preprocessing import image

predict_image = TS_Data.flow_from_directory('D:/programs/AI/Datasets/predict',
                                         target_size= (64, 64))


predict_image = image.img_to_array(predict_image)
predict_image = np.expand_dims(predict_image, axis= 0)

predict = classifier.predict(predict_image)

TR_Data.class_indices

if predict == 1:
    prediction = 'mahmoud'
else:
    prediction = 'nothing'
    
print(prediction)

# serialize model to JSON
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("model.h5")
print("Saved model to disk")

classifier.save('D:/programs')