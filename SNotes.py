import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import cryptocode as cry

password="Legal"

window=tkinter.Tk()
window.title("Secret Notes")
window.configure(pady=10)
window.geometry('450x300')

# ui
ilbl=tkinter.Label()
photo1=Image.open("image/secret4.png")
imageAdd=ImageTk.PhotoImage(photo1)
ilbl.configure(image=imageAdd)

#labels
lbl_title=tkinter.Label(text="Enter Your Title")
lbl_text=tkinter.Label(text="Enter Your Text")
lbl_key=tkinter.Label(text="Enter Master Key")

#inputs
input_title=tkinter.Entry(width=20)
input_keys=tkinter.Entry(width=20)
input_keys.configure()

#textarea
text_box=tkinter.Text(width=15,height=10)

#Functions
def encryptAndSaveText():
    title=input_title.get()
    title=title.lower()
    content=text_box.get(1.0, tkinter.END)
    repassword=input_keys.get()

    if password==repassword:
        encode=cry.encrypt(content,password)
        writeText(title,encode)
        clearInputs()
    else:
        messagebox.showerror("Warning","Invalid Password")

def getTextContent():
    title = input_title.get().lower()
    content = readText(title)
    text_box.insert(tkinter.END,content)

def decryptString():
    content = text_box.get(1.0, tkinter.END)
    repassword = input_keys.get()

    if password==repassword:
        d_encode=cry.decrypt(content,repassword)
        text_box.delete("1.0", tkinter.END)
        text_box.insert(tkinter.END, d_encode)
    else:
        messagebox.showerror("Warning","Invalid Password")

def writeText(title, content):
    with open("test.txt","a") as file:
        file.write(title+":"+content+"\n")

def readText(title):
    with open("test.txt","r") as file:
        keys=file.readlines()
        for key in keys:
            if key.startswith(title):
                key=key.rstrip("\n")
                return key.split(":")[1]

def clearInputs():
    input_keys.delete(0,tkinter.END)
    text_box.delete("1.0", tkinter.END)
    input_title.delete(0,tkinter.END)



#buttons
btn_encrypt=tkinter.Button(text="Save&Encrypt" ,command=encryptAndSaveText, height=1, width=10)
btn_decrypt=tkinter.Button(text="Decrypt", height=1, width=10, command=decryptString)
btn_getir=tkinter.Button(text="Getir", height=1, width=10, command=getTextContent)
btn_getir.configure()

#Design
ilbl.place(x=400,y=0)
lbl_title.place(x=10, y=10)
lbl_text.place(x=10, y=35)
lbl_key.place(x=10,y=205)
input_title.place(x=110,y=10)
text_box.place(x=110,y=35)
input_keys.place(x=110,y=205)
btn_getir.place(x=240, y=10)
btn_encrypt.place(x=240,y=45)
btn_decrypt.place(x=240,y=75)

window.mainloop()









