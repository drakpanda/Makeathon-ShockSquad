#!/usr/bin/env python
# coding: utf-8

# In[22]:


import tensorflow as tf
from tensorflow.keras.layers import Input, Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[23]:


train_datagen = ImageDataGenerator(rescale=1./255, 
                                   shear_range=0.2, 
                                   zoom_range=0.2, 
                                   horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)


# In[24]:


train_generator = train_datagen.flow_from_directory(directory='Data_road/train', 
                                                    target_size=(224, 224), 
                                                    batch_size=32, 
                                                    class_mode='binary')
test_generator = test_datagen.flow_from_directory(directory='Data_road/test', 
                                                  target_size=(224, 224), 
                                                  batch_size=32, 
                                                  class_mode='binary')


# In[25]:



# Load pre-trained VGG16 model
vgg = VGG16(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))


# In[26]:


# Add custom output layers
x = Flatten()(vgg.output)
x = Dense(256, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x)


# In[27]:


# Define model
model = Model(inputs=vgg.input, outputs=output)

# Freeze pre-trained layers
for layer in vgg.layers:
    layer.trainable = False


# In[28]:


# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[29]:


model.summary()


# In[31]:


model.fit(train_generator, epochs=10, validation_data=test_generator)


# In[32]:


# Save model
model.save('road_obstacle_model.h5')


# In[ ]:




