#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from tk_current_sensor import PowerServer
from database import Database
import time

class Tkinter(object):

        def __init__(self):
            super(Tkinter, self).__init__()

            #Inicialitzem la finestra emb les mides i el titol
            self.database = Database()
            self.sensor = PowerServer()
            self.app1 = Tk()
            self.app1.title("Control del consum electric")
            self.app1.geometry("500x300")


            #Insertem el text de les instruccions a seguir
            self.lbl = Label(self.app1,text="\n\ninstruccions d'us \nPrimer de tot \ndespres\nprem continuar",justify=LEFT)
            self.lbl.pack()

            #Boto per continuar despres de llegir les instruccions
            self.boto = Button(self.app1,text="Continuar",command=self.tipus_instalacio)
            self.boto.pack(pady=50)



            self.app1.mainloop()


        def tipus_instalacio(self):

            #Destruim el boto anterior i canviem el text
            self.amagar_finestra("app1")
            self.nova_finestra()

            text = "\nEscull el tipus d'instalació"
            self.lbl = Label(self.app2,text=text, justify= CENTER)
            self.lbl.pack()

            #Crear dos botons mes per a eleccio del tipus d'instalacio
            self.boto_mono = Button(self.app2,text="Monofasic",command=self.monofasic)
            self.boto_tri = Button(self.app2,text="Trifasic",command=self.trifasic)
            self.boto_mono.pack(side=LEFT, fill=Y, expand=YES, padx=70)
            self.boto_tri.pack(side=LEFT, fill=Y, expand=YES, padx=70)


        def monofasic(self):

            self.destruir_finestra("app2")
            self.nova_finestra()

            def linies():

                aa = self.spin_linies.get()
                self.linies = int(aa)
                self.eleccio_base_dades()


            text = "Escull el nombre de linies a mesurar:"
            self.lbl = Label(self.app2,text=text, justify= CENTER, pady=15)
            self.lbl.pack()

            self.spin_linies = Spinbox(self.app2, from_=1, to=3, width=10)
            self.spin_linies.pack()

            self.boto_mono = Button(self.app2,text="Continuar",command=linies)
            self.boto_mono.pack()



        def trifasic(self):

            self.linies = 3
            self.eleccio_base_dades()

        def eleccio_base_dades(self):


            def crear_database():

                database = self.txtbase.get()
                self.database.create_database(database)
                self.boto_comen = Button(self.app2,text="Començar",command=self.lectura_dades)
                self.boto_comen.pack()


            self.destruir_finestra("app2")
            self.nova_finestra()

            text = "Especifica el nom de la base de dades\n i de cada linia de mesura:"
            self.lbl = Label(self.app2,text=text, justify= CENTER, pady=15)
            self.lbl.pack()

            self.lbl_bd = Label(self.app2,text="Base de dades:")
            self.lbl_bd.pack()

            self.entradabase = StringVar()
            self.txtbase = Entry(self.app2, textvariable=self.entradabase)
            self.txtbase.pack()
            self.boto_guardar = Button(self.app2,text="Guardar",command=crear_database)
            self.boto_guardar.pack()

            if self.linies <= 3:

                self.lbl_pin1 = Label(self.app2,text="Pinça 1:")
                self.lbl_pin1.pack()
                self.entrada1 = StringVar(self.app2, 'Pinça 1')
                self.txtpin1 = Entry(self.app2, textvariable=self.entrada1)
                self.txtpin1.pack()


            if self.linies != 1:

                self.lbl_pin2 = Label(self.app2,text="Pinça 2:")
                self.lbl_pin2.pack()

                self.entrada2 = StringVar(self.app2, 'Pinça 2')
                self.txtpin2 = Entry(self.app2, textvariable=self.entrada2)
                self.txtpin2.pack()

            if self.linies == 3:

                self.lbl_pin3 = Label(self.app2,text="Pinça 3:")
                self.lbl_pin3.pack()

                self.entrada3 = StringVar(self.app2, 'Pinça 3')
                self.txtpin3 = Entry(self.app2, textvariable=self.entrada3)
                self.txtpin3.pack()


        def lectura_dades(self):

            self.destruir_finestra("app2")
            self.nova_finestra()

            self.sensor.read_sensor()


            if self.linies <= 3:
                self.lbl_pin1 = Label(self.app2,text=self.entrada1.get())
                self.lbl_pin1.pack()
                self.lbl_pin1 = Label(self.app2,text=self.sensor.a)
                self.lbl_pin1.pack()

            if self.linies != 1:
                self.lbl_pin1 = Label(self.app2,text=self.entrada2.get())
                self.lbl_pin1.pack()
                self.lbl_pin2 = Label(self.app2,text=self.sensor.b)
                self.lbl_pin2.pack()

            if self.linies == 3:
                self.lbl_pin1 = Label(self.app2,text=self.entrada3.get())
                self.lbl_pin1.pack()
                self.lbl_pin3 = Label(self.app2,text=self.sensor.c)
                self.lbl_pin3.pack()

            self.update()

        def actualizar_dades(self):

                self.sensor.read_sensor()

                if self.linies <= 3:
                    self.lbl_pin1.config(text=self.sensor.a)
                if self.linies != 1:
                    self.lbl_pin2.config(text=self.sensor.b)
                if self.linies == 3:
                    self.lbl_pin3.config(text=self.sensor.c)

                self.app2.after(5000, self.actualitzar_dades)





        def nova_finestra(self):

            self.app2 =Tk()
            self.app2.title("Control del consum electric")
            self.app2.geometry("500x300")

        def destruir_finestra(self, finestra):

            if finestra == "app1":
                self.app1.destroy()
            if finestra == "app2":
                self.app2.destroy()


        def amagar_finestra(self, finestra):

            if finestra == "app1":
                self.app1.withdraw()
            if finestra == "app2":
                self.app2.withdraw()

        def mostrar_finestra(self, finestra):

            if finestra == "app1":
                self.app1.deiconify()
            if finestra == "app2":
                self.app2.deiconify()


if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = Tkinter()
        c.monofasic()
