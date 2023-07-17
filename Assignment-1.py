#!/usr/bin/env python
# coding: utf-8

# In[1]:


###  write a python program that accepts a word from the user and reverse it

name="Edyoda"
print(name[::-1])


# In[7]:


w=input()
w1=" "
for i in range(len(w)-1,-1,-1):
    w1=w1+w[i]
print(w1)


# In[ ]:


### write a python program to  count the number of even and odd numbers from aseries of numbers


# In[2]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers: 
        if not x % 2:
             count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)



# In[ ]:


### write a python program to get the fibonacci series between 0 to 50


# In[7]:


a,b=0,1
while b < 50:
    print(b,end=" ")
    a,b=b,a+b
    

