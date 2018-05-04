from Main import *
from tkinter import *
#file = open('/Users/shahud/PycharmProjects/ProjectPOS/data/Inputtext', 'w',  encoding="utf-8")


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


        #Create TextBox2 for cutkum output
        self.cutkum = Label(self,text="PyThaiNLP")
        self.cutkum.grid(row=4,column=0,columnspan =2 )
        self.text2 = Text(self,width=50,height=10,wrap =WORD,borderwidth=2,relief="groove")
        self.text2.grid(row=5,column=0,columnspan =2 )

        # Create TextBox3 for DeepCut output
        self.deep = Label(self, text="Deepcut")
        self.deep.grid(row=6, column=0, columnspan=2 )
        self.text3 = Text(self, width=50, height=10, wrap=WORD,borderwidth=2,relief="groove")
        self.text3.grid(row=7, column=0, columnspan=2 )

        # Create TextBox4 for TAS output
        self.ats = Label(self, text="Dictionary Method")
        self.ats.grid(row=8, column=0, columnspan=2)
        self.text4 = Text(self, width=50, height=10, wrap=WORD,borderwidth=2,relief="groove")
        self.text4.grid(row=9, column=0, columnspan=2 )

        # Create TextBox5 for Comparison output
        self.ats = Label(self, text="Comparison all language")
        self.ats.grid(row=10, column=0, columnspan=2 )
        self.text5 = Text(self, width=50, height=10, wrap=WORD,borderwidth=2,relief="groove")
        self.text5.grid(row=11, column=0, columnspan=2 )

    def output(self):
        ## Display message base on the pasword typed in
        content = self.word.get()
        if content:
            #return trnaslation
            #self.text1.delete(0.0, END)
            #self.text1.insert(0.0,intro.translations(content))
            #k = "We turned it off because internet is slow"
            #self.text1.insert(0.0,k)
            #file.write(content)
            #file.close()
            #return pythize
            self.text2.delete(0.0,END)
            self.text2.insert(0.0,other.pythaize(content))
            #return deepcut
            self.text3.delete(0.0, END)
            self.text3.insert(0.0, other.deepcutize(content))
            #return TAS
            self.text4.delete(0.0, END)
            self.text4.insert(0.0, our.ourmethodize(content))
            # return all
            self.text5.delete(0.0, END)
            self.text5.insert(0.0, ending.flow(content))
        else:
            message = "Please insert the word"
            self.text.delete(0.0,END)
            self.text.insert(0.0,message)
root = Tk()
root.title("Thai Advance segmentator")
app = Application(root)
root.mainloop()
