#!/usr/bin/env python
# coding: utf-8

# # bitwise operators 
# 0's nd1's 
# some operation if u do lyk dis it will be faster like compressing data
# sending data in network to network
# 0-1 or on off or true false

# In[1]:


#bitwise and
#bitwise or
#bitwise not
#bitwise nor
#left shift and right shift


# In[2]:


10&4


# In[3]:


12&7


# In[4]:


10|4


# In[5]:


12|7


# In[6]:


~3 #negation


# In[7]:


~7


# In[8]:


5^6 #xor


# In[9]:


9^8


# In[10]:


10<<2 #left shift


# In[11]:


10>>2 #right shift


# In[12]:


5<<2


# In[13]:


7>>3


# In[14]:


#get any two numbers both the no's shud be less than or eq to 15.Perform bitwise and or xor


# In[ ]:


a,b=int(input("enter a:")),int(input("enter b:"))
print(a&b)
print(a|b)
print(a^b)


# In[1]:


a=int(input())
for i in range(a):
    space=" "*i
    print(space+("* ")*a)
    a=a-1


# In[2]:


n=int(input("size:"))
a=list(map(int,input("numbers:").split()))[:n]
print(a)


# In[3]:


print("its","a","good","day ",end='**')
print(" all","is","good", sep="***",end=' ')
print("joy")


# In[5]:


print(" * *   * * ")
print("* * * * * * ")
print(" * * * * * ")
print("  * * * *") 
print("    * *  ")
print("     *   ")


# In[6]:


#conditional statements
#1.simple if
#2.if else
#3.else if
#4.else if ladder
#5.nested if


# In[7]:


#temp above 45 - hottest
#hot - 40-45
#moderate - 25-40
#cold - 10-25
#chill below 10


# In[8]:


temp=int(input())
if temp>45:
    print("hottest")
elif temp>=40:
        print("hot")
elif temp>=25:
    print("moderate")
elif temp>=10:
    print("cold")
elif temp<=10:
    print("chill")            


# In[ ]:




