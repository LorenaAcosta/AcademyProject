# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import ttk
import Bdatos.basededatos as bd
from Clases.Curso import avanzado
from Clases.Curso import basico
from Clases.Curso import intermedio
from Vistas.Util_tk import MiLabel,  MiBoton


class AgregarCurso(Frame):
   '''Agregar/Eliminar un curso'''

   def __init__(self, master):
        Frame.__init__(self, master = master)
        self.pack(expand =1, fill = BOTH)

        '''se define los campos que contendra la ventana'''
        self.nombre = None
        self.duracion = None
        self.horario = None
        self.monto = None
        self.write = None
        self.read = None
        self.listen = None
        self.speak = None
        self.op = StringVar(self)
        self.op.set("basico")

        '''Se escribe el Titulo'''
        self.text = Label(self, text="Curso", font=("Times", 20, "bold")).grid(row=0, sticky=N)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=1, sticky=W + E)

        " Se definen los label con sus correspondiente entrys"
        MiLabel(self, text="Nivel del Curso").grid(row=7, column= 2,  sticky = E)
        option = OptionMenu(self, self.op, "basico", "intermedio", "avanzado")
        option.grid(row=8, column= 2,  sticky = E)

        MiLabel(self, text="Nombre *:").grid(row=7,sticky = W)
        MiLabel(self, text="Duracion: ").grid(row=8,sticky = W)
        MiLabel(self, text="Horario: ").grid(row=9, sticky = W)
        MiLabel(self, text="Costo Mensual: ").grid(row=10,sticky = W)
        MiLabel(self, text="Puntajes minimos requeridos para aprobar: *:").grid(row=11, sticky = W)
        MiLabel(self, text="Modulo Write *:").grid(row=12,sticky = W)
        MiLabel(self, text="Modulo Read *:").grid(row=13,sticky = W)
        MiLabel(self, text="Modulo Listen *:").grid(row=14,sticky = W)
        MiLabel(self, text="Modulo Speak *:").grid(row=15,sticky = W)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=17, sticky=W + E)

        '''B0ton para guardar/eliminar el curso'''
        self.btn = MiBoton(self, text="Guardar", command=self.add_course)
        self.btn.grid(row=19, rowspan=1, sticky="nw")
        self.btn = MiBoton(self, text="Cancelar", command=self.limpiar_campos)
        self.btn.grid(row=19, rowspan=2, sticky="e")

        '''Frame de listar datos'''
        #self.content = MCListDemo(self, 'curso')

        self.get_nombre()
        self.get_duracion()
        self.get_horario()
        self.get_monto()
        self.get_write()
        self.get_read()
        self.get_listen()
        self.get_speak()


   def get_nombre(self):
       if not self.nombre:
            self.nombre = Entry(master=self, width=20)
            self.nombre.grid(row=7, sticky = E)
            self.nombre.focus()
       return self.nombre

   def get_duracion(self):
       if not self.duracion:
            self.duracion = Entry(master=self, width=20)
            self.duracion.grid(row=8, sticky = E)
       return self.duracion

   def get_horario(self):
       if not self.horario:
            self.horario = Entry(master=self, width=20)
            self.horario.grid(row=9, sticky = E)
       return self.horario

   def get_monto(self):
       if not self.monto:
            self.monto = Entry(master=self, width=20)
            self.monto.grid(row=10, sticky = E)
       return self.monto

   def get_write(self):
       if not self.write:
            self.write = Entry(master=self, width=20)
            self.write.grid(row=12, sticky = E)
       return self.write

   def get_read(self):
       if not self.read:
            self.read = Entry(master=self, width=20)
            self.read.grid(row=13, sticky = E)
       return self.read

   def get_listen(self):
       if not self.listen:
            self.listen = Entry(master=self, width=20)
            self.listen.grid(row=14, sticky = E)
       return self.listen

   def get_speak(self):
       if not self.speak:
            self.speak = Entry(master=self, width=20)
            self.speak.grid(row=15, sticky = E)
       return self.speak

   def val_duracion(self, dur):
       val = False
       if dur.isdigit() and int(dur) <= 12:
           val = True
       else:
           messagebox.showinfo("", "La duracion es en  0meses. Numerico.")
       return val

   def val_monto(self, mon):
       val = False
       if mon.isdigit():
           val = True
       else:
           messagebox.showinfo("", "El monto debe ser solo numerico")
       return val

   def val_modulos(self, mod):
       val = False
       if mod.isdigit() and int(mod) <= 100:
           val = True
       else:
           messagebox.showinfo("", "El limite para puntajes es de 100 Pts.")
       return val


   def limpiar_campos(self):
        self.get_nombre().delete(0, END)
        self.get_duracion().delete(0, END)
        self.get_horario().delete(0, END)
        self.get_monto().delete(0, END)
        self.get_write().delete(0, END)
        self.get_read().delete(0, END)
        self.get_listen().delete(0, END)
        self.get_speak().delete(0, END)

   def get_lista_correcta(self, nombre):
        for var in bd.cursosbasicos:
            if str(var.nombre) == str(nombre):
                return bd.cursosbasicos
        for var in bd.cursosintermedios:
            if var.nombre == nombre:
                return bd.cursosintermedios
        for var in bd.cursosavanzados:
            if var.nombre == nombre:
                return bd.cursosavanzados

   def validar_campos(self, nom, hor):
       val = False
       if nom != "" and hor != "" :
           return True
       else:
           messagebox.showinfo("", "Campos Vacios")
       return False


    # operaciones para registar Cursos
    # --------------------------------------------------------------------------


   def add_course(self):
       self.nom = self.get_nombre().get()
       self.dur = self.get_duracion().get()
       self.hor = self.get_horario().get()
       self.mon = self.get_monto().get()
       self.w = self.get_write().get()
       self.r = self.get_read().get()
       self.l = self.get_listen().get()
       self.s = self.get_speak().get()

       if self.validar_campos(self.nom, self.hor):
           if self.val_duracion(self.dur) and self.val_monto(self.mon) and self.val_modulos(self.w) and \
               self.val_modulos(self.r) and self.val_modulos(self.l) and self.val_modulos(self.s):

               x = self.guardar(self.op.get())
               x()

               messagebox.showinfo("Correcto", "Datos Guardados")
               self.limpiar_campos()

   def guardar(self, lang):
       def es_basico():
           bd.cursosbasicos.append(
               basico(**{"nombre": self.nom, "duracion": self.dur, "horario": self.hor, "monto": self.mon,
                         "write": self.w, "read": self.r, "listen": self.l, "speak": self.s}))

       def es_avanzado():
           bd.cursosavanzados.append(
               avanzado(**{"nombre": self.nom, "duracion": self.dur, "horario": self.hor, "monto": self.mon,
                           "write": self.w, "read": self.r, "listen": self.l, "speak": self.s}))

       def es_intermedio():
           bd.cursosintermedios.append(
               intermedio(**{"nombre": self.nom, "duracion": self.dur, "horario": self.hor, "monto": self.mon,
                             "write": self.w, "read": self.r, "listen": self.l, "speak": self.s}))

       lang_func = {'basico': es_basico,
                    'intermedio': es_intermedio,
                    'avanzado': es_avanzado}
       return lang_func[lang]







