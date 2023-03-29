#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image


# In[6]:


# load the saved model
model = tf.keras.models.load_model('accident_detection_model.h5')

# define a function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.
    return img


# In[7]:


# define a function to classify the image
def classify_image(img_path):
    img = preprocess_image(img_path)
    prediction = model.predict(img)
    if prediction < 0.5:
        str=('accident')
    else:
        str=('no accident')
    return str


# In[ ]:



img_path = "C:/Users/Sarthak/Documents/Hackathon/Data/data/test/Accident/test_33.jpg"
prediction = classify_image(img_path)
print(prediction)


# ALERT SENDING USING TWILIO:
# Send an aleert if the image obtained is of a crash 

# In[12]:


get_ipython().system('pip install twilio')


# In[24]:


from twilio.rest import Client


# In[25]:


account_sid = 'ACf57831fde3da312ce7f861199ecc9faf'
auth_token = '66b7afcd7b25911e3187856caefc6af1'
client = Client(account_sid, auth_token)


# In[26]:


message_body="A motor accident is detected on the highway! Provide assistance"
sender=+14346239445
receiver =+919986903880


# In[36]:


print(prediction)


# In[37]:


if prediction=='accident':
    message = client.messages.create(
                                  from_=sender,
                                  body =message_body,
                                  to =receiver
                              )
  
print(message.sid)


# message = client.messages.create(
#                               from_='+15017122661',
#                               body ='body',
#                               to ='+15558675310'
#                           )
#   
# print(message.sid)

# In[ ]:




