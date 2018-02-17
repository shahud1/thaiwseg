# thaiwseg
Thaiwseg is word segmentation which based on Thai language, the project of a group of SIIT. We've tried to experiment and play around with the Thai language with using module like Pythainlp,Thai Dictionary and,mtranslate. We created an algorithm to divide the text input into word segment.

We noticed several methods of achieving this task across the internet and came up with the conclusion that Machine learning methods out perform any 'Stand alone Python' algorithm. Thai Language is far too complex than matching words from the dictionary for segmentation.

In this version (v0.9) we compared the top performing methods like Deepcut, Cutkum (coming in v1.0),PythaiNlp with a python algorithm based word segmenter. 

In the future versions we plan to implement a Machine learning algorithm (using Tensorflow).

# Requirement
Python 3.0 ++

Deepcut

Pythainlp

mTranslate

Fuzzywuzzy

Flask

# Detail and Install instructions

Create a virtual machine using virtualenv ( pip install virtualenv ) and run the whole project in a virtual environment 

Also, install these repositories:
```python
$ pip install cutkum
```
```python
$ pip install pythainlp
```
```python
$ pip install deepcut  and pip install docker
```
```python
$ pip install pythainlp
```
```python
$ pip install mtranslate   
```
```python
$ pip install fuzzywuzzy
```

- Easiest way to install is by creating a virtual environment. Install all the repositories above only when the virtualenv have been activated.
- Download the whole git folder as zip and unzip the files inside the virtual environment folder that you created.
- If Cutkum cannot find 'lstm.l6.d2.pb' , download and copy it to 'virtualenv/model/' directory.
- Copy the Main.py and thaidict.txt to the 'virtualenv/' directory. [ make sure both files are in the same Dir ]
- To run the file, open Terminal and move to the 'virtualenv/' directory. Then activate using 'source bin/activate' command. After that run python3 and type the necessary command.
- In the above mentioned directory type: python3 Real_gui.py and run it!
- After the GUI successfully loads type in the Thai sentence and press enter.
- IF YOU HAVE ANY ISSUES RUNNING THE FILE PLEASE RAISE AN ISSUE

# Installation video:

 [Install guide]https://www.youtube.com/watch?v=iDxvAWlIR-w


# Coding Section

first of all let's explain about the code and how it work 
1.import each modules

```python

from mtranslate.core import translate
import deepcut
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from mtranslate.core import translate
from pythainlp import *
```
2.in "class intro" shows translation function for translate from Thai to English and Chinese
```python

class intro:
    def translations(x):
        s="\n"
        T = ["Original text/sentences: ", x]  # Original Sentence
        OTE = ["Thai translation : ", translate(x, "en", "th")]  # English Translation of original
        OTC = ["Chinese translation : ", translate(x, "zh", "th")]  # Chinese Translation of original
        return T,s,OTE,s,OTC

```
3.using module of each word segmet of each module
```Pyhton

class other:
    def deepcutize(x):
        words = deepcut.tokenize(x)
        return words

    def pythaize(x):
        words = word_tokenize(x)
        return words
        
```
4.using dictmethod class which is our algorithm to work with word segmentation
```python
class dictmethod:
    def methodize(x):
        thaidictfile = open('thaidict.txt', 'r', encoding="utf-8")  # Opening the dictionary file
        thaidf = thaidictfile.read()  # Reading the dictionary file
        texttf = x  # Reading the input file
        dicwordssplit = thaidf.split()  # Making all the words in the dictionary as individual strings
        inputwordsplit = x.split()  # Making the whole input in the input file as individual strings
        lengthinput = len(x)  # The length of all the letters in dictionary
        string = ''
        finalstring = ''
        duplicate = ''
        translatethis = x

        listofwords = ''
        for i in range(0, len(dicwordssplit)):  # This for loop splits the whole dictionary into word by word
            if dicwordssplit[i] in x:  # and checks whether everyword in the dictionary is present
                listofwords = listofwords + ' ' + dicwordssplit[
                    i]  # in the input sentence. If it finds any, it adds those words in to
                # the variable list of words
        mix = listofwords.split()

        #
        st = ''

        for i in range(len(x)):  # This for loop checks if the first letter of every word in the mix var
            for j in range(len(mix)):  # matches the first letter of all words in the input. If it finds any it
                if mix[j][0] == x[i]:  # adds the word in to variable st
                    st = st + ' ' + mix[j]
        st = st.split()

        #
        st2 = ''
        for i in range(len(st)):  # This for loop checks if all the words in st are length 1 and above. This
            if len(st[i]) > 1:  # is to eliminate any single letters.
                st2 = st2 + ' ' + st[i]
        st = st2
        st = st.split()

        #
        s = x
        k = ''
        for i in range(len(st)):  # This for loop checks if any words of st are in the input sentence. If it
            if st[i] in s:  # finds any, it will remove the word from the input sentence and also add
                k = k + '|' + st[i]  # that word into a variable k.
                s = s.replace(st[i], '')

        #
        srest = ''
        s = s.split()
        if len(s) != 0:  # srest if the words that were present in input text not found in dictinary.
            for i in range(len(s)):  # these words are printed the last
                srest = srest + '|' + s[i]
        return (k + srest)

        thaidictfile.close()

```
5.finally show all the method and comparision of each one 
```python

class ending:
    def flow(x):
        deep = ("Deepcut: ", other.deepcutize(x))
        py = ("PyThaiNLP: ", other.pythaize(x))
        tas = ("Dictionary Method: ", dictmethod.methodize(x))
        s = "\n"
        li=[deep,s,py,s,tas]
        return li[0:]
        
```
# Reference
[Flask](http://flask.pocoo.org)

[Thai Dictionary](https://github.com/pureexe/thai-wordlist)

[mTranslate](https://www.npmjs.com/package/@ngx-translate/core)

[DeepCut](https://github.com/rkcosmos/deepcut)

[PyThaiNLP](https://github.com/PyThaiNLP/pythainlp)

[CutKum](https://github.com/pucktada/cutkum)

[FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy)

# Contributers 
* Punchok Kerdsiri -  https://github.com/punch872
* boycatbay - https://github.com/boycatbay
