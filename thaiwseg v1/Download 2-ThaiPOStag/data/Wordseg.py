from pythainlp.tokenize import word_tokenize
#from pSCRDRtagger.RDRPOSTagger import *
import deepcut
import os

inputfile = open('/Users/shahud/PycharmProjects/ProjectPOS/data/Inputtext', 'r',  encoding="utf-8")     # Opening the input file
outputfile = open('/Users/shahud/PycharmProjects/ProjectPOS/data/segmentedtext', 'w',  encoding="utf-8")     # Opening the input file
inputtext = inputfile.read()


x = word_tokenize(inputtext,engine='newmm')
y = deepcut.tokenize(inputtext)

inputfile.close()

#print(x)
#print(y)

for i in range(len(y)):
    outputfile.write(y[i])
    outputfile.write(" ")




