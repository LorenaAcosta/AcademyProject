# -*- coding:utf-8 -*-
from tkinter import *

import Bdatos.basededatos as bd
from Vistas.McListDemo import MCListDemo
from Vistas.Util_tk import MiBoton
from Vistas.Util_tk import MiLabel
from Vistas.Util_tk import Util


class TestCurso(Frame):

    def __init__(self, master):
        Frame.__init__(self, master = master)
        self.pack(expand =1, fill = BOTH)

        '''se define los campos que contendra la ventana'''
        self.cedula = None
        self.write = None
        self.read = None
        self.listen = None
        self.speak = None
        self.redcarpets = None
        self.asistencia = None

        '''Se escribe el Titulo'''
        self.text = Label(self, text="Evaluacion Final de Curso", font=("Times", 20, "bold")).grid(row=0, sticky=N)

        " Se definen los label con sus correspondiente entrys"
        MiLabel(self, text="Cedula *:").grid(row=2, sticky=W)
        MiLabel(self, text="Cant.Red Carpets:").grid(row=3, sticky=W)
        MiLabel(self, text="Asistencia %*:").grid(row=4, sticky=W)
        MiLabel(self, text="Puntajes minimos requeridos para aprobar: *:").grid(row=5, sticky=W)
        MiLabel(self, text="Modulo Write *:").grid(row=6, sticky=W)
        MiLabel(self, text="Modulo Read *:").grid(row=7, sticky=W)
        MiLabel(self, text="Modulo Listen *:").grid(row=8, sticky=W)
        MiLabel(self, text="Modulo Speak *:").grid(row=9, sticky=W)

        '''Boton para evaluar el curso'''
        self.btn = MiBoton(self, text="Calcular", command=self.tomar_test)
        self.btn.grid(row=10, rowspan=1, sticky="nw")

        self.btn = MiBoton(self, text="Cancelar", command=self.limpiar_campos)
        self.btn.grid(row=10, rowspan=2, sticky="ne")

        '''Frame de listar datos
        self.content = MCListDemo(self, 'cursos_habilitados')
        '''

        self.get_cedula()
        self.get_redcarpets()
        self.get_asistencia()
        self.get_write()
        self.get_read()
        self.get_listen()
        self.get_speak()

    def get_cedula(self):
        if not self.cedula:
            self.cedula = Entry(master=self, width=20)
            self.cedula.grid(row=2, sticky=E)
            self.cedula.focus()
        return self.cedula

    def get_redcarpets(self):
        if not self.redcarpets:
            self.redcarpets = Entry(master=self, width=20)
            self.redcarpets.grid(row=3, sticky=E)
            self.redcarpets.focus()
        return self.redcarpets

    def get_asistencia(self):
        if not self.asistencia:
            self.asistencia = Entry(master=self, width=20)
            self.asistencia.grid(row=4, sticky=E)
            self.asistencia.focus()
        return self.asistencia

    def get_write(self):
        if not self.write:
            self.write = Entry(master=self, width=20)
            self.write.grid(row=6, sticky=E)
        return self.write

    def get_read(self):
        if not self.read:
            self.read = Entry(master=self, width=20)
            self.read.grid(row=7, sticky=E)
        return self.read

    def get_listen(self):
        if not self.listen:
            self.listen = Entry(master=self, width=20)
            self.listen.grid(row=8, sticky=E)
        return self.listen

    def get_speak(self):
        if not self.speak:
            self.speak = Entry(master=self, width=20)
            self.speak.grid(row=9, sticky=E)
        return self.speak

    def limpiar_campos(self):
        self.get_cedula().delete(0, END)
        self.get_redcarpets().delete(0, END)
        self.get_asistencia().delete(0, END)
        self.get_write().delete(0, END)
        self.get_read().delete(0, END)
        self.get_listen().delete(0, END)
        self.get_speak().delete(0, END)

    def validar_campos(self,c, redc, asis, w,r,l,s):
        val= False
        if (c.isdigit() and redc.isdigit() and asis.isdigit()
            and w.isdigit() and r.isdigit() and l.isdigit() and s.isdigit()):
            return True
        else:
            messagebox.showinfo("", "Campos Vacios")
        return False


    def tomar_test(self):
        ced = self.get_cedula().get()
        redc = self.get_redcarpets().get()
        asis = self.get_asistencia().get()
        w = self.get_write().get()
        r = self.get_read().get()
        l = self.get_listen().get()
        s = self.get_speak().get()

        """Permite tomar un Test de Ubicacion al alumno."""
        if (ced.isdigit() and redc.isdigit() and asis.isdigit() and
            w.isdigit() and r.isdigit() and l.isdigit() and s.isdigit()):
            try:
                pos = Util.get_posicion_in_list(ced)

                if Util.validar_puntajes(w, r, l, s) and Util.val_asistencia(asis, redc):
                    self.alumno = bd.total_estudiantes[pos]
                    ced= self.alumno.cedula

                    if (self.alumno.estado == 1 and self.alumno.cursoActual != None) : # 1->>Activo o ya realizo test
                        notas = {"write": w, "read": r, "listen": l, "speak": s, "asistencia": asis, "redcarpet": redc}
                        resul = self.alumno.tomar_test_curso(pos, notas)  # puntaje 81.25
                        value = str(self.get_resul(resul))
                        messagebox.showinfo("Resultados del Test: ", "Total de Pts ->>" + str(resul) + "\n" + value)

                        if (value == 'Curso Aprobado!'):
                            self.cadena = 'Inscribir a nuevo curso'
                            self.text = Label(self, text=self.cadena, font=("Times", 10, "bold")).grid(row=11, sticky=N)

                            self.btn = MiBoton(self, text="Inscribir", command=self.inscribir_alumno)
                            self.btn.grid(row=10, rowspan=2, sticky="n")

                            self.content = MCListDemo(self, 'curso')

                    else:
                        messagebox.showinfo("INFO", "No esta inscripto a curso  "
                                                        "\n o esta desactivado")
            except:
                messagebox.showinfo("Error", "Cedula no registrada")
        else:
            messagebox.showinfo("Error", "Ingrese numerico para todos los campos")



    def inscribir_alumno(self):
        try:
            nombre_curso = self.content.selecion_item()  # get first column (nombre_curso)
            print(nombre_curso)

            if nombre_curso is not None  :
                # get_position of course in list
                pos = Util.get_position(nombre_curso)

                if (Util.no_esta_inscripto(self.alumno.cedula)): #true
                    texto = self.alumno.set_curso(pos, self.opcion, self.alumno)
                    nombre_curso = str(self.alumno.get_course())
                    messagebox.showinfo("INFO", texto + nombre_curso)
                    self.limpiar_campos()
                else: #si esta inscripto
                    if (self.alumno.get_cuotas() != None):
                        messagebox.showinfo("INFO", 'Inscripcion denegada por mora en el pago de cuotas.')
                    else:
                        for i, item in enumerate(bd.inscriptos):
                            if (item[0] == self.alumno.cedula):
                                bd.inscriptos.pop(i)
                                break
                        opcion = Util.get_list(nombre_curso)
                        texto = self.alumno.set_curso(pos, opcion, self.alumno)
                        nombre_curso = str(self.alumno.get_course())
                        messagebox.showinfo("INFO", texto + nombre_curso)
                        self.limpiar_campos()

            else:
                messagebox.showinfo("INFO", " Alumno ya inscripto!")

        except:
            messagebox.showinfo("INFO", "Seleccione un curso")

    def cancelar(self):
        self.limpiar_campos()


    def get_resul(self, resul):
        if (resul >= 60):
            return("Curso Aprobado!")
        else:
            return("Curso No aprobado!")








