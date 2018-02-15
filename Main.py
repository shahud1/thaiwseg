# -*- coding: utf-8 -*
from cutkum.tokenizer import Cutkum
import deepcut
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from mtranslate.core import translate

class intro:
    
    def translations(x):
        T = print("Original text/sentences: ",x)                      # Original Sentence
        OTE = print("Thai translation : ",translate(x,"en","th"))     # English Translation of original
        OTC = print("Chinese translation : ",translate(x,"zh","th"))  # Chinese Translation of original
    

class other:
    
    def cutkumize(x):
        ck = Cutkum('lstm.l6.d2.pb')
        words = ck.tokenize(x)
        return words

    def deepcutize(x):
        words = deepcut.tokenize(x)
        return words

class our:
    def ourmethodize(x):
        from fuzzywuzzy import fuzz
        from fuzzywuzzy import process
        import time
        from mtranslate.core import translate
        from datetime import datetime
        thaidictfile = open('thaidict.txt', 'r',  encoding="utf-8")  # Opening the dictionary file
        thaidf = thaidictfile.read()                                 # Reading the dictionary file
        texttf = x                                                   # Reading the input file
        dicwordssplit = thaidf.split()                               # Making all the words in the dictionary as individual strings
        inputwordsplit = x.split()                                   # Making the whole input in the input file as individual strings
        lengthinput = len(x)                                         # The length of all the letters in dictionary
        string =''
        finalstring = ''
        duplicate = ''
        translatethis = x

        listofwords = ''
        for i in range(0,len(dicwordssplit)):
            if dicwordssplit[i] in x:
                listofwords = listofwords + ' ' + dicwordssplit[i]

        mix = listofwords.split()
        #
        st = ''
        
        for i in range(len(x)):
            for j in range(len(mix)):
                if mix[j][0] == x[i]:
                    st = st + ' ' + mix[j]
        st=st.split()
        #
        st2=''
        for i in range(len(st)):
            if len(st[i])>1:
                st2 = st2 + ' ' + st[i]
        st=st2
        st=st.split()
        #
        s = x
        k = ''
        for i in range(len(st)):
                if st[i]  in s:
                    k = k + '|' + st[i]
                    s = s.replace(st[i],'')
        #
        srest = ''
        s = s.split()
        if len(s)!=0:
            for i in range(len(s)):
                srest = srest + '|' + s[i]
        return (k+srest)

        thaidictfile.close()
                

class ending:
    
    def flow(x):
        print("Cutkum: ",other.cutkumize(x))
        print("Deepcut: ",other.deepcutize(x))
        print("Ourcut: ",our.ourmethodize(x))

        
        



    
