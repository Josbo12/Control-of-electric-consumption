#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *

class Tkinter(object):

        def __init__(self):
            super(Tkinter, self).__init__()

            #Inicialitzem la finestra emb les mides i el titol

            self.app1 = Tk()
            self.app1.title("Control del consum electric")
            self.app1.geometry("500x300")


            #Insertem el text de les instruccions a seguir
            texto="""Instruccions d'us:
                     Primer de tot
                     despressi has entes
                     prem continuar"""
            self.lbl = Label(self.app1,text=texto, justify= CENTER, pady=15)
            self.lbl.pack()

            #Boto per continuar despres de llegir les instruccions
            self.boto = Button(self.app1,text="Continuar",command=self.tipus_instalacio)
            self.boto.pack()

            self.app1.mainloop()


        def tipus_instalacio(self):

            #Destruim el boto anterior i canviem el text
            self.amagar_finestra("app1")
            self.nova_finestra()



            #self.boto.destroy()
            text = "Escull el tipus d'instalació"
            self.lbl = Label(self.app2,text=text, justify= CENTER, pady=15)
            self.lbl.pack()

            #Crear dos botons mes per a eleccio del tipus d'instalacio
            self.boto_mono = Button(self.app2,text="Monofasic",command=self.monofasic)
            self.boto_tri = Button(self.app2,text="Trifasic",command=self.trifasic)
            #self.boto_tri.place(x=310,y=50)
            #self.boto_mono.place(x=210,y=50)
            self.boto_mono.pack()
            self.boto_tri.pack(side=RIGHT)


        def monofasic(self):


            self.destruir_finestra("app2")
            self.nova_finestra()

            text = "Escull el nombre de linies a mesurar:"
            self.lbl = Label(self.app2,text=text, justify= CENTER, pady=15)
            self.lbl.pack()

            self.selec = IntVar()

            self.radiobutton1 = Radiobutton(self.app2,text="Una linia", value=1, variable=self.selec, command=self.eleccio_base_dades)
            self.radiobutton2 = Radiobutton(self.app2,text="Dos linies", value=2, variable=self.selec, command=self.eleccio_base_dades)
            self.radiobutton3 = Radiobutton(self.app2,text="Tres linies", value=3, variable=self.selec, command=self.eleccio_base_dades)
            self.radiobutton1.pack()
            self.radiobutton2.pack()
            self.radiobutton3.pack()
            #self.radiobutton1.place(x=260,y=100)
            #self.radiobutton2.place(x=260,y=150)
            #self.radiobutton3.place(x=260,y=200)

            #self.boto_cont = Button(self.app2,text="Continuar",command=self.eleccio_base_dades)
            #self.boto_cont.place(x=260,y=250)
            #self.monofasic = True


        def trifasic(self):

            self.boto_mono.destroy()
            self.boto_tri.destroy()
            self.selec = 3

            self.eleccio_base_dades()

        def eleccio_base_dades(self):

            #Això nomès passar
            if self.monofasic == True:

                self.boto_cont.destroy()
                self.radiobutton1.destroy()
                self.radiobutton2.destroy()
                self.radiobutton3.destroy()



            self.lbl.config(text="Especifica el nom de la base de dades\n i de cada linia de mesura:")

            self.lbl_bd = Label(self.app1,text="Base de dades:")
            self.lbl_bd.place(x=100, y=50)
            self.entradabase = StringVar()
            self.txtbase = Entry(self.app1, textvariable=self.entradabase)
            self.txtbase.place(x=200, y=50)


            self.boto_comen = Button(self.app1,text="Començar",command=self.lectura_dades)
            self.boto_comen.place(x=400, y=250)

            #self.boto_enrere = Button(self.app,text="Anterior",command=self.monofasic)
            #self.boto_enrere.place(x=50, y=250)




            if self.selec <= 3:

                self.lbl_pin1 = Label(self.app1,text="Pinça 1:")
                self.lbl_pin1.place(x=100, y=100)
                self.entrada1 = StringVar()
                self.txtpin1 = Entry(self.app1, textvariable=self.entrada1)
                self.txtpin1.place(x=200, y=100)


            if self.selec != 1:

                self.lbl_pin2 = Label(self.app1,text="Pinça 2:")
                self.lbl_pin2.place(x=100, y=125)

                self.entrada2 = StringVar()
                self.txtpin2 = Entry(self.app1, textvariable=self.entrada2)
                self.txtpin2.place(x=200, y=125)

            if self.selec == 3:

                self.lbl_pin3 = Label(self.app1,text="Pinça 3:")
                self.lbl_pin3.place(x=100, y=150)

                self.entrada3 = StringVar()
                self.txtpin3 = Entry(self.app1, textvariable=self.entrada1)
                self.txtpin3.place(x=200, y=150)




        def lectura_dades():
            pass

        def nova_finestra(self):

            self.app2 = Tk()
            self.app2.title("Control del consum electric")

        def destruir_finestra(self, finestra):

                if finestra == "app1":
                    self.app1.destroy()
                if finestra == "app2":
                    self.app2.destroy()
                #if finestra == "app3":
                #    self.app3.destroy()
                #if finestra == "app4":
                #    self.app4.destroy()

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
        c.tipus_instalacio()
