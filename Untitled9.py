#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
bigString = myfile.read()
myList = bigString.split()
wordcounts = {}
for w in myList:    
    if w in wordcounts:        
        wordcounts[w] += 1   
    else:        
        wordcounts[w] = 1
x = {k: v for k, v in sorted(wordcounts.items(), key=lambda item: item[1])}

words = []
counts = []
for pair in x.items():
    counts.append(pair[1])
    words.append(pair[0])
words.reverse()
counts.reverse()
plt.plot(counts)
plt.xlabel("Words")
plt.ylabel("Counts")
plt.show()
#print(counts)
#print(words)


# In[2]:


mylist = ['rabbit', 'Dog', 'cat', 'Mouse', 'horse']

#Part A
t = sorted(mylist, key = lambda a: len(a))
t.reverse()
print(t)
print()

#Part B
y = sorted(mylist, key = lambda a: a.casefold())
print(y)


# In[ ]:




