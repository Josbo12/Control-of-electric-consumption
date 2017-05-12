#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
import Tkinter as tk
from tkFont import Font
import ttk
#import tkImage
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
            self.app1.geometry("800x480")
            #self.app1.configure(background="LightCyan4")
            self.fondo = PhotoImage(file="fondo.gif")
            self.lbl_Fondo = Label(self.app1, image=self.fondo).place(x=0,y=0)

            #TIpus i mides de lletres que utilitzarem
            self.myFont = Font(family="Verdana", size=16)
            self.myFont2 = Font(family="Verdana",weight="bold", size=20)

            #Insertem el text de les instruccions a seguir
            self.lbl = Label(self.app1,text=" Instruccions d'us:"
                             "\n\n  Primer de tot assegura't\n"
                             " de tenir conectades les pinces que utilitzaras.\n"
                             "  A la part superior de les pinces hi ha un fletxa\n"
                             " que s'ha de col·locar en direcció de la corrent"
                             ,justify=LEFT, font=self.myFont,bg="ivory2", fg="black"
                             ,padx=10, bd=2, relief=GROOVE)
            self.lbl.place(x=200,y=100)

            #Boto per continuar despres de llegir les instruccions
            self.boto = Button(self.app1,text="Continuar",font=self.myFont,command=self.tipus_instalacio,
                                bg="ivory2", bd=3, activebackground="light yellow",relief=RIDGE, overrelief=GROOVE )
            self.boto.place(x=350,y=400)


#############################################COMBOBOX############################################
            #cbx = ttk.Combobox(values=["uno", "dos", "tres", "cuatro", "cinco"])
            #cbx.set("uno")
            #cbx.configure(width=25)
            #cbx.pack()
            #cbx.master.title("ttk widgets")

            #Definim lestructura que tindra les lectures
            self.sensor1 = StringVar()
            self.sensor2 = StringVar()
            self.sensor3 = StringVar()
            self.sensor1.set("- - "+" W")
            self.sensor2.set("- -"+" W")
            self.sensor3.set("- -"+" W")

            #self.database.get_database()

            self.app1.mainloop()


        def tipus_instalacio(self):

            #Destruim finestra anterior i creem una nova
            self.amagar_finestra("app1")
            self.nova_finestra()


            text = "Escull el tipus d'instalació"
            self.lbl = Label(self.app2,text=text, justify= CENTER, font=self.myFont, bg="ivory2",padx=2)
            self.lbl.place(x=250, y=100)

            #Crear dos botons mes per a eleccio del tipus d'instalacio
            self.boto_mono = Button(self.app2,text="MONOFÀSIC",command=self.monofasic, bg="ivory2",
                                     bd=3, activebackground="light yellow",relief=RIDGE,
                                     overrelief=GROOVE, width=12, height=3, font=self.myFont2)
            self.boto_tri = Button(self.app2,text="TRIFÀSIC",command=self.trifasic, bg="ivory2",
                                     bd=3, activebackground="light yellow",relief=RIDGE,
                                     overrelief=GROOVE, width=12, height=3, font=self.myFont2)
            self.boto_mono.place(x=150,y=270)
            self.boto_tri.place(x=410,y=270)


        def monofasic(self):

            #Destruim finestra anterior i creem una nova
            self.destruir_finestra("app2")
            self.nova_finestra()

            def linies():

                #passem el valor obtingut a un enter i cridem la seguent funció
                aa = self.spin_linies.get()
                self.linies = int(aa)
                self.eleccio_base_dades()

            #Crear text i botons de la finestra
            text = "Escull el nombre de linies a mesurar:"
            self.lbl = Label(self.app2,text=text, font=self.myFont, justify= CENTER, pady=15)
            self.lbl.place(x=190,y=100)
            self.spin_linies = Spinbox(self.app2, font=self.myFont2, from_=1, to=3, width=10, borderwidth=2)
            self.spin_linies.place(x=280,y=200)
            self.boto_mono = Button(self.app2, text="Continuar", font=self.myFont, command=linies).place(x=325, y=300)


        def trifasic(self):

            #Defenim que a trifasic hi haurà 3 linies obligatories
            self.linies = 3
            self.eleccio_base_dades()


        def eleccio_base_dades(self):


            def crear_database():

                database = self.txtbase.get()
                self.database.create_database(database)
                self.boto_comen = Button(self.app2,text="Començar",command=self.lectura_dades)
                self.boto_comen.place(x=360,y=375)


            self.destruir_finestra("app2")
            self.nova_finestra()

            text = "Especifica el nom de la base de dades\n i de cada linia de mesura:"
            self.lbl = Label(self.app2,text=text, justify= CENTER, pady=15)
            self.lbl.place(x=290, y=25)

            self.lbl_bd = Label(self.app2,text="Base de dades:")
            self.lbl_bd.place(x=360,y=100)

            self.entradabase = StringVar()
            self.txtbase = Entry(self.app2, textvariable=self.entradabase)
            self.txtbase.place(x=325, y=125)
            self.boto_guardar = Button(self.app2,text="Guardar",command=crear_database)
            self.boto_guardar.place(x=375,y=150)

            if self.linies <= 3:

                self.lbl_pin1 = Label(self.app2,text="Pinça 1:")
                self.lbl_pin1.place(x=385,y=200)
                self.entrada1 = StringVar(self.app2, 'Pinça 1')
                self.txtpin1 = Entry(self.app2, textvariable=self.entrada1)
                self.txtpin1.place(x=325,y=225)


            if self.linies != 1:

                self.lbl_pin2 = Label(self.app2,text="Pinça 2:")
                self.lbl_pin2.place(x=385,y=250)

                self.entrada2 = StringVar(self.app2, 'Pinça 2')
                self.txtpin2 = Entry(self.app2, textvariable=self.entrada2)
                self.txtpin2.place(x=325,y=275)

            if self.linies == 3:

                self.lbl_pin3 = Label(self.app2,text="Pinça 3:")
                self.lbl_pin3.place(x=385,y=300)

                self.entrada3 = StringVar(self.app2, 'Pinça 3')
                self.txtpin3 = Entry(self.app2, textvariable=self.entrada3)
                self.txtpin3.place(x=325,y=325)


        def lectura_dades(self):

            self.destruir_finestra("app2")
            self.nova_finestra()

            if self.linies <= 3:
                self.linia1 = Label(self.app2,text=self.entrada1.get())
                self.linia1.pack()
                self.lectura1 = Label(self.app2,text=self.sensor1.get())
                self.lectura1.pack()

            if self.linies != 1:
                self.linia2 = Label(self.app2,text=self.entrada2.get())
                self.linia2.pack()
                self.lectura2 = Label(self.app2,text=self.sensor2.get())
                self.lectura2.pack()

            if self.linies == 3:
                self.linia1 = Label(self.app2,text=self.entrada3.get())
                self.linia1.pack()
                self.lectura3 = Label(self.app2,text=self.sensor3.get())
                self.lectura3.pack()

            self.actualitzar_dades()

        def actualitzar_dades(self):

                self.sensor.read_sensor()

                if self.linies <= 3:
                    self.sensor1.set(str(self.sensor.a)+" W")
                    self.lectura1.config(text=self.sensor1.get())
                if self.linies != 1:
                    self.sensor2.set(str(self.sensor.b)+" W")
                    self.lectura2.config(text=self.sensor2.get())
                if self.linies == 3:
                    self.sensor3.set(str(self.sensor.c)+" W")
                    self.lectura3.config(text=self.sensor3.get())

                self.app2.after(5000, self.actualitzar_dades)
                print "5 segons"



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        def nova_finestra(self):

            self.app2 =tk.Toplevel()
            self.app2.title("Control del consum electric")
            self.app2.geometry("800x480")
            self.fondo2 = PhotoImage(file="fondo.gif")
            self.lbl_Fondo2 = Label(self.app2, image=self.fondo2).place(x=0,y=0)


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
