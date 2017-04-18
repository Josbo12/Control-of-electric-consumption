#!/usr/bin/python
from Tkinter import *

def tipus_instalacio():

    boto.destroy()
    lbl.config(text="Selecciona el tipus d'instalacio:")
    boto1 = Button(app,text="Monofasic",command=monofasic)
    boto1.place(x=100,y=50)
    boto2 = Button(app,text="Trifasic",command=trifasic)
    boto2.place(x=200,y=50)


def monofasic():
    lbl.config(text="Selecciona el nombre de linies que es mesuraran:")
    boto1 = Button(app,text="Acceptar",command=eleccio_base_dades)

def trifasic():
    pass

def eleccio_base_dades():
    pass

app = Tk()
app.title("Control del consum electric")
app.geometry("500x300")

#FP -> Finestra Principal
#vp = Frame(app)
#vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
 #vp.columnconfigure(0,weight=1)
 #vp.rowconfigure(0,weight=1)

texto="Instruccions d'us:\n Primer de tot "
lbl = Label(app,text=texto)
lbl.place(x=200,y=10)

boto = Button(app,text="Continuar",command=tipus_instalacio)
boto.place(x=210,y=50)



app.mainloop()
