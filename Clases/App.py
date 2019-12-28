# -*- coding: utf-8 -*-
import Bdatos.store as Store
from datetime import timedelta, datetime
from Clases.Persona import Estudiante
from Clases.Contacto import Contacto
from Clases.Curso import basico, intermedio, avanzado
from Clases.Test import TestCurso, TestUbi
from COntrolador.Util import Util
import Bdatos.basededatos as basededatos
import shelve


class App():

    def __init__(self):
        pass

    # ....................................................................................
    # _________________________________FUNCIONES________________________________________
    # ...................................................................................


    def get_resul(self, resul):
        if (resul>=60):
            print("Curso Aprobado!")
            print("-------------------------------------------")
        else:
            print("Curso No aprobado!")
            print("-------------------------------------------")

    def get_obs(self, resul):
        int(resul)
        if (resul <= 74 ): return ('Puede seleccionar un curso basico.- ')
        if (resul >=75 and resul <= 94): return (  'Puede seleccionar un curso Intermedio.-')
        if (resul >= 95 ): return('Puede seleccionar un curso Avanzado.-')

    def evaluar(self, resul):
        int(resul)
        if (resul <= 74): return 0
        if (resul >=75 and resul <= 94): return 1
        if (resul >= 95 ): return 2

    def get_value(self, var):
        if (var == 'si'): return 1
        if (var == 'no'): return 0

    def get_location(self, cedula):
        cont = 1
        lista = basededatos.total_estudiantes
        for x in lista:
            if cedula == x.cedula:
                return cont
            cont+=1


    #....................................................................................
    #_________________________________MENU_CURSO________________________________________
    #...................................................................................

    def add_curso(self):
        """Permite agregar un curso a la base de datos,
            Existen tres tipos de cursos, basicos, intermedio y avanzados"""

        datos = self.tipo_curso[(opcion)].prompt_init()
        basededatos.cursos.append(**datos)

    def del_curso(self):
        """Permite eliminar un curso de la base de datos."""
        self.del_datos(basededatos.cursos)


    # ....................................................................................
    # _________________________________MENU ESTUDIANTE_____________________________________
    # ...................................................................................

    def add_estudiante(self):
        """Permite agregar los datos personales de un estudiante a la base de datos.
           Actualiza la lista total de alumnos.
           La lista total de alumnos se compone de todos los tipos de estudiantes
        """
        print("REGISTRAR ESTUDIANTE".center(40, "*"))

        datos = Estudiante.prompt_init()
        basededatos.total_estudiantes.append(datos)

        # guarda al cliente en el vector cliente
        print("Completado!!!")


    def hab_estudiante(self):
        """Modifica el atributo "Estado" del estudiante."""

        if not basededatos.total_estudiantes:
            print("\nSin datos.")
            return input("Presione enter para volver al menu..")

        cedula = Util.input_entero_r("Ingrese cedula de estudiante:")
        alumno = self.obtener_datos(cedula)  # retorna estudianet o retona que no existe
        try:
            id = self.get_location(cedula)
            print(alumno.nombre, alumno.habilitar(id))
        except:
            print("No registrado")

        input("Presiona enter para volver al menu..")


    def deshab_estudiante(self):
        """Permite dar de baja a un estudiante.
            Para dar de baja se modifica el estado del estudiante"""

        if not basededatos.total_estudiantes:
            print("\nSin datos.")
            return input("Presione enter para volver al menu..")
        cedula = Util.input_entero_r("Ingrese cedula de estudiante")
        alumno = self.obtener_datos(cedula)
        try:
            id = self.get_location(cedula)
            print(alumno.nombre, alumno.deshabilitar(id))
        except:
            print("No registrado")
        input("Presiona enter para volver al menu..")


    def obtener_datos(self, cedula):
        """Devuelve el objeto "estudiante" de la lista total de estudiante"""
        lista= basededatos.total_estudiantes
        for estudiante in lista:
            if cedula == estudiante.cedula:
                return estudiante
        return "No existe"


    def tomar_test_ubi(self):
        """Permite tomar un Test de Ubicacion al alumno."""
        if not basededatos.total_estudiantes:
            print("\nNo hay estudiantes registrados aun.")
            return input("Presione enter para volver al menu..")

        try :
            cedula = Util.input_entero_r("Ingrese cedula de estudiante")
            alumno = self.obtener_datos(cedula)

            if (alumno.estado ==1):
                id = self.get_location(cedula)
                '''Agrega las notas en el Test de Curso'''
                resul= alumno.tomar_test_ubicacion(id) #puntaje 81.25
                opcion = self.evaluar(resul) #retorna 0, 1, 2
                print("\n -------------------------------------------")
                print ("\nResultado del Test: " + str(resul) + "\nObservaciones:"+ str(self.get_obs(resul)) )
                print("\n -------------------------------------------")
                '''Despliega los cursos habilitados'''
                value = self.get_lista_correcta(opcion)
                if (value == 0):
                    print("No puede inscribirse por que no hay Cursos registrados.")
                if (value ==1):
                    print("\n")
                    resp = Util.input_entero_r("Ingresar ID del curso al que desea inscribir el estudiante: ")

                    try:
                        print(alumno.set_curso(resp, opcion),str(alumno.get_course()), "!")
                        print(alumno.set_cuota(id), alumno.get_cuotas())

                    except:
                        print("NO se pudo realizar accion.")
            else:
                print("Este alumno debe realizar test de UBicacion")
        except:
            print("Esta cedula no esta registrada en la base de datos")

        self.main_menu()
        input("Presiona enter para volver al menu..")


    def tomar_curso(self):
        """Permite agregar un Test de Curso a un estudiante"""
        if not basededatos.total_estudiantes:
            print("\nSin datos.")
            return input("Presione enter para volver al menu..")

        try:
            cedula = Util.input_entero_r("Ingrese cedula de estudiante")
            alumno = self.obtener_datos(cedula)

            if (alumno.estado == 1 and alumno.cursoActual != None):
                id = self.get_location(cedula)

                '''Agrega las notas en el Test de Curso'''
                resul = alumno.tomar_test_curso(id) # puntaje 81.25 o cero

                print("-------------------------------------------")
                print("\nResultados del Test: " + str(resul))
                self.get_resul(resul)
            else:
               if (alumno.estado== 0):
                   print("Alumno no esta activo")
               else:
                print("Este estudiante aun no tomo un Test de Ubicacion.")
        except:
            print("Esta cedula no esta registrada en la base de datos")

    def mostrarDatos(self, alumno):
        print("-------------------------------------------")
        print("Estudiante: ", alumno.nombre)
        print ("Curso Actual", alumno.cursoActual.nombre)
        alumno.get_cuotas()
        print("-------------------------------------------")

    def pago_cuotas(self):
        if not basededatos.total_estudiantes:
            print("\nSin datos.")
            return input("Presione enter para volver al menu..")
        try:
            cedula = Util.input_entero_r("Ingrese cedula de estudiante")
            alumno = self.obtener_datos(cedula)

            if (alumno!= 0 and alumno.cursoActual != None):
                self.mostrarDatos(alumno)
                input("Presione enter para continuar la operacion...")
                print(alumno.pagarCuotas())
                input("Presione enter para continuar la operacion...")
                print("Cuotas Restantes!")
                alumno.get_cuotas()
            else:
                print("No esta registrado en ningun curso.")
        except:
            print("Esta cedula no esta registrada en la base de datos")



    # ...................................................................................
    # _________________________________MENU - MENU - MENU________________________________
    # ...................................................................................
    def main_menu(self):
        """Menu principal del programa"""
        while True:
            # cls()
            print("                                                           ")
            print("--------------------MENU--PRINCIPAL------------------------")
            print()
            for key in list(self.opciones.keys()):
                print(("{} - {}".format(key, self.opciones[key]["t"])))
            print()
            opcion = Util.input_range("Ingrese una opcion", 1, 5)
            self.opciones[int(opcion)]["f"](self)


    def menu_list(self, text, dic, lim):
        """Presenta el menu con las opciones"""
        while True:
           # Util.cls()
            print(("\n------------------{}--------------------------\n".
                   format(text)))
            for key in list(dic.keys()):
                print(("{} - {}".format(key, dic[key]["t"])))
            print()
            opcion = Util.input_range("Ingrese una opcion", 1, lim)
            dic[int(opcion)]["f"](self)

    def menu_estudiantes(self):
        self.menu_list("MENU--ESTUDIANTES", self.o_estudiantes, len(self.o_estudiantes))

    def menu_cursos(self):
        self.menu_list("MENU--CURSOS", self.o_cursos, len(self.o_cursos))

    def menu_evaluaciones(self):
        self.menu_list("MENU--EVALUACIONES", self.o_evaluaciones, len(self.o_evaluaciones))

    def menu_reportes_cursos(self):
        self.menu_list("MENU--REPORTES CURSOS", self.o_reportes_cursos, len(self.o_reportes_cursos))

    def menu_reportes_estudiantes(self):
        self.menu_list("MENU--REPORTES ESTUDIANTES", self.o_reportes_estudiantes, len(self.o_reportes_estudiantes))


    # ....................................................................................
    # _________________________________LISTAR CURSOS_____________________________________
    # ...................................................................................

    def listar_basicos(self):
        """Lista los cursos basicos"""
        self.listar_datos(basededatos.cursosbasicos, 'b')

    def listar_intermedios(self):
        """Lista los cursos intermedios"""
        self.listar_datos(basededatos.cursosintermedios, 'i')

    def listar_avanzados(self):
        """Lista los cursos avanzados"""
        self.listar_datos(basededatos.cursosavanzados, '')

    # ....................................................................................
    # _________________________________LISTAR_____________________________________________
    # ....................................................................................

    def listar_todos(self):
        """Lista la totalidad de los EStudiantes"""
        self.listar_datos(basededatos.total_estudiantes, 'todos')

    def listar_estado(self):
        """Lista estudiantes por estado. Activo o Inactivo"""
        opcion = Util.input_opcion_r("Estado ", ("activo", "inactivo"))
        if opcion == 'activo':
            self.listar_datos(basededatos.total_estudiantes, opcion)
        if opcion == 'inactivo':
            self.listar_datos(basededatos.total_estudiantes, opcion)

    def listar_tipo(self):
        """Lista estudiantes por tipo. Privado o de la UNA"""
        opcion = Util.input_opcion_r("CON Descuento: CD, SIN Descuento: SD", ("CD", "SD"))
        self.listar_datos(basededatos.total_estudiantes, opcion)


    def get_lista_correcta(self, opcion):
        '''Lista el curso correcto dependiento de la opcion que se recibe como parametro'''
        if (opcion == 0):
            value = self.listar_cursos(basededatos.cursosbasicos, 'ubicacion', False)
            return value
        if (opcion == 1):
            value = self.listar_cursos(basededatos.cursosintermedios, 'ubicacion', False)
            return value
        if (opcion == 2):
            value = self.listar_cursos(basededatos.cursosavanzados, 'ubicacion', False)
            return value
        if (opcion == 3):
            lista = (basededatos.cursosbasicos + basededatos.cursosintermedios + basededatos.cursosavanzados)
            value = self.listar_cursos(lista, 'ubicacion', False)
            return value

    def fin(self):
        Store.guardar_datos()
        print("\n\n----------Todos los datos fueron guardados----------------")
        print("-------------------FIN DE LA APLICACION--------------\n")
        exit()



    # ....................................................................................
    # _________________________________OPCIONES DE MENU______________________________________
    # ....................................................................................

    opciones = {}
    opciones[1] = {"t": "Menu de Estudiantes", "f": menu_estudiantes}
    opciones[2] = {"t": "Menu de Cursos", "f": menu_cursos}
    opciones[3] = {"t": "Menu de Evaluaciones", "f": menu_evaluaciones}
    opciones[4] = {"t": "Pago de Cuotas", "f": pago_cuotas}
    opciones[5] = {"t": "SALIR", "f": fin}

    o_estudiantes = {}
    o_estudiantes[1] = {"t": "Agregar estudiante", "f": add_estudiante}
    o_estudiantes[2] = {"t": "Habilitar estudiante", "f": hab_estudiante}
    o_estudiantes[3] = {"t": "Dar de baja estudiante", "f": deshab_estudiante}
    o_estudiantes[4] = {"t": "Listar estudiantes", "f": menu_reportes_estudiantes}
    o_estudiantes[5] = {"t": "Volver", "f": main_menu}

    o_cursos = {}
    o_cursos[1] = {"t": "Agregar curso", "f": add_curso}
    o_cursos[2] = {"t": "Eliminar curso", "f": del_curso}
    o_cursos[3] = {"t": "Resportes de Cursos", "f": menu_reportes_cursos}
    o_cursos[4] = {"t": "Volver", "f": main_menu}

    o_evaluaciones = {}
    o_evaluaciones[1] = {"t": "Tomar Test de Ubicacion", "f": tomar_test_ubi}
    o_evaluaciones[2] = {"t": "Tomar Test de Curso", "f": tomar_curso}
    o_evaluaciones[3] = {"t": "Volver", "f": main_menu}

    o_reportes_cursos = {}
    o_reportes_cursos[1] = {"t": "Cursos Basicos", "f": listar_basicos}
    o_reportes_cursos[2] = {"t": "Cursos Intermedios", "f": listar_intermedios}
    o_reportes_cursos[3] = {"t": "Cursos Avanzados", "f": listar_avanzados}
    o_reportes_cursos[4] = {"t": "Volver", "f": main_menu}


    o_reportes_estudiantes = {}
    o_reportes_estudiantes[1] = {"t": "Todos los estudiantes", "f": listar_todos}
    o_reportes_estudiantes[2] = {"t": "Estudiantes por Tipo", "f": listar_tipo}
    o_reportes_estudiantes[3] = {"t": "Estudiantes por Estado", "f": listar_estado}
    o_reportes_estudiantes[4] = {"t": "Volver", "f": main_menu}



    # ....................................................................................
    # _________________________________LISTAR_____________________________________________
    # ....................................................................................

    def listar_cursos(self, lista, opcion, p = True):
        """Permite listar los cursos"""
        cont = 1
        if lista:
            print("Lista de Cursos Habilitados")
            for val in lista:
                if (opcion == 'ubicacion'):
                    print(("-----------------=={}==-----------------".format(cont)))
                    print("Curso: {}".format(val.nombre))
                    print("Duracion: {}".format(val.duracion))
                    print("Horario: {}".format(val.horario))
                    print("Monto: {}".format(val.monto))
            return 1
        else:
            return 0

    def listar_datos(self, lista, opcion, p=True):
        """Permite listar los datos contenidos en en los distintos vectores
           El valor p =False sirve para imprimir sin pausas"""
        cont = 1
        if lista:
            print()
            for val in lista:
                if (opcion == 'activo'):
                    if (val.estado == 1):
                        print(("-----------------=={}==-----------------".format(cont)))
                        print(val)
                        print()
                if (opcion) == 'inactivo':
                    if (val.estado == 0):
                        print(("-----------------=={}==-----------------".format(cont)))
                        print(val)
                        print()
                if (opcion == 'CD'):
                    if (val.tipo == True):
                        print(("-----------------=={}==-----------------".format(cont)))
                        print(val)
                if (opcion == 'SD'):
                    if (val.tipo == False):
                        print(("-----------------=={}==-----------------".format(cont)))
                        print(val)
                if (opcion == 'todos' or opcion == ''):
                    print(("-----------------=={}==-----------------".format(cont)))
                    print(val)
                if (cont % 5) is 0:
                    if p:
                        input("Presione enter para continuar...")
                cont += 1
            if p:
                input("Presione enter para volver al menu...")
        else:
            input("\n No hay datos registrados... \nPresione enter para continuar...")

    def del_datos(self, lista):
        """Permite eliminar un objeto por valor posicional del mismo"""
        if lista:
            pos = Util.input_entero_r("Ingrese posicion de dato a eliminar")
            if pos is not None:
                try:
                    lista[pos - 1].mostrar()
                    resp = Util.input_opcion("Desea eliminar el dato de arriba",
                                        ("si", "no"))
                    if resp == "si":
                        lista.pop(pos - 1)
                        print("Eliminado.")
                    else:
                        print("Cancelado.")
                except:
                    print("Valor incorrecto.")
            else:
                print("Cancelado.")
        else:
            print("\nSin datos.")
        input("Presione enter para continuar...")

# ....................................................................................
    # ____________________________CARGAR DATOS PREDETERMINADOS____________________________
    # ....................................................................................

    def datos_predeterminados(self):
        """Funcion que sirve para cargar algunos datos en el sistema"""

        self.contactos = Contacto(tel=21678678, cel=98765432, email= "lore_f@hotmail.com")
        basededatos.total_estudiantes.append(Estudiante(**{"cedula": 1234 ,"nombre": "Lorena", "apellido": "Acosta" ,
                                                           "direccion": "km23", "contacto": self.contactos}))

        self.contactos = Contacto(tel=21678678, cel=98765432, email="anita_p@hotmail.com")
        basededatos.total_estudiantes.append(Estudiante(**{"cedula": 5678, "nombre": "Anita", "apellido":  "Caceres",
                                                           "direccion": "Espana", "contacto": self.contactos}))

        self.contactos = Contacto(tel=21678678, cel=98765432, email= "ricardo_g@hotmail.com ")
        basededatos.total_estudiantes.append(Estudiante(**{"cedula": 1000, "nombre": "Ricardo", "apellido": "Fish",
                                                           "direccion": "km12", "contacto": self.contactos}))

        self.contactos = Contacto(tel=98768, cel= 984775517, email="Jhony_ben@hotmail.com ")
        basededatos.total_estudiantes.append(Estudiante(**{"cedula": 5000, "nombre": "Jhony", "apellido": "Benitez",
                                                           "direccion": "km16", "contacto": self.contactos}))

        basededatos.cursosbasicos.append(basico(nombre='Everyday', duracion= 3, horario='lunes/viernes',
                                                monto = 150000, write= 20, read= 20, listen=20, speak=20))
        basededatos.cursosbasicos.append(basico(nombre='EnglishA01', duracion= 5, horario='martes/jueves',
                                                monto=100000, write=20, read=20, listen=20, speak=20))
        basededatos.cursosintermedios.append(intermedio(nombre='Values', duracion=3, horario='lunes/viernes',
                                                        monto=200000, write=20, read=20, listen=20, speak=20))
        basededatos.cursosintermedios.append(intermedio(nombre='Boston', duracion=2, horario='martes/sabado',
                                                        monto=250000, write=20, read=20, listen=20, speak=20))
        basededatos.cursosavanzados.append(avanzado(nombre='Leadership', duracion=6,  horario='lunes/viernes',
                                                    monto=350000, write=20, read=20, listen=20, speak=20))
        basededatos.cursosavanzados.append(avanzado(nombre='UniversityPrep', duracion=6, horario='lunes/viernes',
                                                    monto=350000, write=20, read=20, listen=20, speak=20))

        Store.guardar_datos()
