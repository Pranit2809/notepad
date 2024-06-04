from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import os
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

l1=Label(root,text="file name:")
l1.place(relx=0.45,rely=0.05, anchor=CENTER)

input_field=Entry(root)
input_field.place(relx=0.6, rely=0.05, anchor=CENTER)

text_area=Text(root,height=35,width=80)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""
def openfile():
    global name
    input_field.delete(0,END)
    text_area.delete(1.0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("text files","*.txt"),))
    print(text_file)
    name=os.path.basename(text_file)
    print(name)
    actual_name=name.split('.')[0]
    print(actual_name)
    input_field.insert(END,actual_name)
    root.title(actual_name)
    text_file=open(name,'r')
    para=text_file.read()
    text_area.insert(END, para)
    text_file.close()

def save():
    input_name=input_field.get()
    file=open(input_name+".txt","w")
    data=text_area.get("1.0",END)
    print(data)
    file.write(data)
    input_field.delete(0,END)
    text_area.delete(1.0,END)
    messagebox.showinfo("update","success")
    
def closew():
    root.destroy()

load1=Image.open("folder.jpg")
load=load1.resize((50,50))
folder=ImageTk.PhotoImage(load)
openfolder=Button(root,image=folder,command=openfile)
openfolder.place(relx=0.05,rely=0.05,anchor=CENTER)

load2=Image.open("close.jpg")
load3=load2.resize((50,50))
close=ImageTk.PhotoImage(load3)
closefolder=Button(root,image=close, command=closew)
closefolder.place(relx=0.15,rely=0.05,anchor=CENTER)

load4=Image.open("save.png")
load5=load4.resize((50,50))
save=ImageTk.PhotoImage(load5)
savefolder=Button(root,image=save, command=save)
savefolder.place(relx=0.25,rely=0.05,anchor=CENTER)

load6=Image.open("play.jpg")
load7=load6.resize((50,50))
play=ImageTk.PhotoImage(load7)
playf=Button(root,image=play)
playf.place(relx=0.35,rely=0.05,anchor=CENTER)

root.mainloop()
#add a play button