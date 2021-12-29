#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task : 1
Line1 = "Twinkle, twinkle, little star,"
Line2 = "    How I wonder what you are!"
Line3 = "        Up above the world so high,"
Line4 = "        Like the diamond in the sky."
Line5 = "Twinkle, twinkle, little star,"
Line6 = "    How I wonder what you are!"


# In[2]:


print(Line1)
print(Line2)
print(Line3)
print(Line4)
print(Line5)
print(Line6)


# In[3]:


#Task : 2
get_ipython().system('python -V')


# In[4]:


#Task : 3
from datetime import datetime

date_and_time = datetime.now()
print("The today current date and time is:-" , date_and_time)


# In[5]:


#Task : 4

Radius = float(input("Enter the radius of circle: "))
Area = 3.14159 * (Radius*Radius)
print("Area of circle is: ", Area, "square units")


# In[6]:


#Task : 5

name = input("Enter your first and last name: ")

for char in range(len(name) - 1, -1, -1):
  print(name[char], end="")
print("\n")


# In[7]:


#Task : 6
a = float(input("Enter first number: "));
b = float(input("Enter second number: "));
c = a + b;
print(float(c))


# In[ ]:




