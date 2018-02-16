import time
from mtranslate.core import translate
from datetime import datetime

print ("                             LOADING...                                   ")
time.sleep(1.5) 
print("\n")
print("                            World's most...                                ")
print("   _       _                               _   _____ _           _         ")
print("  /_\   __| |_   ____ _ _ __   ___ ___  __| | /__   \ |__   __ _(_)        ")
print(" //_\\ / _` \ \ / / _` | '_ \ / __/ _ \/ _` |   / /\/ '_ \ / _` | |        ")
print("/  _  \ (_| |\ V / (_| | | | | (_|  __/ (_| |  / /  | | | | (_| | |        ")
print("\_/ \_/\__,_| \_/ \__,_|_| |_|\___\___|\__,_|  \/   |_| |_|\__,_|_|        ")
print(" __    __              _   __                                 _            ")
print("/ / /\ \ \___  _ __ __| | / _\ ___  __ _ _ __ ___   ___ _ __ | |_ ___ _ __ ")
print("\ \/  \/ / _ \| '__/ _` | \ \ / _ \/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \ '__|")
print(" \  /\  / (_) | | | (_| | _\ \  __/ (_| | | | | | |  __/ | | | ||  __/ |   ")
print("  \/  \/ \___/|_|  \__,_| \__/\___|\__, |_| |_| |_|\___|_| |_|\__\___|_|   ")
print("                                   |___/                                   ")
print("\n")
print ("|￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|  ")
print ("|  ©   CREATED BY: HUD, PUNCH & BOY   ©   |  ")
print ("|＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿| ")
print ("       || ")
print ("(\__/) || ")
print ("(•ㅅ•) || ")
print ("/ 　 づ  ")
print("\n")

''' We Will comment out the loading and outing screen while implementing code in class '''

thaidictfile = open('thaidict.txt', 'r',  encoding="utf-8")  # Opening the dictionary file
thaiinputfile = open('thai.txt', 'r',  encoding="utf-8")     # Opening the input file
thaidf = thaidictfile.read()                                 # Reading the dictionary file
texttf = thaiinputfile.read()                                # Reading the input file
dicwordssplit = thaidf.split()                               # Making all the words in the dictionary as individual strings
inputwordsplit = texttf.split()                              # Making the whole input in the input file as individual strings
lengthinput = len(texttf)                                      # The length of all the letters in dictionary
string =''
finalstring = ''
duplicate = ''
translatethis = texttf

OT = print("Original text/sentences: ",translatethis)      # Original Sentence
OTE = print("Thai translation : ",translate(translatethis,"en","th"))  # English Translation of original
OTC = print("Chinese translation : ",translate(translatethis,"zh","th"))  # Chinese Translation of original
print("\n")

press = input("Press any key to continue!")
print("\n")
print("******* SEARCHING WORDS FROM DICTIONARY *********")
print("Searching the whole dictionary file to find any world that might match the input sentence")
print("\n")
startTime = datetime.now()                # Place at beginning of code.To keep track of time.

searchterms = ''
for i in range(0,len(dicwordssplit)):
    if dicwordssplit[i] in texttf:
        #print (dicwordssplit[i],'-',translate(dicwordssplit[i],"en","th"),end=',')
        searchterms = searchterms + ' ' + dicwordssplit[i]
        
print("\n")    
print("Found terms are: ",searchterms)
print("\n")


print("******* USING THE SEARCHH TERMS...*********")
longestterms = ''
stermssplit = searchterms.split()
for i in range(0,len(dicwordssplit)):
    for j in  range(0,len(stermssplit)):
        if dicwordssplit[i] + stermssplit[j] in texttf:
            longterm = (dicwordssplit[i] + stermssplit[j])
            #print ((longterm + '-' + translate(longterm,"en","th")),end=' , ')
            longestterms = longterm + ' ' + longestterms
            
print("\n")
#print("The longest terms found are",longestterms)
print("\n")

longestterms = longestterms.split()          # Finding the single longest term
longestterm = ''

for i in range(0,len(longestterms)):
    if len(longestterms[i]) > len(longestterm):
            longestterm = longestterms[i]

print ("Longest Word is: ",longestterm," - ",translate(longestterm,"en","th") )

print("\n")


def longestp(x):                           # This step removes all duplicates
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
for i in range(0,lengthinput):
    set1 = ''
    #print(text[i])
    for j in range(0,len(longestterms)):
        if longestterms[j][0] == texttf[i]:
            set1 = set1 + ' ' + longestterms[j]
    set2 = set1.split()
    #print(set2,len(set2))
    longestp(set2)
    #print (l3)
    longest2 = longest2 + '|' + l3
    longest3 = longest3 + ' ' + l3
print("\n")
print (longest2)
print (translate(longest2,"en","th") )

l3split = longest3.split()
st = searchterms.split()
mix = l3split + st
x=0
s = texttf+'|'
q = ' '
ft = ''
for i in range(len(mix)-1):
    if mix[i][0] == s[0] and mix[i][1] == s[1]:
        s = s.replace(mix[i],"")
        ft = ft + '|'+ mix[i]
    
    
#print(ft)
srest = ''
s = s.split()
if len(s)!=0:
    for i in range(len(s)):
        srest = srest + '|' + s[i]
print(ft+srest)

    

timetook = (datetime.now() - startTime)   # End of the main code. Calculates time taken.



'''

NEW ONE:

for all the worlds of the dictionary found in the input text:
        Derive a method to 








longest3 = longest3.split()
lengthdic = int (len(longest3)/2)
d = ''
for i in range(lengthdic):
    if (longest3.count(longest3[i]) != 1 ):
        longest3.remove(longest3[i])
        

print("\n")           
print(" ******* REMOVING DUPLICATES ********* \n",longest3)
for i in range(0,len(longest3)):
    print((translate(longest3[i],"en","th")),end=' | ')

print("\n")

print("######### 12 feb 2018 ##########")
print("\n")

for i in range(0,lengthdic):
    set1 = ''
    print(text[i])
    for j in range(0,len(ltt)):
        if ltt[j][0] == text[i]:
            set1 = set1 + ' ' + ltt[j]
    set2 = set1.split()








    

'''
'''
print("\n")
print("\n")
print("\n")
print("******* FILTERING FOR DUPLICATES & REMOVING BULLSHIT*********")

y = searchterms.split()
lengthdic = int (len(y)/2)
d = ''

for i in range(lengthdic):
    if (y.count(y[i]) != 1 ):
        d = d + '  ' + y[i]
        y.remove(y[i])
        
print(" The Duplicated terms fixed are: ",d)
print("\n")

print(" Therefore the SEGMENTED words WITH ENG TRANSLATION are: ",y)
print("\n")
lengthdic = len(y)
for i in range(lengthdic-1):
    print ((y[i] + '-' + translate(y[i],"en","th")),end=' , ')
'''

thaidictfile.close()
thaiinputfile.close()

print("\n")




print("###############################################################################")
print("##                                                                           ##")
print("    SEGMENTED WORDS: ",(ft+srest))
print("##                                                                           ##")
print("###############################################################################")
print("                    ____    ")
print("                 _.' :  `._    ")
print("            .-.'`.  ;   .'`.-.    ")
print("   __      / : ___\ ;  /___ ; \ ___,   ")
print(" ,'_ ""--.:__;'.-.';: :'.-.':__;.--"" _`,")
print("  :' `.t" "--.. '<@.`;_  ',@>` ..--""j.' `;")
print("      `:-.._J '-.-'L__ `-- ' L_..-;   ")
print('        "-.__ ;  .-"  "-.  : __.-   ')
print("            L ' /.------.\ ' J    ")
print('             "-.   "--"   .-"          |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|')
print('            __.l"-:_JL_;-";.__         | DONE!','Completed in:',timetook,' |')
print('         .-j/".;  ;""""  / ."\"-.       |                                     |')        
print("       .' /:`. '-.:     .-' .';  `.    |     MAY THE FORCE BE WITH YOU!      |")
print("    .-'  / ;  '-. '-..-' .-'  :    '-. |_____________________________________|")
print(" .+'-.  : :      '-.__.-'      ;-._   \" ")
print(" ; \  `.; ;                    : : '+. ;")
print(" :  ;   ; ;                    : ;  : \:")
print(": `.'-; ;  ;                  :  ;   ,/;")
print(" ;    -: ;  :                ;  : .-"'  :')
print(" :\     \  : ;             : \.-'      :")
print("  ;`.    \  ; :            ;.'_..--  / ;")
print("  :  '-.  '-:  ;          :/.'      .'  :")
print("    \       .-`.\        /t-""  ':-+.   :")
print("     `.  .-'    `l    __/ /`. :  ; ; \  ;")
print("       \   .-' .-'-.-'  .' .'j \  /   ;/")
print("        \ / .-'   /.     .'.' ;_:'    ;")
print("         :-""-.`./-.'     /    `.___.'")
print("               \ `t  ._  /      :___:")
print("                '-.t-._:'")
print("")
print("")
print("###############################################################################")

    
