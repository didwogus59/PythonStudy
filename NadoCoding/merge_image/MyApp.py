from tkinter import *
from MainLayout import *
class MyApp :
    def __init__(self) :
        self.root = Tk()
        self.root.title("MY APP")
        self.root.title("Nano Gui")
        self.root.geometry("500x600+300+100")
        self.root.resizable(False, False)
        MainLayout(self.root)
    def run(self) :
        self.root.mainloop()

app = MyApp()
app.run()