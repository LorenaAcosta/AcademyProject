import webbrowser
from tkinter import *
from tkinter import messagebox

import Bdatos.store as Store
from Vistas.AgregarCurso import AgregarCurso
from Vistas.AgregarEstudiante import AgregarEstudiante
from Vistas.Listar import ListarBasicos,  ListarIntermedios, ListarAvanzados
from Vistas.Listar import ListarEstudiantes,  ListarActivos, ListarInactivos, ListarInscriptos
from Vistas.PagarCuota import PagarCuota
from Vistas.TomarTestCurso import TestCurso
from Vistas.TomarTestUbicacion import TestUbicacion


class MainMenu(Frame):
    '''Contiene la barra de menu principal'''
    ventanaActual = None

    def __init__(self, ventana):
        Frame.__init__(self, ventana, height = 800, width= 600, borderwidth = 5, relief = RIDGE)
        self.pack()
        self.ventana = ventana

        barraMenu = Menu(ventana)
        self.cargarDatos()


        """---------- menu Estudiante----------------"""
        menuStudent= Menu (barraMenu, tearoff=0)

        # se crea los submenus para estudiantes
        submenu_one = Menu(menuStudent)
        submenu_one.add_command(label="Todos", command=self.listar_todos)
       # submenu_one.add_command(label="Estudiantes con Descuento", command=self.listar_cd)
       #submenu_one.add_command(label="Estudiantes Sin Descuento", command=self.listar_sd)
        submenu_one.add_command(label="Estudiantes Activos", command=self.listar_ena)
        submenu_one.add_command(label="Estudiantes Inactivos", command=self.listar_dis)
        submenu_one.add_command(label="Estudiantes Matriculados", command=self.listar_inscr)

        menuStudent.add_command(label="Registar nuevo Estudiante", command=self.add_student)
        menuStudent.add_command(label="Matricular estudiante", command=self.loc_test)
        menuStudent.add_command(label="Evaluar estudiante", command=self.eval_test)
        menuStudent.add_command(label="Pagar Cuotas", command=self.pag_cuotas)
        menuStudent.add_cascade(label="Listar", menu=submenu_one, underline=0)

        # se añade el menu y los sub menus a la barra de menu
        barraMenu.add_cascade(label="Estudiante", menu=menuStudent)

        """---------- menu Cursos----------------"""
        menuCursos= Menu(barraMenu , tearoff=0)

        # se crea los submenus para cursos
        submenu_three = Menu(menuCursos)
        submenu_three.add_command(label="Cursos Basicos", command=self.listar_basicos)
        submenu_three.add_command(label="Cursos Intermedios", command=self.listar_intermedios)
        submenu_three.add_command(label="Cursos Avanzados", command=self.listar_avanzados)

        menuCursos = Menu(barraMenu, tearoff=0)
        menuCursos.add_command(label="Registar nuevo Curso", command=self.add_curso)
        menuCursos.add_cascade(label="Listar Cursos", menu=submenu_three, underline=0)

        # se añade el menu y los sub menus a la barra de menu
        barraMenu.add_cascade(label="Cursos", menu=menuCursos)


        """----------se crea el menu Informacion----------------"""
        menuInfo = Menu(barraMenu, tearoff=0)
        # se crea los submenus para Informacion
        menuInfo.add_command(label="Acerca de", command=self.info)
        menuInfo.add_command(label="Ayuda", command=self.ayuda)

        # se añade el menu y los sub menus a la barra de menu
        barraMenu.add_cascade(label="Ayuda", menu=menuInfo)
        barraMenu.add_command(label="Salir", command=self.salir)

        # se añade la barra de menu a la ventana root
        ventana.config(menu=barraMenu)

    # ---------------------------------------------------------------------
    def salir(self):
        '''Funcion para salir del sistema'''
        if (messagebox.askyesno ("Salir","Desea realmente salir?")):
            Store.guardar_datos()
            exit()

    def ayuda(self):
        if (messagebox.askyesno("?", "Desea abrir el manual de usuario?")):
            self.callback()

    def callback(event):
        webbrowser.open_new(r"help/index.html")

    def cargarDatos(self):
        '''FUncion para cargar los datos predeterminados al iniciar el sistema'''
      # ins = App()
      # ins.datos_predeterminados()
        Store.cargar_datos()
        messagebox.showinfo("INFO", "Todos los datos cargados")

    def info(self):
        '''Informacion acerca del sistema'''
        messagebox.showinfo("Acerca del sistema", "".center(20, "=") + "\n"
                            + "GESTOR ACADEMICO" + "\n"
                            + "Lorena Acosta" + "\n"
                            + "5.808.868 " + "\n"
                            + " LCIK" + "\n"
                            + "".center(20, "="))


    """ Funciones para las llamadas a los submenus de Estudiante"""
    def add_student(self):
        '''Funcion que destruye y crea UN FRAME ESTUDIANTE'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual=  AgregarEstudiante(self)


    def add_curso(self):
        '''Funcion que destruye y crea UN nuevo FRAME CURSO'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual=  AgregarCurso(self)

    def listar_todos(self):
        '''Funcion que destruye y crea UN nuevo FRAME para Listar Todos los estudiantes'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual = ListarEstudiantes(self, "Lista de Estudiantes", 'todos')

    def listar_cd(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Estudiantes con Descuento'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarEstudiantes(self, "Estudiantes con Descuento", 'cd')

    def listar_sd(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Estudiantes sin Descuento'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarEstudiantes(self, "Estudiantes sin Descuento", 'sd')

    def listar_ena(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Estudiantes Activos'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarActivos(self, "Estudiantes Activos", 'activo')

    def listar_dis(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Estudiantes Inactivos'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarInactivos(self, "Estudiantes Inactivos", 'inactivo')
    def listar_inscr(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Estudiantes inscriptos'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarInscriptos(self, "Estudiantes matriculados", 'inscripto')


    def listar_basicos(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Cursos Basicos'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual = ListarBasicos(self, "Cursos Basicos", 'basico_')

    def listar_intermedios(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Cursos Intermedios'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarIntermedios(self, "Cursos Intermedios", 'intermedio_')

    def listar_avanzados(self):
        '''Funcion que destruye y crea UN nuevo FRAME para listar Cursos Avanzados'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
            self.ventanaActual = ListarAvanzados(self, "Cursos Avanzados", 'avanzado_')

    def loc_test(self):
        '''Funcion que destruye y crea UN nuevo FRAME para Test de Ubicacion'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual=TestUbicacion(self)

    def eval_test(self):
        '''Funcion que destruye y crea UN nuevo FRAME para Test de Ubicacion'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual = TestCurso(self)


    def pag_cuotas(self):
        '''Funcion que destruye y crea UN nuevo FRAME para Test de Ubicacion'''
        if (self.ventanaActual):
            self.ventanaActual.destroy()
        self.ventanaActual = PagarCuota(self)


