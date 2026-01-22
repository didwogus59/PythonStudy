from tkinter import *
from os import *
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

txt = Text(root, width=30, height=20)
txt.pack()
txt.insert(END, "Hello")

entry = Entry(root, width=30)
entry.pack()
entry.insert(0, "한줄용")
def change() :
    print(txt.get("1.0", END))#1 첫번째 로우 0은 0번쨰 컬럼
    print(entry.get())
    txt.delete("1.0",END)
    entry.delete(0, END)

btn = Button(root, text = "Change", command=change)

btn.pack()
root.mainloop()