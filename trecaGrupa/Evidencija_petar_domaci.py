import tkinter as tk
import datetime


class App:
    def __init__(self, filename=None):
        self.win = tk.Tk()
        self.filename = filename
        self.status1 = tk.IntVar()
        self.status2 = tk.IntVar()
        self.status3 = tk.IntVar()
        self.status4 = tk.IntVar()
        self.status5 = tk.IntVar()
        ram1 = tk.Frame(self.win).grid(row=0, column=0)
        self.lbl1 = tk.Label(ram1, text="Ucenik 1").grid(row=0, column=0)
        self.lbl2 = tk.Label(ram1, text="Ucenik 2").grid(row=0, column=1)
        self.lbl3 = tk.Label(ram1, text="Ucenik 3").grid(row=0, column=2)
        self.lbl4 = tk.Label(ram1, text="Ucenik 4").grid(row=0, column=3)
        self.lbl5 = tk.Label(ram1, text="Ucenik 5").grid(row=0, column=4)
        self.chb1 = tk.Checkbutton(ram1, var=self.status1).grid(row=1, column=0)
        self.chb2 = tk.Checkbutton(ram1, var=self.status2).grid(row=1, column=1)
        self.chb3 = tk.Checkbutton(ram1, var=self.status3).grid(row=1, column=2)
        self.chb4 = tk.Checkbutton(ram1, var=self.status4).grid(row=1, column=3)
        self.chb5 = tk.Checkbutton(ram1, var=self.status5).grid(row=1, column=4)
        self.btn11 = tk.Button(ram1, command=self.savedata, text="Save").grid(row=2, column=2)
        self.datum = datetime.datetime.now()
        print(self.datum)
        self.namn = []
        self.win.mainloop()

    def savedata(self):
        if self.status1.get() == 1:
            self.namn.append("Ucenik1")
        if self.status2.get() == 1:
            self.namn.append("Ucenik2")
        if self.status3.get() == 1:
            self.namn.append("Ucenik3")
        if self.status4.get() == 1:
            self.namn.append("Ucenik4")
        if self.status5.get() == 1:
            self.namn.append("Ucenik5")
        with open("data.txt", "a") as f:
            f.write("Datum: {}\n Pristuni: {}\n\n".format(self.datum, self.namn))


App()
