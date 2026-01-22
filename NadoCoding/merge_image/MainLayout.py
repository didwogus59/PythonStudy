from tkinter import *
from ButtonFrame import ButtonFrame
from ListFrame import ListFrame
from PathFrame import PathFrame
from OptionFrame import OptionFrame
from RunFrame import RunFrame
from ProgressFrame import ProgressFrame
class MainLayout :
    def __init__(self, root) :
        self.buttonFrame = ButtonFrame(root, self.onSelect, self.onDelete)
        self.listFrame = ListFrame(root)
        self.pathFrame = PathFrame(root)
        self.optionFrame = OptionFrame(root)
        self.progressFrame = ProgressFrame(root)
        self.runFrame = RunFrame(root, self.onStart, self.onProgress)
    
    def onSelect(self, files) :
        self.listFrame.addList(files)
    
    def onDelete(self) :
        self.listFrame.deleteList()

    def onStart(self) :
        return self.optionFrame.getOption(), self.pathFrame.getPath(), self.listFrame.getList()
    
    def onProgress(self, progress) :
        return self.progressFrame.setProgress(progress)
