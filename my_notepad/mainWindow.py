import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.font as tkFont



win = tk.Tk()
customFont = tkFont.Font(family="Helvetica", size=14)

frame1 = tk.Frame(
    master = win,
    #background = 'maroon'
)
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    font = customFont,

)

editArea.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
editArea.focus_set()
win.mainloop()