from tkinter import *

class Editor :
    def __init__(self):
        self.root = Tk()
        self.root.title("Nano Gui")
        self.root.geometry("500x500+200+200")
        # self.root.resizable(False, False)
        f1 = Frame(self.root, relief="solid", bd = 1)
        f1.pack(side = "left",fill="both", expand = True)

        
        scroll = Scrollbar(f1)
        scroll.pack(side="right", fill="y")

        self.txt = Text(f1, yscrollcommand=scroll.set)
        self.txt.pack(fill="both",expand=True)

        scroll.config(command=self.txt.yview)

        menu = Menu(self.root)
        menu_file = Menu(self.root, tearoff=0)
        menu_file.add_command(label = "New File", command=self.create_new_file)
        menu_file.add_command(label = "Read File", command=self.read_file)
        menu.add_cascade(label = "File",menu=menu_file)
        self.root.config(menu=menu)

    def create_new_file(self) :
        with open("editor.txt","w",encoding="utf8") as file :
            file.write(self.txt.get("1.0",END))

    def read_file(self) :
        with open("editor.txt","r",encoding="utf8") as file :
            self.txt.delete("1.0",END)
            self.txt.insert("1.0",file.read())
        
    def run(self) :
        self.root.mainloop()

edit = Editor()

edit.run()