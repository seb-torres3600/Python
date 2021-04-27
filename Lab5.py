#!/usr/bin/env python
# coding: utf-8

# In[2]:


sent = input("Enter a sentence:")
length = len(sent)
print("Your sentence", "\"",sent,"\"", "contains", length, "characters.")


# In[ ]:


fruits = ["apple", "banana","kiwi", "tomato", "apricot"]
length = len(fruits)
stop = 1
while(stop != length + 1 ):
    print(fruits[length - stop])
    stop = stop + 1


# In[ ]:




