#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
import Tkinter as tk
from tkFont import Font
import ttk
from tk_current_sensor import PowerServer
from database import Database
import time


class Tkinter(object):

        def __init__(self):
                super(Tkinter, self).__init__()

                #Inicialitzem la finestra emb les mides i el titol
                self.app1 = Tk()
                self.app1.title("Control del consum electric")
                self.app1.geometry("800x450")
                self.fondo = PhotoImage(file="fondo.gif")
                self.lbl_Fondo = Label(self.app1, image=self.fondo).place(x=0,y=0)

                #Importem les classes dels altres arxius
                self.database = Database()
                self.sensor = PowerServer()

                #TIpus i mides de lletres que utilitzarem
                self.myFont = Font(family="Verdana", size=16)
                self.myFont2 = Font(family="Verdana",weight="bold", size=20)
                self.myFont3 = Font(family="Verdana",weight="bold", size=26)
                self.myFont4 = Font(family="Verdana", size=12, weight="bold")

                #Definim les variables de lectura i la seva estructura
                self.sensor1 = StringVar()
                self.sensor2 = StringVar()
                self.sensor3 = StringVar()
                self.sensor1.set("- - "+" W")
                self.sensor2.set("- -"+" W")
                self.sensor3.set("- -"+" W")

                #Insertem el text de les instruccions a seguir
                lbl = Label(self.app1,text=" Instruccions d'us:"
                            "\n\n  Primer de tot assegura't\n"
                            " de tenir conectades les pinces que utilitzaras.\n"
                            "  A la part superior de les pinces hi ha un fletxa\n"
                            " que s'ha de col·locar en direcció de la corrent",
                             justify=LEFT, font=self.myFont,bg="khaki",
                             highlightbackground="gold3", highlightthickness=3, padx=10, )
                lbl.place(x=150,y=100)

                #Boto per continuar despres de llegir les instruccions
                boto_continuar = Button(self.app1,text="Continuar",font=self.myFont,command=self.tipus_instalacio,
                              bg="khaki", bd=3, activebackground="gold",relief=RIDGE, overrelief=GROOVE,
                              highlightbackground="gold3", highlightthickness=3 )
                boto_continuar.place(x=350,y=350)


                self.app1.mainloop()


        def tipus_instalacio(self):

                #Destruim finestra anterior i creem una nova
                self.amagar_finestra("app1")
                self.nova_finestra()

                #Nova etiqueta amb dos botons per elegir la instalació
                text = "Escull el tipus d'instalació"
                lbl = Label(self.app2,text=text, font=self.myFont, justify= CENTER, bg="khaki",
                                 padx=2,highlightbackground="gold", highlightthickness=3)

                boto_mono = Button(self.app2,text="MONOFÀSIC",font=self.myFont2, bg="khaki",
                                         bd=3, activebackground="gold",relief=RIDGE,
                                         overrelief=GROOVE, width=12, height=3, command=self.monofasic)

                boto_tri = Button(self.app2,text="TRIFÀSIC",font=self.myFont2, bg="khaki",
                                         bd=3, activebackground="gold",relief=RIDGE,
                                         overrelief=GROOVE, width=12, height=3, command=self.trifasic)

                lbl.place(x=250, y=100)
                boto_mono.place(x=150,y=270)
                boto_tri.place(x=410,y=270)


        def monofasic(self):

                #Destruim finestra anterior i creem una nova
                self.destruir_finestra("app2")
                self.nova_finestra()

                def linies():

                        #passem el valor obtingut a un enter i cridem la seguent funció
                        nlinies = self.spin_linies.get()
                        self.linies = int(nlinies)
                        self.eleccio_base_dades()


                #Etiqueta i Spin per escollir el nombre de linies monofàsiques a mesurar
                text = "Escull el nombre de linies a mesurar:"
                lbl = Label(self.app2, text=text, font=self.myFont, bg="ivory2",
                                justify= CENTER, pady=15)

                spin_linies = Spinbox(self.app2, font=self.myFont2, bg="ivory2",
                                from_=1, to=3, width=10, borderwidth=2)

                boto_continuar = Button(self.app2, text="Continuar", font=self.myFont,
                                bg="ivory2", command=linies)

                lbl.place(x=190,y=100)
                spin_linies.place(x=280,y=200)
                boto_continuar.place(x=325, y=300)


        def trifasic(self):

                #Defenim que a trifasic hi haurà 3 linies obligatories
                self.linies = 3
                self.eleccio_base_dades()


        def eleccio_base_dades(self):

                #Destruim finestra anterior i creem una nova
                self.destruir_finestra("app2")
                self.nova_finestra()

                def nova_database():

                        #Obtenim el valor entrat de la nova base de dades
                        self.base = self.txtbase.get()
                        #Creem la nova base de dades cridant la funcio de l'arxiu database.py
                        self.database.create_database(self.base)
                        #Cridar funció per seleccioar la base dades a utilitzar
                        llista_base_dades()


                def llista_base_dades():

                        #Actualitzem totes les bases de dades
                        self.database.get_database()

                        #Desplegable amb totes les bases de dades i boto per seleccionar
                        self.desplegable = ttk.Combobox(self.app2)
                        self.desplegable['values']=self.database.llista_databases

                        boto_utilitzar = Button(self.app2,text="Utilitzar", bg="gold2",command=vella_database,
                                                    highlightbackground="gold3", highlightthickness=3,
                                                    activebackground="gold")

                        self.desplegable.place(x=440,y=125)
                        boto_utilitzar.place(x=500,y=150)

                def vella_database():

                        #Obtenim el valor selecconat al desplegable i cridem a la seguent funció
                        self.base = self.desplegable.get()
                        crear_database()


                def crear_database():

                        #Creem la base de dades per poderla utilitzar, amb el valor obtingut anterior
                        self.database.create_database(self.base)

                        #Boto per començar les lectures
                        boto_comen = Button(self.app2,text="Començar",command=self.lectura_dades,
                                                 highlightbackground="gold3", highlightthickness=3,
                                                 activebackground="gold", bg="gold2")

                        boto_comen.place(x=360,y=375)



                #Etiquetes, botons i entrades de text per escollir la base de dades
                text = "Especifica el nom de la base de dades\n i de cada linia de mesura:"
                lbl = Label(self.app2,text=text, bg="khaki", justify= CENTER, pady=15,
                                font=self.myFont4, highlightbackground="gold3", highlightthickness=3)

                #Variable a la qual assignarem el nom de la base de dades
                self.entradabase = StringVar()

                lbl_bd = Label(self.app2,text="Base de dades:", bg="khaki",
                                    highlightbackground="gold3", highlightthickness=3)

                #Entrada de text per la base de dades
                self.txtbase = Entry(self.app2, textvariable=self.entradabase, bg="ivory2")

                #Boto per crear la base de dades
                boto_crear = Button(self.app2,text="Crear", bg="gold2",command=nova_database,
                                            highlightbackground="gold3", highlightthickness=3,
                                            activebackground="gold")

                #Boto per escollir una base de dades ja guardada
                boto_escollir = Button(self.app2,text="Escolleix una ...", bg="gold2",command=llista_base_dades,
                                            highlightbackground="gold3", highlightthickness=3,
                                            activebackground="gold")

                lbl.place(x=220, y=15)
                lbl_bd.place(x=360,y=100)
                self.txtbase.place(x=200, y=125)
                boto_crear.place(x=200,y=150)
                boto_escollir.place(x=300,y=150)


                #Etiquetes i entrades de text per el nom de cada linia de mesura
                #segons les linies que s'hagin elegit anteriorment

                if self.linies <= 3:

                    lbl_pin1 = Label(self.app2,text="Pinça 1:",bg="khaki",
                                     highlightbackground="gold3", highlightthickness=3)

                    self.entrada1 = StringVar(self.app2, 'Pinça 1')

                    self.txtpin1 = Entry(self.app2, textvariable=self.entrada1, bg="ivory2")

                    lbl_pin1.place(x=385,y=200)
                    self.txtpin1.place(x=325,y=225)


                if self.linies != 1:

                    lbl_pin2 = Label(self.app2,text="Pinça 2:",bg="khaki",
                                     highlightbackground="gold3", highlightthickness=3)

                    self.entrada2 = StringVar(self.app2, 'Pinça 2')

                    self.txtpin2 = Entry(self.app2, textvariable=self.entrada2,  bg="ivory2")

                    lbl_pin2.place(x=385,y=250)
                    self.txtpin2.place(x=325,y=275)

                if self.linies == 3:

                    lbl_pin3 = Label(self.app2,text="Pinça 3:",bg="khaki",
                                          highlightbackground="gold3", highlightthickness=3)

                    self.entrada3 = StringVar(self.app2, 'Pinça 3')

                    self.txtpin3 = Entry(self.app2, textvariable=self.entrada3,  bg="ivory2")

                    lbl_pin3.place(x=385,y=300)
                    self.txtpin3.place(x=325,y=325)


        def lectura_dades(self):

            self.destruir_finestra("app2")
            self.nova_finestra()

            #Creem les etiquetes on es mostraran les dades en funcio de les linies elegides
            if self.linies <= 3:

                    linia1 = Label(self.app2,text=self.entrada1.get()+':',
                                   font=self.myFont3, highlightbackground="gold3",
                                   highlightthickness=5, bg="khaki")

                    self.lectura1 = Label(self.app2,text=self.sensor1.get(), font=self.myFont3,
                                     padx=50, highlightbackground="navy",
                                     highlightthickness=5, bg="LightBlue1")

                    linia1.place(x=100,y=100)
                    self.lectura1.place(x=400,y=100)

            if self.linies != 1:

                    linia2 = Label(self.app2,text=self.entrada2.get()+':',
                                   font=self.myFont3, highlightbackground="gold3",
                                highlightthickness=5, bg="khaki")

                    self.lectura2 = Label(self.app2,text=self.sensor2.get(), font=self.myFont3,
                                          padx=50, highlightbackground="navy",
                                          highlightthickness=5, bg="LightBlue1")

                    linia2.place(x=100, y=200)
                    self.lectura2.place(x=400, y=200)

            if self.linies == 3:

                    linia1 = Label(self.app2,text=self.entrada3.get()+':',
                                        font=self.myFont3, highlightbackground="gold3",
                                        highlightthickness=5, bg="khaki")

                    self.lectura3 = Label(self.app2,text=self.sensor3.get(), font=self.myFont3,
                                          padx=50, highlightbackground="navy",
                                          highlightthickness=5, bg="LightBlue1")

                    linia1.place(x=100, y=300)
                    self.lectura3.place(x=400, y=300)

            #Cridem la funció que ens mostrarà les lectures
            self.actualitzar_dades()

        def actualitzar_dades(self):

                #Cridem la funció per insertar les lectures a la base de dades
                self.database.insert_data()
                #Cridem la funció per obtenir les lectures del sensor
                self.sensor.read_sensor()

                #Actualitsem les dades amb les lectures actuals
                if self.linies <= 3:
                    self.sensor1.set(str(self.sensor.a)+" W")
                    self.lectura1.config(text=self.sensor1.get())
                if self.linies != 1:
                    self.sensor2.set(str(self.sensor.b)+" W")
                    self.lectura2.config(text=self.sensor2.get())
                if self.linies == 3:
                    self.sensor3.set(str(self.sensor.c)+" W")
                    self.lectura3.config(text=self.sensor3.get())

                #Eecutem aquesta funció cada x segons
                self.app2.after(5000, self.actualitzar_dades)





#///////////////////////////////////////////////////////////////////////////////////////////////////////

        def nova_finestra(self):

            #funció per crear la finestra
            self.app2 =tk.Toplevel()
            self.app2.title("Control del consum electric")
            self.app2.geometry("800x480")
            self.fondo2 = PhotoImage(file="fondo.gif")
            self.lbl_Fondo2 = Label(self.app2, image=self.fondo2).place(x=0,y=0)


        def destruir_finestra(self, finestra):

            #funció per destruir la finestra
            if finestra == "app1":
                self.app1.destroy()
            if finestra == "app2":
                self.app2.destroy()


        def amagar_finestra(self, finestra):

            #funció per amagar la fiestra
            if finestra == "app1":
                self.app1.withdraw()
            if finestra == "app2":
                self.app2.withdraw()

        def mostrar_finestra(self, finestra):

            #funció per mostrar la finestra
            if finestra == "app1":
                self.app1.deiconify()
            if finestra == "app2":
                self.app2.deiconify()



if __name__ == "__main__":

        print " 'Control of electric consumption' "
        c = Tkinter()
        c.monofasic()
