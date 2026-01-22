from tkinter import *
import tkinter.ttk as ttk

root = Tk()


root.title("Nano Gui")

root.geometry("500x500+200+200")

menu = Menu(root)

def create_new_file() :
    print("Created")

menu_file = Menu(root, tearoff=0)
menu_file.add_command(label = "New File", command=create_new_file)

menu_file.add_command(label = "New Window", command=create_new_file)
menu_file.add_separator()
menu_file.add_command(label = "Open File", command=create_new_file)
menu_file.add_command(label= "Save All", state = "disable")
menu_file.add_separator()
menu_file.add_command(label= "Exit", command=root.quit)

menu.add_cascade(label = "File",menu=menu_file)

menu.add_cascade(label = "Edit")

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="food1")
menu_lang.add_radiobutton(label="food2")
menu_lang.add_radiobutton(label="food3")

menu.add_cascade(label = "Menu", menu = menu_lang)

root.config(menu=menu)
root.mainloop()