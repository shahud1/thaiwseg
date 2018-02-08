import time
from mtranslate.core import translate

filed = open('thaidict.txt', 'r',  encoding="utf-8")
file = open('thai.txt', 'r',  encoding="utf-8")
textd = filed.read()
text = file.read()
words = textd.split()
wordss = text.split()
length = len(text)
string =''
fstring = ''
duplicate = ''
tran = text
tran = translate(tran,"en","th")
print("The Original text/sentences:" ,text)
print("The Google translation :" ,tran)
print("\n")
print("******* SHORTEST TERM METHOD *********")
for i in range(0,length):
    #print (i)
    if string + text[i] in words:
        duplicate = duplicate + '  ' + string + text[i] 
        fstring = fstring + ' ' + (string + text[i] )
        string = ''
    else:
        string = text[i] 
        
print (fstring)

print("\n")
print("******* SEARCHING METHOD *********")

searchterms = ''
for i in range(0,len(words)):
    if words[i] in text:
        #print (words[i])
        searchterms = searchterms + ' ' + words[i]
    
print(searchterms)
print("\n")
print("******* NEW METHOD ( LONGEST ) *********")
ltt = ''
st = searchterms.split()
for i in range(0,len(words)):
    for j in  range(0,len(st)):
        if words[i] + st[j] in text:
            lt = (words[i] + st[j])
            print ((lt + '-' + translate(lt,"en","th")),end=' , ')
            ltt = lt + ' ' + ltt
            
print("\n")
print("\n")
print("\n")
print("******* WHAT IS THE LONGEST WORD? *********")
ltt = ltt.split()
longest = ''

for i in range(0,len(ltt)):
    if len(ltt[i]) > len(longest):
            longest = ltt[i]

print ("Longest Word is: ",translate(longest,"en","th") )

print("\n")
print("******* WITHOUT REMOVING DUPLICATES *********")

def longestp(x):
    l =''
    l2 = ''
    for i in range(0,len(x)):
        if(len(x[i]) > len(l)):
            l2 = x[i]
            l = l2
    #print (l2)
    global l3
    l3 = l2
           
        

set1 = ''
longest2 = ''
longest3 = ''
for i in range(0,length):
    set1 = ''
    #print(text[i])
    for j in range(0,len(ltt)):
        if ltt[j][0] == text[i]:
            set1 = set1 + ' ' + ltt[j]
    set2 = set1.split()
    #print(set2,len(set2))
    longestp(set2)
    #print (l3)
    longest2 = longest2 + '|' + l3
    longest3 = longest3 + ' ' + l3
print("\n")
print (longest2)
print (translate(longest2,"en","th") )
longest3 = longest3.split()
length = int (len(longest3)/2)
d = ''
for i in range(length):
    if (longest3.count(longest3[i]) != 1 ):
        longest3.remove(longest3[i])
        
print("\n")           
print(" ******* REMOVING DUPLICATES ********* \n",longest3)
for i in range(0,len(longest3)):
    print((translate(longest3[i],"en","th")),end=' | ')
    



print("\n")
print("\n")
print("\n")
print("******* FILTERING FOR DUPLICATES & REMOVING BULLSHIT*********")

y = searchterms.split()
length = int (len(y)/2)
d = ''

for i in range(length):
    if (y.count(y[i]) != 1 ):
        d = d + '  ' + y[i]
        y.remove(y[i])
        
print(" The Duplicated terms fixed are: ",d)
print("\n")

print(" Therefore the SEGMENTED words WITH ENG TRANSLATION are: ",y)
print("\n")
length = len(y)
for i in range(length-1):
    print ((y[i] + '-' + translate(y[i],"en","th")),end=' , ')


filed.close()
file.close()




    
