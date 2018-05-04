from Main import *
from tkinter import *
#file = open('/Users/shahud/PycharmProjects/ProjectPOS/data/Inputtext', 'w',  encoding="utf-8")

import tkinter as tk

root = tk.Tk()
image = tk.PhotoImage(file="yoda3.png")
label = tk.Label(image=image)
label.pack()
root.mainloop()



class Application(Frame):
    """A GUI with app button"""
    def __init__(self,master):
        """ init the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Create button,text,and Entry widgets"""
        self.instruction = Label(self,text = "Enter the Sentence(s) ")
        self.instruction.grid(row= 0 ,column=0,columnspan= 2,sticky=W)

        self.word= Entry(self)
        ##trying
        ##endtrying
        self.word.grid(row=1,column=0)

        self.submit_button = Button(self,text ="Submit",command=self.output)
        self.submit_button.grid(row=1, column =1 ,sticky=W)

        #Create TextBox1 for cutkum output  NEEEWWWW
        self.newcutkum = Label(self,text="Cutkum", font='Helvetica 17 bold')
        self.newcutkum.grid(row=2,column=0,columnspan =2 )
        self.text1 = Text(self,width=50,height=10,wrap =WORD,borderwidth=2,relief="groove")
        self.text1.grid(row=3,column=0,columnspan =2 )


        #Create TextBox2 for pythai output
        self.cutkum = Label(self,text="PyThaiNLP", font='Helvetica 17 bold')
        self.cutkum.grid(row=4,column=0,columnspan =2 )
        self.text2 = Text(self,width=50,height=10,wrap =WORD,borderwidth=2,relief="groove")
        self.text2.grid(row=5,column=0,columnspan =2 )

        # Create TextBox3 for DeepCut output
        self.deep = Label(self, text="Deepcut", font='Helvetica 17 bold')
        self.deep.grid(row=6, column=0, columnspan=2 )
        self.text3 = Text(self, width=50, height=10, wrap=WORD,borderwidth=2,relief="groove")
        self.text3.grid(row=7, column=0, columnspan=2 )

        #Create TextBox4 for Fuzzywuzzy
        self.fuzzy = Label(self, text="FuzzyWuzzy Accuracy Comparison: ", font='Helvetica 17 bold')
        self.fuzzy.grid(row=8, column=0, columnspan=2 )
        self.fuzzy = Label(self, text="1- Cutkum & PyThaiNLP")
        self.fuzzy.grid(row=9, column=0, columnspan=2 )
        self.fuzzy = Label(self, text="2- Cutkum & Deepcut")
        self.fuzzy.grid(row=10, column=0, columnspan=2 )
        self.fuzzy = Label(self, text="3- Deepcut & PythaiNLP")
        self.fuzzy.grid(row=11, column=0, columnspan=2 )
        self.text4 = Text(self, width=50, height=1, wrap=WORD,borderwidth=2,relief="groove")
        self.text4.grid(row=12, column=0, columnspan=2 )

        #Create TextBox5 for tokenization output
        self.tok = Label(self,text="Tokenization of Most Accurate method", font='Helvetica 17 bold')
        self.tok.grid(row=2,column=2,columnspan =2 )
        self.text5 = Text(self,width=50,height=10,wrap =WORD,borderwidth=2,relief="groove")
        self.text5.grid(row=3,column=2,columnspan =2 )

        #Create TextBox6 for Romanization output
        self.tok = Label(self,text="Romanization", font='Helvetica 17 bold')
        self.tok.grid(row=4,column=2,columnspan =2 )
        self.text6 = Text(self,width=50,height=10,wrap =WORD,borderwidth=2,relief="groove")
        self.text6.grid(row=5,column=2,columnspan =2 )

        #Create TextBox7 for Frequent words output
        self.tok = Label(self,text="Most frequent words", font='Helvetica 17 bold')
        self.tok.grid(row=6,column=2,columnspan =2 )
        self.text7 = Text(self,width=50,height=10,wrap =WORD,borderwidth=2,relief="groove")
        self.text7.grid(row=7,column=2,columnspan =2 )

        #translate button
        self.translate_button = Button(self,text ="Translate text to English",command=self.output2)
        self.translate_button.grid(row=8, column =2 ,sticky=W)

        #Create TextBox8 for translated words output
        self.tok = Label(self,text="BONUS! English Translation", font='Helvetica 17 bold')
        self.tok.grid(row=9,column=2,columnspan =2 )
        self.text8 = Text(self,width=50,height=3,wrap =WORD,borderwidth=2,relief="groove")
        self.text8.grid(row=10,column=2,columnspan =2 )


    def output2(self):
        content = self.word.get()
        if content:
            #return Translation
            self.text8.delete(0.0, END)
            self.text8.insert(0.0, other.translationize(content))


    def output(self):
        ## Display message base on the pasword typed in
        content = self.word.get()
        if content:
            #return cutkum
            self.text1.delete(0.0,END)
            self.text1.insert(0.0,other.cutcomize(content))
            #return pythainlp
            self.text2.delete(0.0,END)
            self.text2.insert(0.0,other.pythaize(content))
            #return deepcut
            self.text3.delete(0.0, END)
            self.text3.insert(0.0, other.deepcutize(content))
            #return comparison
            self.text4.delete(0.0, END)
            self.text4.insert(0.0, other.fuzzywuzzize(content))
            #return tokanization
            self.text5.delete(0.0, END)
            self.text5.insert(0.0, other.tokenize(content))
            #return Romanization
            self.text6.delete(0.0, END)
            self.text6.insert(0.0, other.romanize(content))
            #return Frequent
            self.text7.delete(0.0, END)
            self.text7.insert(0.0, other.frequentize(content))
            '''#return Translation
            self.text8.delete(0.0, END)
            self.text8.insert(0.0, other.translationize(content))'''
            
        else:
            message = "Please insert the word"
            self.text.delete(0.0,END)
            self.text.insert(0.0,message)
root = Tk()
root.title("Thai Advance segmentator")
app = Application(root)
root.mainloop()
