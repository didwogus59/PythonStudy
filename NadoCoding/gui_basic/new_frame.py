from tkinter import *
import tkinter.messagebox as msg
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

f1 = Frame(root, relief="solid", bd = 1)
f1.pack(side = "left",fill="both", expand = True)

Button(f1, text = "food1").pack()
Button(f1, text = "food2").pack()
Button(f1, text = "food3").pack()

lf = LabelFrame(root, text = "Drink")
lf.pack(side = RIGHT, expand = True,fill="both",)
Button(lf, text = "soda").pack()
Button(lf, text = "coca").pack()

root.mainloop()