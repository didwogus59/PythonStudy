from tkinter import *
from os import *
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

listBox = Listbox(root, selectmode="extended", height=0)
listBox.insert(0,"1")
listBox.insert(2,"2")
listBox.insert(3,"3")
listBox.insert(END,"4")
listBox.insert(END,"5")
listBox.insert(END,"6")

listBox.pack()

def change() :
    listBox.delete(END)
    print("크기 : ", listBox.size())
    print("1~3번쨰 값  ",listBox.get(0,2))
    print("선택됨 : ",listBox.curselection())

btn = Button(root, text = "Change", command=change)

btn.pack()
root.mainloop()