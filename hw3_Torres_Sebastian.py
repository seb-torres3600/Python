#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Sebastian Torres
#HW3

#S → NP VP
#NP → Det Adj N | Det N | Adj PropN | PropN
#VP → Vi | Vt NP | Vc Comp S

#Det → the | a | some | any | every
#Adj → green | young | tired | confused
#N → dog | cat
#PropN → John | Mary
#Vi → sleeps | walks
#Vt → loves | hates
#Vc → says | thinks | believes
#Comp → that

import random 

stringlist = []

def END():
    END.counter += 1
    x = len(stringlist)
    i = 0
    if(END.counter == 1):
        while (i < x):
            y = stringlist[i]
            if (i == x - 1):
                print(y)
            else:
                print(y, end = " ")
            i += 1
    else:
        return

END.counter = 0 
def S():
    glist = [NP,VP]
    x = len(glist)
    i = 0
    while (i < x):
        glist[i]()
        i = i + 1
    END()
    

def NP():
    list_ONE = [Det, Adj,N]
    list_TWO = [Det, N]
    list_THREE = [Adj, PropN]
    list_FOUR = [PropN]
    list_Total = [list_ONE,list_TWO,list_THREE,list_FOUR]
    x = random.choice(list_Total)
    y = len(x)
    i = 0
    while (i < y):
        x[i]()
        i =i + 1
    if( i != 0):
        return
    VP()
    return

def VP():
    list_ONE = [Vi]
    list_TWO = [Vt , NP]
    list_THREE = [Vt,Comp,S]
    list_Total = [list_ONE,list_TWO,list_THREE]
    x = random.choice(list_Total)  
    y = len(x)
    i = 0
    while (i < y):
        x[i]()
        i = i + 1
    return 

def Det():
    detlist = ["the", "a", "some","any","every"]
    x = random.choice(detlist)
    stringlist.append(x)
def Adj():
    adjlist = ["green", "young","tired","confused"]
    x = random.choice(adjlist)
    stringlist.append(x)
def N():
    nlist = ["dog", "cat"]
    x = random.choice(nlist)
    stringlist.append(x)
def PropN():
    propNlist = ["John", "Mary"]    
    x = random.choice(propNlist)
    stringlist.append(x)
def Vi():
    Vilist = ["sleeps", "walks"]
    x = random.choice(Vilist)
    stringlist.append(x)
def Vt():
    Vtlist = ["loves","hates"]
    x = random.choice(Vtlist)
    stringlist.append(x)
def Vc():
    Vclist = ["says","thinks", "believes"]
    x = random.choice(Vclist)
    stringlist.append(x)
def Comp():
    Complist = ["that"]
    x = random.choice(Complist)
    stringlist.append(x)
    

S()


# In[ ]:





# In[ ]:




