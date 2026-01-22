from tkinter import *
import tkinter.messagebox as msg
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

bt1 = Button(root, text = "버튼1")

bt2 = Button(root, text = "버튼2")

bt3 = Button(root, text = "버튼3")

bt1.grid(row=0, column=1,sticky = N+E+W+S)

bt2.grid(row=0, column=2,sticky = N+E+W+S)


bt3.grid(row=3, column=1,columnspan=2,sticky = N+E+W+S)

root.mainloop()