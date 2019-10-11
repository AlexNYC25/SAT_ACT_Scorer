import tkinter as tk

class SatWindow():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        