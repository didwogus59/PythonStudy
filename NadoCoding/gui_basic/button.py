from tkinter import *
from os import *
root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

# root.resizable(False, False)

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=20, text = "버튼2222222222222222222")
btn2.pack()

# pad 안에 글자에 붙는 여백
btn3 = Button(root, padx=20, pady=5, text = "버튼333333\n333333333")
btn3.pack()

# 버튼크기 설정
btn4 = Button(root, width=10, height=10, text = "버튼4")
btn4.pack()


btn5 = Button(root, fg = "red",bg="green", width=10, height=10, text = "버튼4")
btn5.pack()


photo = PhotoImage(file = "gui_basic/test.png")

# btn6 = Button(root, image = photo)
# btn6.pack()
def btnCmd() :
    print("CLICK")

btn7 = Button(root, text = "WORK", command=btnCmd)
btn7.pack()

root.mainloop()