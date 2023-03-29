#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
from tensorflow.keras.layers import Input, Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[3]:


train_datagen = ImageDataGenerator(rescale=1./255, 
                                   shear_range=0.2, 
                                   zoom_range=0.2, 
                                   horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)


# In[4]:


train_generator = train_datagen.flow_from_directory(directory='Data/data/train', 
                                                    target_size=(224, 224), 
                                                    batch_size=32, 
                                                    class_mode='binary')
test_generator = test_datagen.flow_from_directory(directory='Data/data/test', 
                                                  target_size=(224, 224), 
                                                  batch_size=32, 
                                                  class_mode='binary')


# In[5]:



# Load pre-trained VGG16 model
vgg = VGG16(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))


# In[6]:


# Add custom output layers
x = Flatten()(vgg.output)
x = Dense(256, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x)


# In[10]:


# Define model
model = Model(inputs=vgg.input, outputs=output)

# Freeze pre-trained layers
for layer in vgg.layers:
    layer.trainable = False


# In[11]:


# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[12]:


model.summary()


# In[ ]:


model.fit(train_generator, epochs=20, validation_data=test_generator)


# In[ ]:


# Save model
model.save('accident_detection_model.h5')


# In[ ]:




