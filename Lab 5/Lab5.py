#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9,20.1]


# In[3]:


C = np.array(cvalues)


# In[4]:


print(cvalues)


# In[5]:


print(type(cvalues))


# In[6]:


print(C)


# In[7]:


print(type(C))


# In[8]:


F = C * 9/5 + 32
print(F)


# In[9]:


A = np.array([[1,2,3],[4,5,6]])


# In[10]:


print(A)


# In[11]:


print(A.shape)


# In[12]:


B = np.array([[7,8,9],[10,11,12]])
print(B)


# In[13]:


print(B.shape)


# In[14]:


C = A + B
print(C)


# In[15]:


print(C.shape)


# In[16]:


a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])


# In[17]:


b = a[:,0:2]


# In[18]:


print(b)


# In[19]:


print(a[0,0])


# In[20]:


print(a)


# In[21]:


a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)


# In[22]:


print(a[bool_idx])


# In[23]:


print(a[a > 2])


# In[24]:


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)


# In[25]:


print(x + y)


# In[26]:


print(np.add(x, y))


# In[27]:


print(x - y)


# In[28]:


print(np.subtract(x, y))


# In[29]:


print(x * y)


# In[30]:


print(np.multiply(x, y))


# In[31]:


print(x / y)


# In[32]:


print(np.divide(x, y))


# In[33]:


print(np.sqrt(x))


# In[34]:


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
v = np.array([9,10])
w = np.array([11, 12])


# In[35]:


print(v.dot(w))


# In[36]:


print(np.dot(v, w))


# In[37]:


print(x.dot(v))


# In[38]:


print(np.dot(x, v))


# In[39]:


print(x.dot(y))


# In[40]:


print(np.dot(x, y))


# In[41]:


x = np.array([[1,2],[3,4]])
print(np.sum(x))


# In[42]:


print(np.sum(x, axis=0))


# In[43]:


print(np.sum(x, axis=1))


# In[44]:


data1 = np.arange(1.5)
print(np.average(data1))


# In[45]:


data2 = np.arange(6).reshape(3,2)
print(data2)


# In[46]:


print(np.average(data2, axis = 0))


# In[47]:


print(np.average(data2, axis = 1))


# In[48]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)


# In[49]:


for i in range(4):
    y[i, :] = x[i, :] + v


# In[50]:


print(y)


# In[51]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))
y = x + vv
print(y)


# In[52]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print(y)


# In[57]:


np.zeros(5)


# In[58]:


np.zeros((2,3))


# In[59]:


np.random.rand(2,3)


# In[60]:


np.full((2,2),7)


# In[61]:


np.eye(3)


# In[62]:


np.arange(2,10,2)


# In[63]:


np.linspace(0,1,5)


# In[64]:


a = np.array([3,6,9,12])


# In[65]:


np.reshape(a,(2,2))


# In[70]:


a = np.ones((2,2))
print(a)


# In[71]:


b = a.flatten()
print(b)


# In[72]:


a = np.array([[1,2,3],[4,5,6]])
print(a)


# In[73]:


b = np.transpose(a)
print(b)


# In[74]:


import matplotlib.pyplot as plt


# In[75]:


x = np.array([1,2,3])
y = np.array([2,4,1])


# In[76]:


plt.plot(x, y)


# In[77]:


plt.xlabel('x - axis')
plt.ylabel('y - axis')


# In[78]:


plt.title('My first graph!')


# In[79]:


plt.show()


# In[80]:


import matplotlib.pyplot as plt


# In[81]:


left = [1, 2, 3, 4, 5]


# In[82]:


height = [10, 24, 36, 40, 5]
tick_label = ['one', 'two', 'three', 'four', 'five']


# In[83]:


plt.bar(left, height, tick_label = tick_label, width = 0.8, color =['red', 'green'])


# In[84]:


plt.xlabel('x - axis')
plt.ylabel('y - axis')


# In[85]:


plt.title('My bar chart!')


# In[86]:


plt.show()


# In[ ]:




