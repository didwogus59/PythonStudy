from tkinter import *
from os import *
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

chked = IntVar()


radio = Radiobutton(root, text="Food1", value = 1, variable=chked)
radio2 = Radiobutton(root, text="Food2", value = 2, variable=chked)
radio3= Radiobutton(root, text="Food3", value = 3, variable=chked)

radio.pack()
radio2.pack()
radio3.pack()

def change() :
    print(chked.get())
    if chked.get() == 0 :
        chk.select()
    else :
        chk.deselect()

btn = Button(root, text = "Change", command=change)

btn.pack()
root.mainloop()