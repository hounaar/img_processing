import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np


root = Tk()
root.geometry("1000x1000")
frame = tk.Frame(root)


show_pic = tk.Label(frame)
grayscale_pic = tk.Label(frame)
bw_pic = tk.Label(frame)



browse = tk.Button(frame, text='Select Image',bg='navy', fg='#ffffff',
                          font=('verdana',16))


def selectPic():
    global img
    global grayscale
    global bw
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("jpg images","*.jpg"),("png images","*.png"),
                           ("jpeg images","*.jpeg"), ("bmp images","*.bmp"),
                           ("gif images","*.gif")
                           ))
    img = Image.open(filename)
    img = img.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    show_pic['image'] = img
    toarray = np.asarray(img)
    print(toarray)

    grayscale_title = tk.Label(frame, text='Edited:', padx=25, pady=25,
                                      font=('verdana',16))
    grayscale_title.grid(row=3, column=0)

    grayscale = Image.open(filename)
    grayscale = grayscale.convert("L")
    grayscale = grayscale.resize((200,200), Image.ANTIALIAS)
    grayscale = ImageTk.PhotoImage(grayscale)
    grayscale_pic['image'] = grayscale


    bw = Image.open(filename)
    bw = bw.convert("1")
    bw = bw.resize((200,200), Image.ANTIALIAS)
    bw = ImageTk.PhotoImage(bw)
    bw_pic['image'] = bw



browse['command'] = selectPic    

frame.pack()



browse.grid(row=1, column=0, columnspan="1", padx=10, pady=10)
show_pic.grid(row=2, column=0, columnspan="2")
grayscale_pic.grid(row=4, column=0, columnspan="2")
bw_pic.grid(row=4, column=4, columnspan="2")


root.mainloop()