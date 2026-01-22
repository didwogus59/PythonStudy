from tkinter import *
from os import *
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

chked = IntVar()
chk = Checkbutton(root, text = "CHECKED", variable=chked)
chk.pack()

chked2 = IntVar()
def change() :
    print(chked.get())
    if chked.get() == 0 :
        chk.select()
    else :
        chk.deselect()

btn = Button(root, text = "Change", command=change)

btn.pack()
root.mainloop()