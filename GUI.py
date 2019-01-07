try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import enhet


def init():
    mainWindow = tkinter.Tk()

    mainWindow.title("Manges Mekanik")
    mainWindow.geometry('640x480-100-200')
    mainWindow['padx'] = 8

    mainWindow.columnconfigure(0, weight=100)
    mainWindow.columnconfigure(1, weight=1)
    mainWindow.columnconfigure(2, weight=100)
    mainWindow.columnconfigure(3, weight=1)
    mainWindow.columnconfigure(4, weight=1000)
    mainWindow.columnconfigure(5, weight=1000)
    mainWindow.columnconfigure(6, weight=1000)
    mainWindow.columnconfigure(7, weight=1000)
    mainWindow.columnconfigure(8, weight=1000)
    mainWindow.columnconfigure(9, weight=1000)
    mainWindow.columnconfigure(10, weight=1000)
    mainWindow.columnconfigure(11, weight=1000)
    mainWindow.columnconfigure(12, weight=1000)
    mainWindow.columnconfigure(13, weight=1000)
    mainWindow.columnconfigure(14, weight=1000)
    mainWindow.columnconfigure(15, weight=1000)
    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=3)
    mainWindow.rowconfigure(2, weight=1)
    mainWindow.rowconfigure(3, weight=3)
    mainWindow.rowconfigure(4, weight=3)
    mainWindow.rowconfigure(5, weight=3)
    mainWindow.rowconfigure(6, weight=3)
    mainWindow.rowconfigure(7, weight=3)
    mainWindow.rowconfigure(8, weight=3)
    mainWindow.rowconfigure(9, weight=3)
    mainWindow.rowconfigure(10, weight=3)
    mainWindow.rowconfigure(11, weight=3)
    mainWindow.rowconfigure(12, weight=3)

    return mainWindow


class HuvudMeny(tkinter.Frame):

    def topMeny(self):
        top = self.winfo_toplevel()
        self.menuBar = tkinter.Menu(top)
        top['menu'] = self.menuBar

        self.menu_1 = tkinter.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Vilken beräkning', menu=self.menu_1)
        self.menu_1.add_cascade(label="Spänning (Normalkraft)")
        self.menu_1.add_cascade(label="Förlängning (Normalkraft)")
        self.menu_1.add_cascade(label="Begränsad area")
        self.menu_1.add_cascade(label="Genomsnittlig")
        self.menu_1.add_cascade(label="Spänning kring y-axeln")
        self.menu_1.add_cascade(label="Spänning kring z-axeln")

        self.menuBar.add_command(label='Beräkna', command=Berakna)

        self.menu_2 = tkinter.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Visa lösningsförslag', menu=self.menu_2)
        self.menu_2.add_command(label='About', command=Berakna)



def Berakna():
    langdVar = float(langd.get())
    qVar = float(q.get())
    xVar = float(x.get())

    resultat = MOS.UtbreddLast()

    result.delete(0, 100)
    result.insert(0, resultat.M_punktstod(qVar, langdVar, xVar))

    for i in range(1, 7):
        if globals()["check" + str(i) + "Value"].get() == 1:
            print("check" + str(i) + "Value")


# Visar egenskaper på vald profil #
def select_unit(self):
    selection = profilLista.curselection()
    value = profilLista.get(selection)

    egenskapsLista.delete(0, tkinter.END)
    egenskapsLista.insert(tkinter.END, selection)


mainWindow = init()
meny = HuvudMeny()
meny.topMeny()


### Lista med alla profiler ###
profilLista = tkinter.Listbox(mainWindow)
profilLista.grid(row=1, column=0, sticky='nsew', rowspan=1)
profilLista.config(border=2, relief='sunken')

### Initiates the list of units and creates 10 units ###
unit_database = enhet.Database()
for i in range(0, 10):
	unit_database.add_unit()

for units in unit_database.units: 	#Get the profiles in a list
    profilLista.insert(tkinter.END, units)

### listscroll for leftmost window ###
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=profilLista.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=1)
profilLista['yscrollcommand'] = listScroll.set


### Lista med den valda profilens egenskaper ###
egenskapsLista = tkinter.Listbox(mainWindow)
egenskapsLista.grid(row=1, column=2, sticky='nsew', rowspan=1)
egenskapsLista.config(border=2, relief='sunken')

# Scroll till egenskaperna #
egenskapScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=profilLista.yview)
egenskapScroll.grid(row=1, column=3, sticky='nsw', rowspan=1)
profilLista['yscrollcommand'] = egenskapScroll.set

profilLista.bind("<<ListboxSelect>>", select_unit)



### frame for the radio buttons ###
optionFrame = tkinter.LabelFrame(mainWindow, text="Vad ska beräknas?")
optionFrame.grid(row=1, column=4, sticky='ne')

check1Value = tkinter.IntVar()
check2Value = tkinter.IntVar()
check3Value = tkinter.IntVar()
check4Value = tkinter.IntVar()
check5Value = tkinter.IntVar()
check6Value = tkinter.IntVar()


# Radio buttons #
NormalLabel = tkinter.Label(optionFrame, text="Normalkraft")
check1 = tkinter.Checkbutton(optionFrame, text="Spänning (Normalkraft)", variable=check1Value)
check2 = tkinter.Checkbutton(optionFrame, text="Förlängning (Normalkraft)", variable=check2Value)
TvarsnittLabel = tkinter.Label(optionFrame, text="Tvärkraft")
check3 = tkinter.Checkbutton(optionFrame, text="Begränsad area", variable=check3Value)
check4 = tkinter.Checkbutton(optionFrame, text="Genomsnittlig", variable=check4Value)
MomentLabel = tkinter.Label(optionFrame, text="Moment / Böjning")
check5 = tkinter.Checkbutton(optionFrame, text="Spänning kring y-axeln", variable=check5Value)
check6 = tkinter.Checkbutton(optionFrame, text="Spänning kring z-axeln", variable=check6Value)
NormalLabel.grid(row=0, column=0, sticky='w')
check1.grid(row=1, column=0, sticky='w')
check2.grid(row=2, column=0, sticky='w')
TvarsnittLabel.grid(row=3, column=0, sticky='w')
check3.grid(row=4, column=0, sticky='w')
check4.grid(row=5, column=0, sticky='w')
MomentLabel.grid(row=6, column=0, sticky='w')
check5.grid(row=7, column=0, sticky='w')
check6.grid(row=8, column=0, sticky='w')

### inputs tll profilen ###

# q #
qLabel = tkinter.Label(mainWindow, text="q")
qLabel.grid(row=4, column=0, sticky='nw')

q = tkinter.Entry(mainWindow)
q.grid(row=5, column=0, sticky='sw')
q.insert(0, 10)


# Längd #
langdLabel = tkinter.Label(mainWindow, text="Längd")
langdLabel.grid(row=6, column=0, sticky='nw')

langd = tkinter.Entry(mainWindow)
langd.grid(row=7, column=0, sticky='sw')
langd.insert(0, 10)


# X #
XLabel = tkinter.Label(mainWindow, text="x")
XLabel.grid(row=8, column=0, sticky='nw')

x = tkinter.Entry(mainWindow)
x.grid(row=9, column=0, sticky='sw')
x.insert(0, 5)


### Resultatruta ###
resultLabel = tkinter.Label(mainWindow, text="Resultat")
resultLabel.grid(row=10, column=0, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=11, column=0, sticky='w')


### Buttons ###
beraknaButton = tkinter.Button(mainWindow, text="Beräkna", command=Berakna)
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)

beraknaButton.grid(row=12, column=14, sticky='we')
cancelButton.grid(row=12, column=15, sticky='we')



if __name__ == "__main__":
    mainWindow.mainloop()
