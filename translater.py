from cgitb import text
from this import d
from tkinter import *
from tkinter import ttk
from turtle import width
from googletrans import Translator, LANGUAGES


def change(text="type",src="English", dest="Hindi"):
    text1=text
    sec1=src
    dest1=dest
    trans = Translator()
    trans1=trans.translate(text,dest)
    return trans1.text

def data():
    s=comb1.get()
    d=comb2.get()
    masg=sortxt.get(1.0, END)
    textget=change(text=masg, src=s, dest=d)
    destxt.delete(1.0, END)
    destxt.insert(END, textget)


root =Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="red")

labtxt=Label(root, text="Translator", font=("Time New Roman",40, "bold"))
labtxt.place(x=100,y=40, height=50, width=300)

frame=Frame(root).pack(side=BOTTOM)

labtxt=Label(root, text="Source Text", font=("Time New Roman",20, "bold"), fg="black", bg="red")
labtxt.place(x=100,y=100, height=20, width=300)

sortxt=Text(frame, font=("Time New Roman",20, "bold"), wrap=WORD)
sortxt.place(x=10,y=130, height=150, width=480)

list_text=list(LANGUAGES.values())

comb1=ttk.Combobox(frame, value=list_text)
comb1.place(x=10,y=300, height=40, width=150)
#comb1.set("english")

button_change=Button(frame, text="translate", relief=RAISED, command=data)
button_change.place(x=170,y=300, height=40, width=150)

comb2=ttk.Combobox(frame, value=list_text)
comb2.place(x=330,y=300, height=40, width=150)
#comb2.set("english")

labtxt=Label(root, text="Destination Text", font=("Time New Roman",20, "bold"), fg="black", bg="red")
labtxt.place(x=100,y=360, height=20, width=300)

destxt=Text(frame, font=("Time New Roman",20, "bold"), wrap=WORD)
destxt.place(x=10,y=400, height=150, width=480)

root.mainloop()