# -*- coding:utf-8 -*-
from tkinter import *

import Bdatos.basededatos as bd
from Vistas.McListDemo import  MCListDemo
from Vistas.Util_tk import Util, MiLabel, MiBoton


class TestUbicacion(Frame):

    def __init__(self, master):
        Frame.__init__(self, master = master)
        self.pack(expand =1, fill = BOTH)

        '''se define los campos que contendra la ventana'''
        self.cedula = None
        self.write = None
        self.read = None
        self.listen = None
        self.speak = None

        '''Se escribe el Titulo'''
        self.text = Label(self, text="Matriculacion - Ubicacion", font=("Times", 20, "bold")).grid(row=0, sticky=N)

        " Se definen los label con sus correspondiente entrys"
        MiLabel(self, text="Cedula *:").grid(row=2, sticky=W)
        MiLabel(self, text="Cargue el puntaje hecho en cada examen*:").grid(row=4, sticky=W)
        MiLabel(self, text="Modulo Write *:").grid(row=5, sticky=W)
        MiLabel(self, text="Modulo Read *:").grid(row=6, sticky=W)
        MiLabel(self, text="Modulo Listen *:").grid(row=7, sticky=W)
        MiLabel(self, text="Modulo Speak *:").grid(row=8, sticky=W)

        '''Boton para evaluar el curso'''
        self.btn = MiBoton(self, text="Calcular", command=self.tomar_test)
        self.btn.grid(row=9, rowspan=1, sticky="nw")

        self.btn = MiBoton(self, text="Cancelar", command=self.limpiar_campos)
        self.btn.grid(row=9, rowspan=2, sticky="ne")


       # self.content = MCListDemo(self, 'vacio')

        self.get_cedula()
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

    def get_write(self):
        if not self.write:
            self.write = Entry(master=self, width=20)
            self.write.grid(row=5, sticky=E)
        return self.write

    def get_read(self):
        if not self.read:
            self.read = Entry(master=self, width=20)
            self.read.grid(row=6, sticky=E)
        return self.read

    def get_listen(self):
        if not self.listen:
            self.listen = Entry(master=self, width=20)
            self.listen.grid(row=7, sticky=E)
        return self.listen

    def get_speak(self):
        if not self.speak:
            self.speak = Entry(master=self, width=20)
            self.speak.grid(row=8, sticky=E)
        return self.speak

    def limpiar_campos(self):
        self.get_cedula().delete(0, END)
        self.get_write().delete(0, END)
        self.get_read().delete(0, END)
        self.get_listen().delete(0, END)
        self.get_speak().delete(0, END)

    def validar_campos(self,w,r,l,s):
        if w.isdigit() and r.isdigit() and l.isdigit() and s.isdigit():
            return True
        else:
            messagebox.showinfo("", "Campos Vacios")
        return False


    def tomar_test(self):
        """Permite tomar un Test de Ubicacion al alumno."""
        c = self.get_cedula().get()
        w = self.get_write().get()
        r = self.get_read().get()
        l = self.get_listen().get()
        s = self.get_speak().get()

        if (c.isdigit and w.isdigit() and r.isdigit() and l.isdigit() and s.isdigit() ):
            try:
                self.p = Util.get_posicion_in_list(c)
                if Util.validar_puntajes(w, r, l, s):
                    self.alumno = bd.total_estudiantes[self.p]

                    if (self.alumno.estado == 1 and self.alumno.cursoActual ==None) : # 1->>Activo o ya realizo test

                        '''Agrega las notas en el Test de Curso'''
                        notas = {"write": w, "read": r, "listen": l, "speak": s}
                        resul = self.alumno.tomar_test_ubicacion(self.p, notas)  # puntaje 81.25
                        self.opcion = self.evaluar_resul(resul)  # retorna 'basico' 'intermedio' 'avanzado'

                        messagebox.showinfo("Resultados del Test: ", "Total de Pts ->>"+ str(resul) + "\n" + str(self.get_obs(resul)))

                        '''Se escribe el Titulo'''
                        self.cadena = 'INSCRIPCION'
                        self.text = Label(self, text=self.cadena, font=("Times", 10, "bold")).grid(row=11, sticky=N)
                        '''MI boton '''
                        self.btn = MiBoton(self, text="Matricular", command=self.inscribir_alumno)
                        self.btn.grid(row=9, rowspan=2, sticky="n")
                        '''Se cargan los cursos habilitados '''

                        self.content = MCListDemo(self, str(self.opcion))

                    else:
                        messagebox.showinfo("INFO", "Este alumno ya hizo test de Ubicacion "
                                                        "\n o esta desactivado")
            except:
                messagebox.showinfo("Error", "Cedula no registrada")
        else:
            messagebox.showinfo("Error", "Ingrese numerico para todos los campos")



    def cancelar(self):
        self.limpiar_campos()

    def evaluar_resul(self, resul):
        int(resul)
        if (resul <= 74): return 'basico'
        if (resul >= 75 and resul <= 94): return 'intermedio'
        if (resul >= 95): return 'avanzado'

    def get_obs(self, resul):
        int(resul)
        if (resul <= 74): return ('Nivel de Ingles ->> Basico')
        if (resul >= 75 and resul <= 94): return ('Nivel de Ingles ->> Intermedio')
        if (resul >= 95): return ('Nivel de Ingles ->> Avanzado')

    def get_lista_correcta(self):
        if self.opcion == 'basico':
            return bd.cursosbasicos
        elif self.opcion == 'intermedio':
            return bd.cursosintermedios
        elif self.opcion == 'avanzado':
            return bd.cursosavanzados



    def inscribir_alumno(self):
        try:
            selected_item = self.content.selecion_item()  # get first column (nombre_curso)
            lista = self.get_lista_correcta()

            if selected_item is not None:

                #get_position of student in list
                for pos, item in enumerate(lista):
                    if str(item.nombre) == str(selected_item):
                        break

                if (Util.no_esta_inscripto(self.alumno.cedula)): #true
                    texto = self.alumno.set_curso(pos, self.opcion, self.alumno)

                    nombre_curso = str(self.alumno.get_course())
                    #print("texto", texto +nombre_curso)  # inscripcion realizada

                    if (messagebox.askyesno("?", "Se aplicara descuento?")):
                        try:
                            bd.total_estudiantes[self.p].tipo = 1
                            resul = self.alumno.set_cuota(self.p)
                        except:
                            print("no hubo set de cuota")
                    else:
                        bd.total_estudiantes[self.p].tipo = 0
                        resul = self.alumno.set_cuota(self.p)
                    messagebox.showinfo("INFO", texto + nombre_curso)
                    self.limpiar_campos()

                else:
                    messagebox.showinfo("INFO", " Alumno ya inscripto!")
            else:
                messagebox.showinfo("INFO", " No existe")
        except:
            messagebox.showinfo("INFO", "Seleccione un curso")






