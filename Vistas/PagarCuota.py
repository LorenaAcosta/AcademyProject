# -*- coding:utf-8 -*-
from tkinter import *

import Bdatos.basededatos as bd
from Vistas.McListDemo import  MCListDemo
from Vistas.Util_tk import Util, MiLabel, MiBoton


class PagarCuota(Frame):

    def __init__(self, master):
        Frame.__init__(self, master = master)
        self.pack(expand =1, fill = BOTH)

        '''se define los campos que contendra la ventana'''
        self.cedula = None

        '''Se escribe el Titulo'''
        self.text = Label(self, text="Pago de mensualidad", font=("Times", 20, "bold")).grid(row=0, sticky=N)

        " Se definen los label con sus correspondiente entrys"
        MiLabel(self, text="CDI *:").grid(row=1, sticky=W)

        '''Boton para evaluar el curso'''
        self.btn = MiBoton(self, text="Buscar", command=self.buscar)
        self.btn.grid(row=1, column = 2,  sticky="e")

        self.get_cedula()

    def get_cedula(self):
        if not self.cedula:
            self.cedula = Entry(master=self, width=20)
            self.cedula.grid(row=1, sticky=E)
            self.cedula.focus()
        return self.cedula

    def limpiar_campos(self):
        self.get_cedula().delete(0, END)

    def cobrar(self):
        try:
            fila = self.content.get_item_raw()  # get fila
            nro_cuota = self.content.selecion_item()  # get first column (nro_cuota)
            if Util.es_ultima_cuota(self.alu, nro_cuota):
                resul = self.alu.pagarCuotas(int(nro_cuota-1))
                self.content.eliminar_fila(fila)
                messagebox.showinfo("Resultado", resul )
            else:
                messagebox.showinfo("INFO", "Seleccione la ultima cuota")
        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")


    def buscar(self):
        """Permite tomar un Test de Ubicacion al alumno."""
        c = self.get_cedula().get()

        if ( c.isdigit() and Util.verificar_estudiante(int(c))):
            try:
                self.p = Util.get_posicion_in_list(c)
                self.alu = bd.total_estudiantes[self.p]

                if (self.alu.cursoActual is not None):

                    MiLabel(self, text="Estudiante:"+ self.alu.nombre + self.alu.apellido).grid(row=3, sticky=W)
                    MiLabel(self, text="Curso:" + self.alu.get_course()).grid(row=4, sticky=W)

                    self.btn = MiBoton(self, text="Cobrar", command=self.cobrar)
                    self.btn.grid(row=4, rowspan=1, sticky="e")
                    self.content = MCListDemo(self, 'cuotas')
                    self.content.cargar_item(self.alu.get_cuotas())

                else:
                    messagebox.showinfo("Error", "No esta inscripto a ningun curso")
            except:
                messagebox.showinfo("Error", "Cedula no registrada")
        else:
            messagebox.showinfo("Error", "Cedula no registrada")



    def cancelar(self):
        self.limpiar_campos()


