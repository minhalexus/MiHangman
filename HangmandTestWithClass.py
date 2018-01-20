from tkinter import *
from hangman import hangman

class MyWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Hello, world")
        label.pack()

class MyMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        menu = Menu(self)
        master.config(menu=menu)

        subMenu = Menu(menu)
        # Adds a drop down when "File" is clicked
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New Project...")
        subMenu.add_command(label="Restart")
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command= self.quit())

    def quit(self, event=None):
        sys.exit()

root = Tk()
root.wm_title('Hangman')
MyWindow(root).pack()
MyMenu(root).pack()
root.mainloop()