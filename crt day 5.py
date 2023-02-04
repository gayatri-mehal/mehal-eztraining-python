#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as r


# In[2]:


x = 'i luv sweets'


# In[15]:


print(r.sample(x,2))


# In[5]:


a = [1,2,3,4,5,6]


# In[6]:


r.shuffle(a)


# In[14]:


print(a)


# In[10]:


b = "welcome back"


# In[18]:


print(r.choice(b))


# In[19]:


A=r.random() #will return any num from 0.0 to 1.0 , 0.0 includes nd 1.0 exc


# In[20]:


A


# In[21]:


B=[10,20,30,40,50]


# In[26]:


print(r.choices(B,k=90))


# In[27]:


print(r.uniform(10,90)) #returns any random num #b/w the range includes the range values


# In[30]:


c=dir(r)  #to find all functions in a module


# In[33]:


c


# In[34]:


#display whole year calendar


# In[35]:


import calendar


# In[39]:


print(calendar.calendar(2022))


# In[40]:


print(calendar.month(2022,6))


# In[43]:


calendar.setfirstweekday(calendar.THURSDAY)


# In[44]:


print(calendar.month(2022,6))


# In[46]:


import datetime as dt


# In[51]:


d=dt.datetime.now()


# In[54]:


print(d)


# In[56]:


sv=d.strftime('%y') #lower case


# In[57]:


sv


# In[62]:


fv=d.strftime('%Y') #uppercase


# In[61]:


fv


# In[69]:


#functions

#classifications - 
 #1. pre defined funcs
 #2.userdefined funcs
#for code resuability we use func's.
#lets say we want to use a particular concept multiple times in our programn instead of writing the same code multiple times,we can write in once include that inside a function and can call the function whereever we need it
#types - 
 #1. funcs without argument without return values
 #2. without argument with return value
 #3. with argument with return value
 #4. with arg without rv   


# In[66]:


def sample():    #def or descriptn
    print("great day")
    print("happy time")
sample()     #call
print("today")
sample()
    


# In[73]:


def multi():   #without arg without rv
    n1=int(input('number:'))
    n2=int(input('number:'))
    n3=int(input('number:'))
    prod=n1*n2*n3
    print(prod)
multi()    


# In[74]:


def multi():   #without arg with rv
    n1=int(input('number:'))
    n2=int(input('number:'))
    n3=int(input('number:'))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)


# In[76]:


#with arg w/o rv
def multi(n1,n2,n3):   
    prod=n1*n2*n3
    print(prod)
multi(3,4,5)    


# In[82]:


def multi(a,b,c):   #user input
    prod=a*b*c
    print(prod)
n1=int(input('number:'))
n2=int(input('number:'))
n3=int(input('number:'))    
multi(n1,n2,n3)
    


# In[83]:


#with arg with rv
def multi(n1,n2,n3):   
    prod=n1*n2*n3
    return(prod)
res=multi(3,4,5)
print(res)


# In[85]:


def multi(a,b,c):   #user input
    prod=a*b*c
    return prod
n1=int(input('number:'))
n2=int(input('number:'))
n3=int(input('number:'))    
res1=multi(n1,n2,n3)
print(res1)
    


# In[86]:


#1. lemons prgrm using func type1
#2. find factors of the given number using funcs type2
#3. print multiplication table of given number using funcs type3
#4. find out sum of digits of the given number using funcs type4


# In[92]:


#2
def factors():
    x=int(input("enter number:"))
    for i in range(1,x+1):
        if x % i == 0:
            print(i)
    return(i)
res=factors()
print(res)
        


# In[94]:


#3
def table(num):
    for i in range(1,11):
        print(num, 'x',i, '=',num*i)
n = int(input("enter a number:")) 
table(n)


# In[16]:


#4
def add(n):
    sum = 0
    for digit in range(0,len(n)):
        sum = sum+int(n[digit])
    return(sum)
sd=add('1234')
print(sd)


# In[ ]:




