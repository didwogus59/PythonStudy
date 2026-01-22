from tkinter import *
import tkinter.messagebox as msg
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

def info() :
    msg.showinfo("알림", "으어어어어어")

def warn() :
    msg.showwarning("경고", "뿌에에에엨")

def error() :
    msg.showerror("에러", "끼에에에에엨")

def cancel() :
    res = msg.askokcancel("취소", "쫄????????????")
    print(res)
    
Button(root, command=info, text = "알림").pack()

Button(root, command=warn, text = "경고").pack()

Button(root, command=error, text = "에러").pack()

Button(root, command=cancel, text = "취소").pack()

root.mainloop()