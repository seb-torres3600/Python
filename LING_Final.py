#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Program 1
import random

def wordscramble(a): #individual word scrambler
    splitter = list(a) 
    x = len(splitter)-1
    first = splitter[0] #keeps first letter
    last = splitter[x] #keeps last letter
    i = 1
    middle = [] 
    while(i < x):
        middle.append(splitter[i])
        i += 1
    random.shuffle(middle) #shuffles randomly the middle
    newMiddle = "".join(middle) #joins middle
    newWord = first+newMiddle+last #makes new word
    return(newWord) #returns word

def scramble(c):
    splitter = c.split() #splits string into list
    i = 0
    x = len(splitter) #length of list
    sentence = [] #list for wprds returned
    while(i < x): 
        y = len(splitter[i]) #finds length of word at given space in list
        if (y <= 2): #checks to see if word is longer than 2 characters
            i = i + 1 #if its not it skips that word to scramble 
        else: #if longer than 2 characters
            w = wordscramble(splitter[i]) #sends word to wordscramble function, makes it into w
            sentence.append(w) #adds w to sentence list
            i = i + 1
    newSentence = " ".join(sentence)#makes string from joining list
    print(newSentence)#prints string
scramble("the quick brown fox jumped over the lazy dog")
scramble("i cant believe this code actually works")


# In[30]:


#Program 2

def isredup(a): #fuction
    x = len(a) #checks length for future use
    y = x / 2 #splits length in half
    t = list(a) #makes a into a list
    firsthalf = [] #first half of sentence
    lasthalf = [] #second half of sentence
    if(x % 2 == 0): #checks for even length
        i = 0
        s = int(y)
        while(i < y):#loop appends first half of a into list
            firsthalf.append(t[i])
            i += 1
        while(s < x):#loop appends last half of a into other list
            lasthalf.append(t[s])
            s += 1
        word = "".join(firsthalf) #joins first half as string
        wordtwo = "".join(lasthalf) #joins second half as string
        if(word == wordtwo): #if word is same as wordtwo prints "True"
            print(a, end = ": ") 
            print("True")
        else: #else "False"
            print(a, end = ": ") 
            print("False")
    if(x % 2 != 0): #if not even length
        g = a.split("-") #it splits it at "-"
        if (g[0] == g[1]):#comparison if same, prints "True"
            print(a, end = ": ") 
            print("True")
        else:#else prints "False"
            print(a, end = ": ") 
            print("False")

isredup("ma-wa")

isredup("randomword")

isredup("gogo-gogo")

isredup("panpan")

isredup("go-go")

isredup("bigword-bigword")


# In[32]:


#Program 3

def remover(a): #vowel remover function from individual words
    splitter = list(a) #splits a into list
    x = len(splitter) #finds length of splitter
    i = 0
    words = []
    vowels = ["a","e","i","o","u","A","E","I","O","U"] #vowels list 
    while(i < x):
        if(splitter[i] in vowels):#if character in vowels list it jumps to next
            i += 1
        else: #else adds character to new word
            words.append(splitter[i])
            i += 1
    newWord = "".join(words) #makes word into string
    return(newWord)#returns newWord without vowels

def removevowels(c):
    splitter = c.split() #splits string into list at white spaces
    i = 0
    x = len(splitter) #length of list splitter
    sentence = [] 
    while(i < x):#uses loop to call splitter function with each individual word
        w = remover(splitter[i]) #returns removed vowels to w
        sentence.append(w) #appends to sentence
        i = i + 1
    newSentence = " ".join(sentence) #makes it into a string
    print(newSentence) #prints

removevowels("the quick brown fox jumped over the lazy dog")
removevowels("i cant believe this code actually works")


# In[4]:


#Program 4

myfile = open('1200wsj.txt') #opens txt file
mystring = myfile.read() #converts it into string
words = mystring.split() #splits at white spaces
x = {s for s in words if len(s) >= 15} #if word is longer than 15 characters it adds it to dictionary

print(x) #prints dictionary


# In[5]:


#Program 5

myfile = open('1200wsj.txt') #opens txt file
sentence = myfile.read() #makes string of file
def averagelength(a): 
    ws = [len(word) for word in a.split()] #list of lenghts of each individual word
    average = sum(ws) / len(ws) #sum of ws divided by length of ws
    print('{:.2f}'.format(average)) #prints it with only two decimal places

averagelength(sentence)


# In[34]:


#Program 6

myfile = open('1200wsj.txt') #opens txt file
sentence = myfile.read() #makes file into string


def mostfrequent(series):
    sequence = series.split() #splits into list at white spaces
    zips = zip(sequence,sequence[1:]) #zips sequence of tokens
    counts = {} #dictionary of counts
    for pair in zips: #counts repetition of two token sequences
        counts[pair] = counts.get(pair, 0) + 1
    x = sorted(counts.items(),key = lambda x: x[1],reverse = True)[:1] #makes list with most repeated tokens
    g,t = zip(*x)#unzips it
    print(g) #prints most common token 

mostfrequent(sentence)


# In[ ]:




