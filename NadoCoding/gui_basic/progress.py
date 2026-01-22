from tkinter import *
import tkinter.ttk as ttk
import time 
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

days = [str(i) + "일" for i in range(1,32)]

# progress = ttk.Progressbar(root, maximum=100, mode = "indeterminate")
p_var2 = DoubleVar()
progress2 = ttk.Progressbar(root, maximum=100,length=200, variable=p_var2)

progress2.pack()

def prg() : 
   for i in range(1,101) :
        time.sleep(0.01)
        p_var2.set(i)
        progress2.update()
def change() :
   progress2.stop()

btn = Button(root, text = "Change", command=prg)

btn.pack()
root.mainloop()