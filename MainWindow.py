from tkinter import *
from SatWindow import *

# TODO: fix layout of buttons to center them more in the center, assign function to button

class MainWindow():

    def __init__(self):
        root = Tk()
        root.geometry("500x200")
        root.title("SAT and ACT score guide")

        greeting = Label(root, text="Hello User")
        greeting.pack( side="top")

        choice = Label(root, text="Which test do you need help scoring today")
        choice.pack(side="top")

        satButton = Button(root, text="SAT", width="10", height="5", padx="5", command=startSatWindow)
        actButton = Button(root, text="ACT", width="10", height="5", padx="5")

        satButton.pack(side="left")
        actButton.pack(side="right")
        root.mainloop()

    def create_window(self):
        window = tk.Toplevel(root)



def main():
    initial = MainWindow()

if __name__ == "__main__":
    main()

def startSatWindow():
    satWin = SatWindow()
    satWin.mainloop()