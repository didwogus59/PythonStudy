from tkinter import *
import tkinter.ttk as ttk
class OptionFrame :
    def __init__(self, root) :
        self.frame = LabelFrame(root, text = "Option")
        self.frame.pack(fill= "both", expand=True)

        size_width = Label(self.frame, text = "Width", width= 3)
        size_width.pack(side = "left", expand=True, fill="x")
        size_opt = ["Original", "1024", "800", "640"]
        self.size_cmb_width = ttk.Combobox(self.frame, state = "readonly", values = size_opt, width= 5)
        self.size_cmb_width.current(0)
        self.size_cmb_width.pack(side = "left", expand=True)

        gap_lbl_width = Label(self.frame, text = "Gap", width= 3)
        gap_lbl_width.pack(side = "left", expand=True, fill="x")
        gap_opt = ["ZERO", "Narrow", "Regular", "Wide"]
        self.gap_cmb_width = ttk.Combobox(self.frame, state = "readonly", values = gap_opt, width= 5)
        self.gap_cmb_width.current(0)
        self.gap_cmb_width.pack(side = "left", expand=True)

        fomat_lbl_width = Label(self.frame, text = "fomat", width= 3)
        fomat_lbl_width.pack(side = "left", expand=True, fill="x")
        fomat_opt = ["JPG", "PNG", "BMP"]
        self.fomat_cmb_width = ttk.Combobox(self.frame, state = "readonly", values = fomat_opt, width= 5)
        self.fomat_cmb_width.current(0)
        self.fomat_cmb_width.pack(side = "left", expand=True)
    
    def getOption(self) :
        return [self.size_cmb_width.current(), self.gap_cmb_width.current(), self.fomat_cmb_width.current()]