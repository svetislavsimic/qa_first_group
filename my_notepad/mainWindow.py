import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.font as tkFont
from tkinter import messagebox

class App:
    def __init__(self):
        self.win = tk.Tk()
        self.customFont = tkFont.Font(
            family="Helvetica", size=14
        )

        frame1 = tk.Frame(
            master=self.win,
            # background = 'maroon'
        )
        frame1.pack(fill='both', expand='yes')
        editArea = tkst.ScrolledText(
            master=frame1,
            wrap=tk.WORD,
            font=self.customFont,

        )

        editArea.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
        editArea.focus_set()

        menubar = tk.Menu(self.win)
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open",)
        filemenu.add_command(label="Save",)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Exit)
        menubar.add_cascade(label="File",  menu=filemenu)
        fontMenu=tk.Menu(menubar, tearoff=1)
        fontMenu.add_command(label="IncreaseFont", command=self.IncreaseFont)
        fontMenu.add_command(label="DecreaseFont", command=self.DecreaseFont)
        menubar.add_cascade(label="Font", menu=fontMenu)
        self.win.config(menu=menubar)


        self.win.mainloop()

    def IncreaseFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size + 2)

    def DecreaseFont(self):
        size = self.customFont['size']
        if size-2>0:
            self.customFont.configure(size=size - 2)

    def Exit(self):
        result = messagebox.askokcancel("Python","Would you like to save the data?")
        if result:
            self.win.destroy()
        else:
            pass


app=App()