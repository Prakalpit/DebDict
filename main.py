from tkinter import *
from tkinter.ttk import *
from PyDictionary import PyDictionary

from pathlib import Path
BaseDIR = Path(__file__).resolve().parent
IMGPATH = BaseDIR/'Debhiss-DIctionary.ico'

root = Tk()
root.title("DEBHISS-Dictionary")
root.iconbitmap(str(IMGPATH))
root.geometry("600x568")

'''
Function Area
'''

def SearchForWord():
    dictionary = PyDictionary
    TextBox.config(state=NORMAL)
    TextBox.delete(1.0, END)
    word = str(WordEntryBox.get())
    meanings = dictionary.meaning(word)
    try:
        for k,v in meanings.items():
            TextBox.insert(END,k + "\n\n")
            for values in v:
                TextBox.insert(END, f"➡{values} \n\n")
    except AttributeError:
        TextBox.insert(END,"Error, not in dictionary")

    TextBox.config(state=DISABLED)

def AboutUsPopUP():
    top = Toplevel(root)
    top.geometry("750x250")
    top.title("About Project")
    Label(top, text="""
    Welcome People \n\n
    This Dictionary uses Python Programming language. It is Developed By Prakalpit Neupane, once a student here. 
    This Dictionary was built using PyDictionary which uses WordNet for getting meanings. 
    site: 
    https://wordnet.princeton.edu/
    
    Thank You for Using this Product, its version is 0.7.1
    
    """).pack()


def ConvertToFIle():
    word = str(WordEntryBox.get())
    text = TextBox.get("1.0", "end-1c")
    with open(f"{word}.txt", 'a') as f:
        f.write(word + '\n\n')
        f.write(text)

    top = Toplevel(root)
    top.geometry("260x260")
    top.title("About Project")
    Label(top, text=f"Created file {word}.txt").pack()


'''
GUI area
'''
MajorFrame = LabelFrame(root,text="Enter A Word")
MajorFrame.pack()

WordEntryBox = Entry(MajorFrame)
WordEntryBox.grid(row=0,column=0,padx=30, pady=15)

SearchButton = Button(MajorFrame, text="Do a Search !!", command=SearchForWord)
SearchButton.grid(row=0, column=1, padx=9, pady=15)

Label(root, text="").pack()
Button(root, text="About This Project", command=AboutUsPopUP).pack()
TextBox = Text(root, height=29,width=70)
TextBox.pack()
Button(root, text="Get in Text File", command=ConvertToFIle).pack()
root.mainloop()