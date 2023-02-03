#!/usr/bin/env python
# coding: utf-8

# In[1]:


L=[1,4,2.3,"mehu"]


# In[3]:


L[3]


# In[4]:


L[2:4]


# In[5]:


L[0:]


# In[6]:


L[:3]


# In[7]:


L[::-1]


# In[8]:


a=[1,4,1,1,6,4,1,2]


# In[9]:


len(a)


# In[10]:


a.count(1)


# In[11]:


a.append(8)


# In[12]:


a


# In[13]:


a.extend([2,3,4,5])


# In[14]:


a


# In[15]:


a.remove(1)


# In[16]:


a


# In[20]:


a.pop(4)


# In[21]:


a


# In[24]:


a.reverse()


# In[25]:


a


# In[26]:


a.insert(2,3)


# In[27]:


a


# In[33]:


#1.create a list with 10 items print the elements one by one 


# In[34]:


#2.create a list with 5 float numbers find and display sum and average of list


# In[35]:


#3. after creating a list with 6 elements from the user extract only even numbers and print


# In[42]:


#1 
l1=[1,2,3,4,5,6,7,8,9,10]


# In[44]:


l1


# In[45]:


l2=[1.2,2.5,4.3,6.5,4.7]
l2


# In[54]:


sum=0
for ele in range(0,len(l2)):
    sum = sum + l2[ele]
    lnt = len(l2)
    print("sum of elements",total)
    average = sum/lnt
    print("average of elements:",average)


# In[5]:


#3
l3=[]
l4=[]
n= int(input("enter size of a list:"))
for i in range(n):
    a=int(input())
    l3.append(a)
for j in l3:
    if j%2 == 0:
        l4.append(j)
print(l4)        
        
    


# In[ ]:




