{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the qcuik borwn fox jpmued over the lzay dog\n",
      "cnat bevelie tihs code altcluay wkors\n"
     ]
    }
   ],
   "source": [
    "#Program 1\n",
    "import random\n",
    "\n",
    "def wordscramble(a): #individual word scrambler\n",
    "    splitter = list(a) \n",
    "    x = len(splitter)-1\n",
    "    first = splitter[0] #keeps first letter\n",
    "    last = splitter[x] #keeps last letter\n",
    "    i = 1\n",
    "    middle = [] \n",
    "    while(i < x):\n",
    "        middle.append(splitter[i])\n",
    "        i += 1\n",
    "    random.shuffle(middle) #shuffles randomly the middle\n",
    "    newMiddle = \"\".join(middle) #joins middle\n",
    "    newWord = first+newMiddle+last #makes new word\n",
    "    return(newWord) #returns word\n",
    "\n",
    "def scramble(c):\n",
    "    splitter = c.split() #splits string into list\n",
    "    i = 0\n",
    "    x = len(splitter) #length of list\n",
    "    sentence = [] #list for wprds returned\n",
    "    while(i < x): \n",
    "        y = len(splitter[i]) #finds length of word at given space in list\n",
    "        if (y <= 2): #checks to see if word is longer than 2 characters\n",
    "            i = i + 1 #if its not it skips that word to scramble \n",
    "        else: #if longer than 2 characters\n",
    "            w = wordscramble(splitter[i]) #sends word to wordscramble function, makes it into w\n",
    "            sentence.append(w) #adds w to sentence list\n",
    "            i = i + 1\n",
    "    newSentence = \" \".join(sentence)#makes string from joining list\n",
    "    print(newSentence)#prints string\n",
    "scramble(\"the quick brown fox jumped over the lazy dog\")\n",
    "scramble(\"i cant believe this code actually works\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ma-wa: False\n",
      "randomword: False\n",
      "gogo-gogo: True\n",
      "panpan: True\n",
      "go-go: True\n",
      "bigword-bigword: True\n"
     ]
    }
   ],
   "source": [
    "#Program 2\n",
    "\n",
    "def isredup(a): #fuction\n",
    "    x = len(a) #checks length for future use\n",
    "    y = x / 2 #splits length in half\n",
    "    t = list(a) #makes a into a list\n",
    "    firsthalf = [] #first half of sentence\n",
    "    lasthalf = [] #second half of sentence\n",
    "    if(x % 2 == 0): #checks for even length\n",
    "        i = 0\n",
    "        s = int(y)\n",
    "        while(i < y):#loop appends first half of a into list\n",
    "            firsthalf.append(t[i])\n",
    "            i += 1\n",
    "        while(s < x):#loop appends last half of a into other list\n",
    "            lasthalf.append(t[s])\n",
    "            s += 1\n",
    "        word = \"\".join(firsthalf) #joins first half as string\n",
    "        wordtwo = \"\".join(lasthalf) #joins second half as string\n",
    "        if(word == wordtwo): #if word is same as wordtwo prints \"True\"\n",
    "            print(a, end = \": \") \n",
    "            print(\"True\")\n",
    "        else: #else \"False\"\n",
    "            print(a, end = \": \") \n",
    "            print(\"False\")\n",
    "    if(x % 2 != 0): #if not even length\n",
    "        g = a.split(\"-\") #it splits it at \"-\"\n",
    "        if (g[0] == g[1]):#comparison if same, prints \"True\"\n",
    "            print(a, end = \": \") \n",
    "            print(\"True\")\n",
    "        else:#else prints \"False\"\n",
    "            print(a, end = \": \") \n",
    "            print(\"False\")\n",
    "\n",
    "isredup(\"ma-wa\")\n",
    "\n",
    "isredup(\"randomword\")\n",
    "\n",
    "isredup(\"gogo-gogo\")\n",
    "\n",
    "isredup(\"panpan\")\n",
    "\n",
    "isredup(\"go-go\")\n",
    "\n",
    "isredup(\"bigword-bigword\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "th qck brwn fx jmpd vr th lzy dg\n",
      " cnt blv ths cd ctlly wrks\n"
     ]
    }
   ],
   "source": [
    "#Program 3\n",
    "\n",
    "def remover(a): #vowel remover function from individual words\n",
    "    splitter = list(a) #splits a into list\n",
    "    x = len(splitter) #finds length of splitter\n",
    "    i = 0\n",
    "    words = []\n",
    "    vowels = [\"a\",\"e\",\"i\",\"o\",\"u\",\"A\",\"E\",\"I\",\"O\",\"U\"] #vowels list \n",
    "    while(i < x):\n",
    "        if(splitter[i] in vowels):#if character in vowels list it jumps to next\n",
    "            i += 1\n",
    "        else: #else adds character to new word\n",
    "            words.append(splitter[i])\n",
    "            i += 1\n",
    "    newWord = \"\".join(words) #makes word into string\n",
    "    return(newWord)#returns newWord without vowels\n",
    "\n",
    "def removevowels(c):\n",
    "    splitter = c.split() #splits string into list at white spaces\n",
    "    i = 0\n",
    "    x = len(splitter) #length of list splitter\n",
    "    sentence = [] \n",
    "    while(i < x):#uses loop to call splitter function with each individual word\n",
    "        w = remover(splitter[i]) #returns removed vowels to w\n",
    "        sentence.append(w) #appends to sentence\n",
    "        i = i + 1\n",
    "    newSentence = \" \".join(sentence) #makes it into a string\n",
    "    print(newSentence) #prints\n",
    "\n",
    "removevowels(\"the quick brown fox jumped over the lazy dog\")\n",
    "removevowels(\"i cant believe this code actually works\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'family-planning', 'multibillion-dollar', 'confrontational', 'morale-damaging', 'transplantation', 'language-housekeeper', 'school-improvement', 'mortgage-backed', 'high-technology', 'state-supervised', 'energy-services', 'single-handedly', 'environmentalists', 'tissue-transplant', 'telecommunications', 'non-encapsulating', 'intellectual-property', 'search-and-seizure', 'get-out-the-vote', 'classifications', 'underprivileged', 'Macmillan/McGraw', 'incentive-bonus', 'attorney-client', 'collective-bargaining', 'school-sponsored', 'anti-abortionists', 'self-aggrandizing', 'stock-manipulation', 'electric-utility', 'Test-preparation', 'Macmillan/McGraw-Hill', 'Sacramento-based', 'computer-generated', 'Bridgestone/Firestone', 'industrial-production', 'abortion-related', 'battery-operated', 'pianist-comedian', 'export-oriented', 'sometimes-tawdry', 'asbestos-related', 'labor-intensive', 'Minneapolis-based', 'school-research', 'school-district', 'achievement-test', 'securities-based', 'Washington-based', 'black-and-white', 'pharmaceuticals', 'test-preparation', 'unrealistically', 'familiarization', 'dollar-denominated', 'automotive-parts', 'over-the-counter'}\n"
     ]
    }
   ],
   "source": [
    "#Program 4\n",
    "\n",
    "myfile = open('1200wsj.txt') #opens txt file\n",
    "mystring = myfile.read() #converts it into string\n",
    "words = mystring.split() #splits at white spaces\n",
    "x = {s for s in words if len(s) >= 15} #if word is longer than 15 characters it adds it to dictionary\n",
    "\n",
    "print(x) #prints dictionary\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.52\n"
     ]
    }
   ],
   "source": [
    "#Program 5\n",
    "\n",
    "myfile = open('1200wsj.txt') #opens txt file\n",
    "sentence = myfile.read() #makes string of file\n",
    "def averagelength(a): \n",
    "    ws = [len(word) for word in a.split()] #list of lenghts of each individual word\n",
    "    average = sum(ws) / len(ws) #sum of ws divided by length of ws\n",
    "    print('{:.2f}'.format(average)) #prints it with only two decimal places\n",
    "\n",
    "averagelength(sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(('.', 'The'),)\n"
     ]
    }
   ],
   "source": [
    "#Program 6\n",
    "\n",
    "myfile = open('1200wsj.txt') #opens txt file\n",
    "sentence = myfile.read() #makes file into string\n",
    "\n",
    "\n",
    "def mostfrequent(series):\n",
    "    sequence = series.split() #splits into list at white spaces\n",
    "    zips = zip(sequence,sequence[1:]) #zips sequence of tokens\n",
    "    counts = {} #dictionary of counts\n",
    "    for pair in zips: #counts repetition of two token sequences\n",
    "        counts[pair] = counts.get(pair, 0) + 1\n",
    "    x = sorted(counts.items(),key = lambda x: x[1],reverse = True)[:1] #makes list with most repeated tokens\n",
    "    g,t = zip(*x)#unzips it\n",
    "    print(g) #prints most common token \n",
    "\n",
    "mostfrequent(sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}