#!/usr/bin/python
from Tkinter import *

class Tkinter(object):

        def __init__(self):
            super(Tkinter, self).__init__()


        def tipus_instalacio(self):

            self.boto.destroy()
            self.lbl.config(text="Selecciona el tipus d'instalacio:")

            self.boto_mono = Button(self.app,text="Monofasic",command=self.monofasic)
            self.boto_tri = Button(self.app,text="Trifasic",command=self.trifasic)
            self.boto_tri.place(x=310,y=50)
            self.boto_mono.place(x=210,y=50)


        def monofasic(self):
            selec = IntVar()
            self.radiobutton1 = Radiobutton(self.app,text="Una linia",variable=selec value=1)
            self.radiobutton2 = Radiobutton(self.app,text="Dos linies",variable=selec value=2)
            self.radiobutton3 = Radiobutton(self.app,text="Tres linies",variable=selec value=3)
            self.radiobutton1.place(x=260,y=100)
            self.radiobutton2.place(x=260,y=150)
            self.radiobutton3.place(x=260,y=200)
            self.boto_mono.destroy()
            self.boto_tri.destroy()
            self.lbl.config(text="Selecciona el nombre de linies que es mesuraran:")
            self.boto_dades_mono = Button(self.app,text="Continuar",command=self.eleccio_base_dades)
            self.boto_dades_mono.place(x=260,y=250)

        def trifasic(self):
            pass

        def eleccio_base_dades(self):

            if self.rad


        def create_window(self):

            self.app = Tk()
            self.app.title("Control del consum electric")
            self.app.geometry("500x300")


            texto="Instruccions d'us:\n Primer de tot "
            self.lbl = Label(self.app,text=texto)
            self.lbl.place(x=200,y=10)

            self.boto = Button(self.app,text="Continuar",command=self.tipus_instalacio)
            self.boto.place(x=210,y=50)



            self.app.mainloop()

if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = Tkinter()
        c.create_window()
