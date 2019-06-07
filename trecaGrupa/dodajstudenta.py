from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('evidencija.db')
cur = con.cursor()

class DodajStudenta(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Dodaj Studenta")
        self.resizable(False, False)

        # ----------Frames------------------------------------------------------

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file='icons/addperson.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text='Dodaj Studenta', font='arial 22 bold',
                        fg='#003f8a')
        heading.place(x=290, y=60)

        # -------------Entries and Labels-----------------------------------------

        # student name
        self.lbl_name = Label(self.bottomFrame, text='Ime i prezime:', font='arial 15 bold',
                              fg='white', bg='#fcc324'
                              )
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, '')
        self.ent_name.place(x=180, y=45)

        # broj indexa
        self.lbl_index = Label(self.bottomFrame, text='Broj Indexa:', font='arial 15 bold',
                              fg='white', bg='#fcc324'
                              )
        self.lbl_index.place(x=40, y=80)
        self.ent_index = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_index.insert(0, '')
        self.ent_index.place(x=180, y=85)


        # button
        button = Button(self.bottomFrame, text='Dodaj', command=self.dodaj_studenta)
        button.place(x=270, y=120)

    def dodaj_studenta(self):
        pass


