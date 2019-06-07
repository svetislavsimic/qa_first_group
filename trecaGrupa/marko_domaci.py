from tkinter import *
from tkinter import ttk
import sqlite3
import dodajpredmet, dodajstudenta

''' TO DO :
    
    Potrebno završiti rad sa bazom i logikom aplikacije'''

con = sqlite3.connect('evidencija.db')
cur = con.cursor()
# con.execute('''CREATE TABLE PREDMETI (ID INT PRIMARY KEY NOT NULL,
#                                       NAZIV TEXT NOT NULL,
#                                       PROFESOR TEXT NOT NULL);''')

class Main(object):
    def __init__(self, master):
        self.master = master

        # frames
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # top frames
        topFrame = Frame(
            mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN,
            borderwidth=2
        )
        topFrame.pack(side=TOP, fill=X)

        # center frame
        centerFrame = Frame(mainFrame, width=1350, relief=RIDGE, bg='#e0f0f0', height=680)
        centerFrame.pack(side=TOP)

        # center left frame
        centerLeftFrame = Frame(
            centerFrame, width=900, height=700, bg='#0f0f0f', borderwidth=2, relief=SUNKEN
        )
        centerLeftFrame.pack(side=LEFT)

        # center right frame
        centerRightFrame = Frame(
            centerFrame, width=450, height=700, bg='#0f0f0f', borderwidth=2, relief=SUNKEN
        )
        centerRightFrame.pack()

        # search bar
        search_bar = LabelFrame(centerRightFrame, width=440, height=175,
                                text='', bg='#9bc9ff'
                                )
        search_bar.pack(fill=BOTH)
        self.lbl_search = Label(search_bar, text='', font='arial 12 bold',
                                bg='#9bc9ff', fg='white'
                                )
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search = Entry(search_bar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text='Traži', font='arial 12',
                                 bg='#fcc324', fg='white'
                                 )
        self.btn_search.grid(row=0, column=4, padx=10, pady=10)

        # list bar
        list_bar = LabelFrame(centerRightFrame, width=440, height=175,
                              text='', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='', font='times 16 bold',
                         fg='#2488ff', bg='#fcc324'
                         )
        lbl_list.grid(row=0, column=1,)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='Svi Predmeti', var=self.listChoice,
                          value=1, bg='#fcc324'
                          )
        rb2 = Radiobutton(list_bar, text='Ne odslušani Predmeti', var=self.listChoice,
                          value=1, bg='#fcc324'
                          )
        rb3 = Radiobutton(list_bar, text='Odlušani Predmeti', var=self.listChoice,
                          value=1, bg='#fcc324'
                          )
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='Prikazi', bg='#2488ff', fg='white',
                          font='arial 12'
                          )
        btn_list.grid(row=2, column=1, padx=40, pady=10)

        # naslov i slika
        image_bar = Frame(centerRightFrame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text='IT_BootCamp',
                                 font='arial 16 bold'
                                 )
        self.title_right.grid(row=0)
        self.img_bootcamp = PhotoImage(file='icons/bootcamp.png')
        self.lblImg = Label(image_bar, image=self.img_bootcamp)
        self.lblImg.grid(row=1)

# --------------------------- Tool Bar -------------------------------------------------
        # dodaj predmet
        self.iconbook = PhotoImage(file='icons/predmet_gore.png')
        self.btnpredmet = Button(
            topFrame, text='Dodaj Predmet', image=self.iconbook, compound=LEFT,
            font='arial 12 bold', command=self.dodaj_predmet
        )
        self.btnpredmet.pack(side=LEFT, padx=10)

        # dodaj studenta
        self.iconstudent = PhotoImage(file='icons/users.png')
        self.btnstudent = Button(topFrame, text='Dodaj Studenta',
                                 font='arial 12 bold', padx=10, command=self.dodaj_studenta)
        self.btnstudent.configure(image=self.iconstudent, compound=LEFT)
        self.btnstudent.pack(side=LEFT)

        # slušao predmet
        self.iconslusao = PhotoImage(file='icons/uho.png')
        self.btnslusao = Button(
            topFrame, text='Slušao Predmet', font='arial 12 bold', padx=10,
            image=self.iconslusao, compound=LEFT
        )
        self.btnslusao.pack(side=LEFT)

# --------------------- Tabs -----------------------------------------------------------

        # ----------------Tab 1-----------------------------------------

        self.tabs = ttk.Notebook(centerLeftFrame, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/sat.png')
        self.tab2_icon = PhotoImage(file='icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Evidencija Časova', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistika', image=self.tab2_icon, compound=LEFT)

        # predmeti
        self.list_predmeti = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_predmeti.grid(row=0, column=0, padx=(10, 0), pady=0, sticky=N)
        self.sb.config(command=self.list_predmeti.yview)
        self.list_predmeti.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N+S+E)

        # detalji
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        # ------------Tab 2--------------------------------------------

        # statistika
        self.lbl_predmeti_zbroj = Label(self.tab2, text="lbl_predmeti_zbroj",
                                        pady=20, font='verdana 14 bold'
                                        )
        self.lbl_predmeti_zbroj.grid(row=0)
        self.lbl_studenti_zbroj = Label(self.tab2, text="lbl_studenti_zbroj",
                                        pady=20, font='verdana 14 bold'
                                        )
        self.lbl_studenti_zbroj.grid(row=1, sticky=W)
        self.lbl_uzeti_zbroj = Label(self.tab2, text="lbl_uzeti_zbroj",
                                     pady=20, font='verdana 14 bold'
                                     )
        self.lbl_uzeti_zbroj.grid(row=2, sticky=W)

    def dodaj_predmet(self):
        add = dodajpredmet.AddPredmet()


    def dodaj_studenta(self):
        student = dodajstudenta.DodajStudenta()


def main():
    root = Tk()
    app = Main(root)
    root.title("Evidencija Časova")
    root.geometry("1350x750+350+200")
    root.mainloop()


if __name__ == '__main__':
    main()

