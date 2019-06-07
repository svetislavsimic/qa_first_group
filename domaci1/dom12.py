import  tkinter as tk
import tkinter.ttk as ttk

def Srpski():
    rezultat=unosSrpski.get().split(',')
    rezultat=[float(x) for x in rezultat]
    rezultatSrpski.set(sum(rezultat) / float(len(rezultat)))

def Matematika():
    rezultat=unosMatematika.get().split(',')
    rezultat=[float(x) for x in rezultat]
    rezultatMatematika.set(sum(rezultat) / float(len(rezultat)))

def Istorija():
    rezultat=unosIstorija.get().split(',')
    rezultat=[float(x) for x in rezultat]
    rezultatIstorija.set(sum(rezultat) / float(len(rezultat)))

def Prosek():
    rezultat=int(prosekSrpski.get() + float(prosekMatematika.get() + prosekIstorija.get()) / int(3)
    prosekSvih.set(rezultat)

def Izvrsi():
    Srpski()
    Matematika()
    Istorija()
    Prosek()

root=tk.Tk()

srpskiFrame=ttk.Frame(root, padding="0 0 0 0")
matematikaFrame=ttk.Frame(root, padding="0 0 0 0")
istorijaFrame=ttk.Frame(root, padding="0 0 0 0")
dugmeFrame=ttk.Frame(root, padding="0 0 0 0")

srpskiLabela=ttk.Label(srpskiFrame, text='Srpski')
matematikaLabela=ttk.Label(matematikaFrame, text='Matematika')
istorijaLabela=ttk.Label(istorijaFrame, text='Istorija')
dugmeLabela=ttk.Label(dugmeFrame, text='Rezultat')

unosSrpski=tk.StringVar()
unosMatematika=tk.StringVar()
unosIstorija=tk.StringVar()

rezultatSrpski=tk.StringVar()
rezultatMatematika=tk.StringVar()
rezultatIstorija=tk.StringVar()

srpskiEntry=ttk.Entry(srpskiFrame, textvariable=unosSrpski)
matematikaEntry=ttk.Entry(matematikaFrame, textvariable=unosMatematika)
istorijaEntry=ttk.Entry(istorijaFrame, textvariable=unosIstorija)

prosekSrpski=ttk.Label(srpskiFrame, textvariable=rezultatSrpski)
prosekMatematika=ttk.Label(matematikaFrame, textvariable=rezultatMatematika)
prosekIstorija=ttk.Label(istorijaFrame, textvariable=rezultatIstorija)
prosekSvih=ttk.Label(dugmeFrame)

dugmeIzracunaj=ttk.Button(dugmeFrame, text='Izvrsi', textvariable=Izvrsi)

srpskiFrame.pack()
matematikaFrame.pack()
istorijaFrame.pack()
dugmeFrame.pack()

srpskiLabela.grid(column=0, row=0)
srpskiEntry.grid(column=1, row=0)
prosekSrpski.grid(column=2, row=0)

matematikaLabela.grid(column=0, row=1)
matematikaEntry.grid(column=1, row=1)
prosekMatematika.grid(column=2, row=1)

istorijaLabela.grid(column=0, row=2)
istorijaEntry.grid(column=1, row=2)
istorijaEntry.grid(column=1, row=2)

dugmeLabela.grid(column=0, row=3)
prosekSvih.grid(column=1, row=3)
dugmeIzracunaj.grid(column=2, row=3)

