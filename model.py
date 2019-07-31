
# coding: utf-8

# In[1]:


# Load Model


# In[11]:


import pickle
import numpy as np


# In[3]:


model_path = "finalized_model.sav"
scaler_path = "scaler_param.sav"


# In[13]:


loaded_model = pickle.load(open(model_path,'rb'))
loaded_scaler = pickle.load(open(scaler_path,'rb'))


# In[28]:


# Xc,Yc,Radius
test = np.array([[5,5,70]])
test = loaded_scaler.transform(test)
predict = loaded_model.predict(test)
predict = predict.flatten()


# In[30]:


points = []
for i in range(0,len(predict)-1,2):
    points.append((predict[i],predict[i+1]))
points


# In[31]:


import matplotlib.pyplot as plt


# In[38]:


for point in points:
    plt.plot(*point,'g.')
plt.show()


# In[41]:


# Lets test the actual Bresenhams agorithm 
import test
Xc = 5 
Yc = 5
Radius = 70
test.plotCircle(Xc,Yc,Radius)


# In[42]:


def prediction_draw(Xc,Yc,R):
    test = np.array([[5,5,70]])
    test = loaded_scaler.transform(test)
    predict = loaded_model.predict(test)
    predict = predict.flatten()
    points = []
    for i in range(0,len(predict)-1,2):
        points.append((predict[i],predict[i+1]))
    for point in points:
        plt.plot(*point,'g.')
    plt.show()
    

    

