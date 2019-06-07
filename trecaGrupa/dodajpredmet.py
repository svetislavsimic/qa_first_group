from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('evidencija.db')
cur = con.cursor()

class AddPredmet(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Dodaj Predmet")
        self.resizable(False, False)

        # ----------Frames------------------------------------------------------

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file='icons/dodajpredmet.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text='Dodaj Predmet', font='arial 22 bold',
                        fg='#003f8a')
        heading.place(x=290, y=60)

        # -------------Entries and Labels-----------------------------------------

        # predmet
        self.lbl_predmet = Label(self.bottomFrame, text='Predmet:', font='arial 15 bold',
                              fg='white', bg='#fcc324'
                              )
        self.lbl_predmet.place(x=40, y=40)
        self.ent_predmet = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_predmet.insert(0, '')
        self.ent_predmet.place(x=150, y=45)

        # profesor
        self.lbl_profesor = Label(self.bottomFrame, text='Profesor:', font='arial 15 bold',
                              fg='white', bg='#fcc324'
                              )
        self.lbl_profesor.place(x=40, y=80)
        self.ent_profesor = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_profesor.insert(0, '')
        self.ent_profesor.place(x=150, y=85)


        # button
        button = Button(self.bottomFrame, text='Dodaj Predmet', command=self.dodaj_predmet)
        button.place(x=270, y=200)

    def dodaj_predmet(self):
        pass
        # predmet = self.ent_predmet.get()
        # profesor = self.ent_profesor.get()
        # if (predmet and profesor !=""):
        #     try:
        #         query = "INSERT INTO 'PREDMETI' (NAZIV, PROFESOR) VALUES(?,?)"
        #         cur.execute(query(predmet, profesor))
        #         con.commit()
        #         messagebox.showinfo("Uspešno se dodali predmet", icon='info')
        #     except:
        #         messagebox.showerror("Error", "ne mogu dodati u bazu", icon='warning')
        # else:
        #     messagebox.showerror("Error", "Polja ne mogu biti prazna", icon='warning')

