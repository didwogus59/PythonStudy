from tkinter import *
from tkinter import filedialog
class ButtonFrame :
    def __init__(self, root, onSelect, onDelete) :
        self.onDelete = onDelete
        self.onSelect = onSelect
        self.frame = Frame(root)
        self.frame.pack(fill= "x", expand=True)

        selectBt = Button(self.frame, text = "Select", padx = 5, pady = 3, width=12, command= self.SelectFile)
        selectBt.pack(side = "left", padx = 5, pady = 5)

        deleteBt = Button(self.frame, text = "Delete", padx = 5, pady = 3, width=12, command = self.DeleteFile)
        deleteBt.pack(side = "right", padx = 5, pady = 5)
    def SelectFile(self) :
        files = filedialog.askopenfilenames(title = "Select Image File", \
                                            filetypes= (("PNG File" , "*.png"), ("Every File" , "*.*")),\
                                            initialdir= "c:/study/python/CodeTest/image")
        if files :
            self.onSelect(files)

    def DeleteFile(self) :
        self.onDelete()