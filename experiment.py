


filed = open('thaidictexp.txt', 'r',  encoding="utf-8")
file = open('thai.txt', 'r',  encoding="utf-8")
textd = filed.read()
text = file.read()
words = textd.split()
wordss = text.split()
length = len(text)
string =''
fstring = ''

for i in range(0,length):
    #print (i)
    if string + text[i] in words:
        print(string + text[i] )
        fstring = fstring + ' ' + (string + text[i] )
        string = ''
    else:
        string = text[i] + string
        
print (fstring)
print("DONE!")
