import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D,Flatten,Dense,Dropout,Dense,Activation,MaxPooling2D
from keras.losses import categorical_crossentropy


train_dir = '/home/ekta3501/pyproject/dataset/images/train'

#hyperparameters
HEIGHT = 48
WIDTH = 48
SAMPLES = 394*3
EPOCHS = 30
BATCH_SIZE =5
INPUT_SHAPE = (HEIGHT,WIDTH,3)


#creating first layer
model = Sequential()

model.add(Conv2D(32,(3,3),input_shape=INPUT_SHAPE))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(3))
model.add(Activation('sigmoid'))



model.compile(loss = "mean_squared_error",
               optimizer = Adam(),
               metrics=['accuracy'],)

train_data_gen = ImageDataGenerator(
        rescale = 1./255,
        shear_range =0.2,
        zoom_range =0.2,
        horizontal_flip= True,
)

training_generator = train_data_gen.flow_from_directory(
              train_dir,
              target_size = (WIDTH,HEIGHT),
              batch_size= BATCH_SIZE,
               class_mode = "categorical",
)

print(training_generator.class_indices)

model.fit_generator(training_generator,
          epochs=EPOCHS,
          steps_per_epoch=SAMPLES//BATCH_SIZE,
          verbose =1,
          # epochs=EPOCHS
          )
#

model.save('model1_2_9.h5')
