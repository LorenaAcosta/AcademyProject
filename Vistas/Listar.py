from tkinter import *
from tkinter import ttk

import Bdatos.basededatos as bd
from Vistas.McListDemo import  MCListDemo
from Vistas.Util_tk import Util, MiBoton


class ListarEstudiantes(Frame):
    ''' ventana agregar Estudiante'''

    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)

        # label
        self.text = Label(self, text=titulo, font = ("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=1, sticky="ew")

        self.content = MCListDemo(self, opcion)

class ListarInscriptos(Frame):
    ''' ventana agregar Estudiante'''

    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)

        # label
        self.text = Label(self, text=titulo, font = ("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)

        self.btn = MiBoton(self, text="Desmatricular", command=self.desinscribir)
        self.btn.grid(row=16, rowspan=1, sticky="nw")
        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, sticky="ew")

        self.content = MCListDemo(self, opcion)

    def desinscribir(self):
        try:
            fila = self.content.get_item_raw()  # get fila
            cedula = self.content.selecion_item()  # get first column (cedula_estudiante)

            if cedula is not None:
                pos = Util.get_posicion_in_list(int(cedula))
                alumno = bd.total_estudiantes[pos]
                print(alumno.nombre)
                for i, var in enumerate(bd.inscriptos):
                    if int(var[0]) == int(alumno.cedula):
                        alumno.cursoActual = None
                        alumno.vectorCuotas = []
                        bd.inscriptos.pop(i)
                        self.content.eliminar_fila(fila)
                        messagebox.showinfo("INFO", "Alumno eliminado del curso")
            else:
                messagebox.showinfo("INFO", " No existe")

        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")


class ListarActivos(Frame):

    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)
        self.opcion = opcion

        # label
        self.text = Label(self, text=titulo, font = ("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)
        self.btn = MiBoton(self, text="Desactivar", command=self.desactivar)
        self.btn.grid(row=16, rowspan=1, sticky="nw")
        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, sticky="ew")

        self.content = MCListDemo(self, opcion)


    def desactivar(self):
        try:
            fila = self.content.get_item_raw() #get fila
            cedula = self.content.selecion_item()  # get first column (cedula_estudiante)

            if cedula is not None :
                pos = Util.get_posicion_in_list(int(cedula))
                alumno = bd.total_estudiantes[pos]
                print(alumno.nombre)

                if (alumno.cursoActual != None):
                    for i, var in enumerate(bd.inscriptos):
                        if int(var[0]) == int(alumno.cedula):
                            if (messagebox.askyesno("Salir", "Para desactivarlo "
                                                             "necesita desincribirlo "
                                                             "de su curso actual, "
                                                             "desea hacerlo ? ")):
                                alumno.cursoActual = None
                                bd.inscriptos.pop(i)
                                resp = alumno.deshabilitar(pos)
                                messagebox.showinfo("INFO", resp)
                                self.content.eliminar_fila(fila)
                else:
                    resp = alumno.deshabilitar(pos)
                    messagebox.showinfo("INFO", resp)
                    self.content.eliminar_fila(fila)
            else:
                messagebox.showinfo("INFO", " No existe")

        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")




class ListarInactivos(Frame):

    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)
        self.opcion = opcion

        # label
        self.text = Label(self, text=titulo, font = ("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)
        self.btn = MiBoton(self, text="Activar", command=self.activar)
        self.btn.grid(row=16, rowspan=1, sticky="nw")

        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, sticky="ew")

        self.content = MCListDemo(self, opcion)

    def activar(self):
        try:
            fila = self.content.get_item_raw() #get fila
            cedula = self.content.selecion_item()  # get first column (cedula_estudiante)

            if cedula is not None:
                pos = Util.get_posicion_in_list(int(cedula))
                self.alumno = bd.total_estudiantes[pos]
                print(self.alumno.nombre)
                try:
                    resp = self.alumno.habilitar(pos)
                    messagebox.showinfo("INFO", resp)
                    self.content.eliminar_fila(fila)

                except:
                    print("No registrado")
            else:
                messagebox.showinfo("INFO", " No existe")

        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")

class ListarBasicos(Frame):
    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)
        self.opcion = opcion

        # label
        self.text = Label(self, text=titulo, font=("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)

        self.btn = MiBoton(self, text="Borrar", command=self.eliminar)
        self.btn.grid(row=16, rowspan=1, sticky="nw")
        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, sticky="ew")

        self.content = MCListDemo(self, opcion)

    def eliminar(self):
        try:
            fila = self.content.get_item_raw()  # get fila
            nombre = self.content.selecion_item()  # get first column (curso_nombre)
            if nombre is not None:
                for i, valor in enumerate(bd.cursosbasicos):
                    if str(valor.nombre) == str(nombre):
                        print(valor.nombre)
                        print(i)
                        bd.cursosbasicos.pop(i)
                        break
                messagebox.showinfo("INFO", nombre +" Eliminado")
                self.content.eliminar_fila(fila)
            else:
                messagebox.showinfo("ERROR", "Ocurrio un error")

        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")

class ListarIntermedios(Frame):
    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)
        self.opcion = opcion

        # label
        self.text = Label(self, text=titulo, font=("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)

        self.btn = MiBoton(self, text="Borrar", command=self.eliminar)
        self.btn.grid(row=16, rowspan=1, sticky="nw")

        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, sticky="ew")

        self.content = MCListDemo(self, opcion)

    def eliminar(self):
        try:
            fila = self.content.get_item_raw()  # get fila
            nombre = self.content.selecion_item()  # get first column (curso_nombre)
            if nombre is not None:
                for i, valor in enumerate(bd.cursosintermedios):
                    if str(valor.nombre) == str(nombre):
                        print(valor.nombre)
                        print(i)
                        bd.cursosintermedios.pop(i)
                        break
                messagebox.showinfo("INFO", nombre +" Eliminado")
                self.content.eliminar_fila(fila)
            else:
                messagebox.showinfo("ERROR", "Ocurrio un error")

        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")

class ListarAvanzados(Frame):
    def __init__(self, master, titulo, opcion):
        Frame.__init__(self, master=master)
        self.pack(expand=1, fill=BOTH)
        self.opcion = opcion

        # label
        self.text = Label(self, text=titulo, font=("Times", 20, "bold"))
        self.text.grid(row=0, sticky=N)

        self.btn = MiBoton(self, text="Borrar", command=self.eliminar)
        self.btn.grid(row=16, rowspan=1, sticky="nw")

        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, sticky="ew")
        self.content = MCListDemo(self, opcion)

    def eliminar(self):
        try:
            fila = self.content.get_item_raw()  # get fila
            nombre = self.content.selecion_item()  # get first column (curso_nombre)
            if nombre is not None:
                for i, valor in enumerate(bd.cursosavanzados):
                    if str(valor.nombre) == str(nombre):
                        print(valor.nombre)
                        print(i)
                        bd.cursosavanzados.pop(i)
                        break
                messagebox.showinfo("INFO", nombre +" Eliminado")
                self.content.eliminar_fila(fila)
            else:
                messagebox.showinfo("ERROR", "Ocurrio un error")
        except:
            messagebox.showinfo("INFO", "Seleccione un elemento")