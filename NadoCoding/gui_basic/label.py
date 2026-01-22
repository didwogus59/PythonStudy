from tkinter import *
from os import *
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

label1 = Label(root, text = "Hello")
label1.pack()

photo = PhotoImage(file  = "gui_basic/test.png")
photo = photo.subsample(5,5)

label2 = Label(root, image = photo)
label2.pack()

num = 0
def change() :
    global num
    num += 1
    label1.config(text = str(num))

btn = Button(root, text = "Change", command=change)

btn.pack()
root.mainloop()