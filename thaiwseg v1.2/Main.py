# -*- coding: utf-8 -*
import deepcut
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from mtranslate.core import translate
from pythainlp import *
from cutkum.tokenizer import Cutkum
from pythainlp.tag import pos_tag
from pythainlp.romanization import romanization
from pythainlp.rank import rank
'''
import tkinter as tk

root = tk.Tk()
image = tk.PhotoImage(file="yoda3.png")
label = tk.Label(image=image)
label.pack()
root.mainloop()'''


class intro:

    def translations(x):
        #s="\n"
        T = ["Original text/sentences: ", x]  # Original Sentence
        #OTE = ["Thai translation : ", translate(x, "en", "th")]  # English Translation of original
        #OTC = ["Chinese translation : ", translate(x, "zh", "th")]  # Chinese Translation of original
        #return T,s,OTE,s,OTC

class other:
    wordcut = ''
    wordpy = ''
    worddeep = ''

    def deepcutize(x):
        words = deepcut.tokenize(x)
        words = '|'.join(words)
        worddeep = words 
        return words

    def pythaize(x):
        words = word_tokenize(x)
        words = '|'.join(words)
        wordpy = words
        return words

    def cutcomize(x):
        ck = Cutkum()
        words = ck.tokenize(x)
        wordcut = words
        return words

    def fuzzywuzzize(x):
        #fuzz.ratio(other.pythaize(x),other.deepcutize(x))
        first = other.cutcomize(x)
        second = other.pythaize(x)
        third = other.deepcutize(x)
        one = "Cutkum and PyThaiNLP has an accuracy of ",fuzz.ratio(first,second)
        return fuzz.ratio(first,second) , fuzz.ratio(first,third) , fuzz.ratio(second,third)

    def tokenize(x):
        tagged = pos_tag(other.cutcomize(x),engine='old')
        return tagged

    def romanize(x):
        tagged = romanization(other.deepcutize(x),engine='royin')
        return tagged

    def frequentize(x):
        tagged = rank(other.cutcomize(x))
        return tagged

    def translationize(x):
        translated = translate(x, 'en')
        return translated

class our:
    def ourmethodize(x):
        from fuzzywuzzy import fuzz
        from fuzzywuzzy import process
        import time
        from mtranslate.core import translate
        from datetime import datetime
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


class ending:
    def flow(x):
        s="\n"
        cut=("pythize: ", other.pythaize(x))
        deep=("Deepcut: ", other.deepcutize(x))
        py=("PyThaiNLP: ", other.pythaize(x))
        tas=("Ourcut: ",our.ourmethodize(x))
        return cut,s,deep,s,py,tas
