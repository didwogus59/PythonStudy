from tkinter import *
import tkinter.ttk as ttk
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

days = [str(i) + "일" for i in range(1,32)]

combo = ttk.Combobox(root, height=5,values=days)

combo.pack()
combo.set("일자")

combo2 = ttk.Combobox(root, height=16,values=days, state = "readonly")

combo2.pack()
combo2.set("일자")

def change() :
    print(chked.get())
    if chked.get() == 0 :
        chk.select()
    else :
        chk.deselect()

btn = Button(root, text = "Change", command=change)

btn.pack()
root.mainloop()