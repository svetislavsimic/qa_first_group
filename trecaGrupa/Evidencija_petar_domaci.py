import tkinter as tk
import datetime


class App:
    def __init__(self, filename=None):
        self.win = tk.Tk()
        self.filename = filename
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()
        self.var1.set("Ucenik1")
        self.var2.set("Ucenik2")
        self.var3.set("Ucenik3")
        self.var4.set("Ucenik4")
        self.var5.set("Ucenik5")
        self.status1 = tk.IntVar()
        self.status2 = tk.IntVar()
        self.status3 = tk.IntVar()
        self.status4 = tk.IntVar()
        self.status5 = tk.IntVar()
        ram1 = tk.Frame(self.win).grid(row=0, column=0)
        self.lbl1 = tk.Label(ram1, textvariable=self.var1).grid(row=0, column=0)
        self.lbl2 = tk.Label(ram1, textvariable=self.var2).grid(row=0, column=1)
        self.lbl3 = tk.Label(ram1, textvariable=self.var3).grid(row=0, column=2)
        self.lbl4 = tk.Label(ram1, textvariable=self.var4).grid(row=0, column=3)
        self.lbl5 = tk.Label(ram1, textvariable=self.var5).grid(row=0, column=4)
        self.chb1 = tk.Checkbutton(ram1, var=self.status1).grid(row=1, column=0)
        self.chb2 = tk.Checkbutton(ram1, var=self.status2).grid(row=1, column=1)
        self.chb3 = tk.Checkbutton(ram1, var=self.status3).grid(row=1, column=2)
        self.chb4 = tk.Checkbutton(ram1, var=self.status4).grid(row=1, column=3)
        self.chb5 = tk.Checkbutton(ram1, var=self.status5).grid(row=1, column=4)
        self.btn11 = tk.Button(ram1, command=self.savedata, text="Save").grid(row=2, column=2)
        self.datum = datetime.datetime.now()
        print(self.datum)
        self.namn = []
        print()
        self.win.mainloop()

    def savedata(self):
        if self.status1.get() == 1:
            self.namn.append(self.var1.get())
        if self.status2.get() == 1:
            self.namn.append(self.var2.get())
        if self.status3.get() == 1:
            self.namn.append(self.var3.get())
        if self.status4.get() == 1:
            self.namn.append(self.var4.get())
        if self.status5.get() == 1:
            self.namn.append(self.var5.get())
        with open("data.txt", "a") as f:
            f.write("Datum: {}\n Pristuni: {}\n\n".format(self.datum, self.namn))


App()
