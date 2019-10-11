import tkinter as tk

class SatWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        theTk = tk.Tk()

        self.Description = tk.Label(theTk, text='Enter your SAT info:')
        self.Description.pack()

        firstEntry = tk.Entry(theTk)
        firstEntry.pack()
        