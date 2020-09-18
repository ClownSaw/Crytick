#!/usr/bin/python3
#Autor: ClownSaw
#Web: www.clownsaw.tk
# Import modules
from tkinter import *
import tkinter as tk
import core.crytick as crytick
from PIL import ImageTk, Image

# Main
if __name__ == "__main__":

    # Commands
    def encrypt():
        text = eText.get('1.0', END)
        key  = kEntry.get()
        res  = crytick.Encrypt(text, key)
        dText.delete('1.0', END)
        dText.insert(1.0,res)

    def decrypt():
        text = dText.get('1.0', END)
        key  = kEntry.get()
        res  = crytick.Decrypt(text, key)
        eText.delete('1.0', END)
        eText.insert(1.0,res)


    # Configure windows
    root = Tk()
    root.iconphoto(False, PhotoImage(file='core/icon.png'))
    root.title("Crytick | ClownSaw")
    root.resizable(0, 0)
    root.geometry("900x355")
    root.configure(background="#111111")
    
    # Items
    eText   = Text(root, height=15, width=50, fg="#d5d8dc", bg="#07000a")
    dText   = Text(root, height=15, width=50, fg="#d5d8dc", bg="#07000a")
    kEntry  = Entry(root, width=96, fg="#d5d8dc", bg="#07000a", bd=2)
    eButton = Button(root, height=2, width=44, fg="#d5d8dc", bg="#07000a", text="Encrypt text >>", command = encrypt)
    dButton = Button(root, height=2, width=44, fg="#d5d8dc", bg="#07000a", text="<< Decrypt text", command = decrypt)
    
    #imagen
    path = 'core/banner.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, height=338, width=100, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    # Place
    panel.place(x=5, y=5)
    eText.place(x=120, y=10)
    dText.place(x=520, y=10)
    kEntry.place(x=119, y=255)
    eButton.place(x=120, y=285)
    dButton.place(x=520, y=285)
    root.mainloop()