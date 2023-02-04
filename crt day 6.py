#!/usr/bin/env python
# coding: utf-8

# In[1]:


#exceptions and exception handling
#the user doesnt want interruption or disturbance in the program flow. to achieve this we use exception handling.


# In[7]:


a=10
b=0
try:     #this may have error so try
    a/b
except Exception as e:
    print("number cannot be divided by zero")

    print("end")  


# In[14]:


a=20
b=0
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("number cannot be zero",e)
finally:
    print("resource closed")


# In[11]:


a=10  #for specific eroors only the specific exception blocks will be executed
try:
    b=int(input("enter the number:"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("number cannot be divided by zero")
except Valueerror as e:
    print("invalid input",e)
except Exception as e: #if not from any of the above errors
    print("other error",e)
finally:
    print("resource closed")
    


# In[18]:


x=int(input("enter a number:"))
if x%2!=0:
    raise Exception("x should be an even number")
else:
    print("x is an even number,correct")


# In[19]:


#oops - its an efficient concept used in all objct oriented programming languages lyk java nd python.for multiple
#reasons we use oops concepts for ex- code reusability,data security,hiding data
# Class - it's a blueprint. ex-birds,laptops,etc
# object - it's a thing created based on class.
# note- one class can have multiple objects.
# example - birds(class)
#            parrots,peacocks,dove,etc(object)
#           laptops (class)
#            dell,hp,lenovo,etc(object)


# In[20]:


class computer:
    def config(self):
        print("yes")
lenovo=computer()
lenovo.config()

dell=computer()
dell.config()


# In[22]:


#constructor

class employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("id : %d \nName:%s"% (self.id,self.name))
        
emp1 = employee("john",101)    
emp2 = employee("david",102)

emp1.display()
emp2.display()


# In[25]:


class computer():
    a=10
    b=20
    print("class variable inside class")
    def config(self):
        c=100
        print("yes")
        print("instance access",self.b)
lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)
lenovo.config


# In[ ]:




