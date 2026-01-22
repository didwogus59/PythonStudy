from tkinter import *
import merge
class RunFrame :
    def __init__(self, root, onStart, onProgress) :
        self.onProgress = onProgress
        self.onStart = onStart
        self.option = None
        self.frame = LabelFrame(root, text = "Run")
        self.frame.pack(fill= "x", expand=True)

        clsBt = Button(self.frame, text = "Close", padx = 5, pady = 3, width=12)
        clsBt.pack(side = "right", padx = 5, pady = 5)

        runBt = Button(self.frame, text = "Run", padx = 5, pady = 3, width=12, command= self.start)
        runBt.pack(side = "right", padx = 5, pady = 5)

    def start(self) :
        option, path, files = self.onStart()
        merge.mergeImage(path, option, files, self.onProgress)


