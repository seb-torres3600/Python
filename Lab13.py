#!/usr/bin/env python
# coding: utf-8

# In[1]:


numberlist = [5,4,3,2,1]
letterlist = ["c","b","a"]

def mySort(NumList, reverse = False):
    Number = len(NumList)
    i = 0
    while(i < Number):
        j = i + 1
        if(reverse == True):
            while(j < Number):
                if(NumList[i] < NumList[j]):
                    temp = NumList[i]
                    NumList[i] = NumList[j]
                    NumList[j] = temp
                j = j + 1
        else:
            while(j < Number):
                if(NumList[i] > NumList[j]):
                    temp = NumList[i]
                    NumList[i] = NumList[j]
                    NumList[j] = temp
                j = j + 1
        i = i + 1
    return(NumList)


print(mySort(numberlist))#Part A
print(mySort(numberlist,reverse = True))#Part B,Option 2
print(mySort(letterlist))#Part A
print(mySort(letterlist,reverse = True))#Part B,Option 2


# In[ ]:




