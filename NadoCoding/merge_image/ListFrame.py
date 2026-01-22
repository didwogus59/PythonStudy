from tkinter import *
class ListFrame :
    def __init__(self, root) :
        self.frame = Frame(root)
        self.frame.pack(fill = "both", expand=True)

        scroll = Scrollbar(self.frame)
        scroll.pack(side = "right", fill = "y")

        self.files = Listbox(self.frame, selectmode = "extended", height= 15, yscrollcommand=scroll.set)
        self.files.pack(side = "left", fill= "both", expand = True)
        scroll.config()

    def addList(self, files) :
        for file in files :
            self.files.insert(END, file)
    
    def deleteList(self) :
        selected = self.files.curselection()
        for index in reversed(selected):
            self.files.delete(index)

    def getList(self) :
        return self.files.get(0, END)