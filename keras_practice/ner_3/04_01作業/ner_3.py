# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:25:17 2020

@author: User
"""

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

import matplotlib.pyplot as plt, numpy as np

from keras import losses
import torch
import torch.nn.functional as F
from keras.models import Sequential
import numpy as np

from keras.layers.core import Dense
x_test=np.ones((len(range(0,44000,1)),1))
y_test=np.ones((len(range(0,44000,1)),1))


for i in range(0,44000,1):
    p=(i-2000)/1000
    x_test[i]=p
    y_test[i]=1+np.sin(np.pi/4*p)
        
plt.figure(figsize=(8,8))
plt.plot(x_test,y_test,'g')
plt.show()

x_test2=np.ones((len(range(0,44000,1)),1))
y_test2=np.ones((len(range(0,44000,1)),1))


for i in range(0,44000,1):
    p=(i-2000)/1000
    x_test2[i]=p
    y_test2[i]=1+np.sin(np.pi/4*p)
        
plt.figure(figsize=(8,8))
plt.plot(x_test2,y_test2,'g')
plt.show()


model1 = Sequential()
model1.add(Dense(1024,input_dim=1,activation='sigmoid'))
model1.add(Dense(512,activation='sigmoid'))
model1.add(Dense(256,activation='sigmoid'))
model1.add(Dense(1,activation='linear'))
model1.compile(loss=losses.mean_squared_error, optimizer='adam')
model1.fit(x_test,y_test,batch_size=128,epochs=64)
loss=model1.evaluate(x_test,y_test)
print("\nloss: %.10f" %(loss))
y_pred=model1.predict(x_test2)

plt.figure(figsize=(8,8))
plt.plot(x_test,y_test,'g',x_test2,y_pred,'r-.')
plt.show()
