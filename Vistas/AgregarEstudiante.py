from tkinter import *
from tkinter import ttk

import Bdatos.basededatos as bd
from Clases.Contacto import Contacto
from Clases.Persona import Estudiante
from Vistas.Util_tk import Util, MiLabel, MiBoton


class AgregarEstudiante(Frame):
    ''' ventana agregar Estudiante'''

    def __init__(self, master):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)


        '''se define los campos que contendra la ventana'''
        self.cedula = None
        self.nombre = None
        self.apellido = None
        self.direccion = None
        self.telefono =None
        self.celular = None
        self.email = None


        '''Se escribe el Titulo'''
        self.text = Label(self, text="Estudiantes", font=("Times", 20, "bold")).grid(row=0, sticky=N)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=1, sticky=W+E )

        " se definen los label con sus correspondiente entrys"
        MiLabel(self, text="Cedula Identidad*:").grid(row=2,  sticky=W)
        MiLabel(self, text="Nombre Completo :").grid(row=3, sticky=W)
        MiLabel(self, text="Apellido Completo :").grid(row=4, sticky=W)
        MiLabel(self, text="Direccion :").grid(row=5, sticky=W)
        MiLabel(self, text="Telefono  :").grid(row=6, sticky=W)
        MiLabel(self, text="Celular :").grid(row=7, sticky=W)
        MiLabel(self, text="Correo Electronico:").grid(row=8, sticky=W)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=10,  sticky="ew")


        '''Boton para guardar al estudiante'''
        self.btn = MiBoton(self, text="Guardar", command=self.guardarEstudiante)
        self.btn.grid(row=12,  column=0,  sticky="e")
        self.btn = MiBoton(self, text="Cancelar", command=self.limpiar_campos)
        self.btn.grid(row=12, column=1, sticky="w")

        '''Frame de listar datos'''
        #self.content = MCListDemo(self, 'estudiante')


        self.get_cedula()
        self.get_nombre()
        self.get_apellido()
        self.get_direccion()
        self.get_telefono()
        self.get_celular()
        self.get_email()


    def get_cedula(self):
        if not self.cedula:
            self.cedula = Entry(master=self, width=20)
            self.cedula.grid(row=2,  column=1)
            self.cedula.focus()
        return self.cedula

    def get_nombre(self):
        if not self.nombre:
            self.nombre = Entry(master=self, width=20)
            self.nombre.grid(row=3,  column=1)
        return self.nombre

    def get_apellido(self):
        if not self.apellido:
            self.apellido = Entry(master=self, width=20)
            self.apellido.grid(row=4,  column=1)
        return self.apellido

    def get_direccion(self):
        if not self.direccion:
            self.direccion = Entry(master=self, width=20)
            self.direccion.grid(row=5, column=1)
        return self.direccion

    def get_telefono(self):
        if not self.telefono:
            self.telefono = Entry(master=self, width=20)
            self.telefono.grid(row=6,  column=1)
        return self.telefono

    def get_celular(self):
        if not self.celular:
            self.celular = Entry(master=self, width=20)
            self.celular.grid(row=7,  column=1)
        return self.celular

    def get_email(self):
        if not self.email:
            self.email = Entry(master=self, width=20)
            self.email.grid(row=8,  column=1)
        return self.email



    def cancelar(self):
        if (self.master):
            self.master.destroy()

    def limpiar_campos(self):
        self.get_cedula().delete(0, END)
        self.get_nombre().delete(0, END)
        self.get_apellido().delete(0, END)
        self.get_direccion().delete(0, END)
        self.get_telefono().delete(0, END)
        self.get_celular().delete(0, END)
        self.get_email().delete(0, END)

    def validar_campos(self, nom, ape, dire, email):
        if nom != "" and ape != "" and dire!= "":
            if  Util.val_email(email):
                return True
        else:
            messagebox.showinfo("", "Campos incorrectos")
        return False


    def guardarEstudiante(self):
        try:
            ced = self.get_cedula().get()
            nom = self.get_nombre().get()
            ape = self.get_apellido().get()
            dire = self.get_direccion().get()
            tel = self.get_telefono().get()
            cel = self.get_celular().get()
            email = self.get_email().get()

            if (self.validar_campos(nom, ape, dire, email)): #cmapos cadena
                if (Util.validar_cedula(ced) and Util.validar_contacto(tel, cel)): #campos numericos
                    if (Util.verificar_estudiante(ced)):
                        messagebox.showinfo("Error", "Estudiante ya registrado!")
                    else:
                        self.contacto = Contacto(tel, cel, email)
                        bd.total_estudiantes.append(Estudiante(**{"cedula": ced, "nombre": nom,
                                                                  "apellido": ape, "direccion": dire,
                                                                  "contacto": self.contacto}))
                        messagebox.showinfo("Correcto", "Datos Guardados")
#                        self.content.cargar_item((ced, nom, ape, dire))
                        self.limpiar_campos()

        except ValueError:
            messagebox.showinfo("Error", "Datos no validos")








