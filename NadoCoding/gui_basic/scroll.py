from tkinter import *
import tkinter.messagebox as msg
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

frame = Frame(root)
frame.pack()
scroll = Scrollbar(frame)
scroll.pack(side = "right", fill = "y")
list = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand=scroll)

for i in range(1, 32) :
    list.insert(END, str(i) + "일")

scroll.config(command=list.yview)
list.pack(side = "left")
root.mainloop()