from tkinter import *
import tkinter.ttk as ttk
class ProgressFrame :
    def __init__(self, root) :
        self.frame = LabelFrame(root, text = "Progress")
        self.frame.pack(fill= "x", expand=True)
        self.p_var = DoubleVar()
        self.bar = ttk.Progressbar(self.frame, maximum = 100, variable=self.p_var)
        self.bar.pack(fill = "x")

    def setProgress(self, progress) :
        self.p_var.set(progress)
        self.bar.update()
        pass