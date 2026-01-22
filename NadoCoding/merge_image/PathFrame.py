from tkinter import *
from tkinter import filedialog
class PathFrame :
    def __init__(self, root) :
        self.frame = LabelFrame(root, text = "PATH")
        self.frame.pack(fill= "x", expand=True)

        self.text = Entry(self.frame)
        self.text.pack(side = "left" , fill = "x", expand = True, ipady = 4)
        
        btn = Button(self.frame, text = "Seacch", width = 10, command= self.selectPath)
        btn.pack(side = "right")

    def selectPath(self) :
        path = filedialog.askdirectory()
        if path :
            self.text.delete(0)
            self.text.insert(0,path)
    def getPath(self) :
        return self.text.get()