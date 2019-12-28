import shelve
import Bdatos.basededatos as basededatos


def shelve_open(self, lista):
    s = shelve.open('test_shelf.db')
    try:
        s['cursos'] = lista
        print('datos cargados')
    finally:
        s.close()


def shelve_exisiting(self):
    s = shelve.open('test_shelf.db')
    try:
        existing = s['cursos']
    finally:
        s.close()


def write_back(self):
    s = shelve.open('test_shelf.db', writeback=True)
    try:
        print(s['cursos'])
        s['cursos'] = basededatos.cursosbasicos

    finally:
        s.close()

        s = shelve.open('test_shelf.db', writeback=True)
        try:
            print(s['cursos'])
        finally:
            s.close()


# ------------------------------------------------------------------

def guardarDatos(lista, nombreArchivo, clave):
    ''' metodo o funcion que sirve para
     guardar los datos en archivo'''
    try:
        archivo = shelve.open(nombreArchivo,'n')
        archivo[clave] = lista
    except FileNotFoundError:
        print("Archivo no existe")

    else:
        archivo.close()


# ---------------------------------------------------------------------------
""" funciones de cargar y guardar utilizado para
una mejor reutilizacion tanto por consola """


def cargar_datos():
    ''' carga los datos en listas para su uso'''
    basededatos.cursosbasicos = cargarLista("Basicos", "basicos")
    basededatos.cursosintermedios = cargarLista("Intermedios", "intermedios")
    basededatos.cursosavanzados = cargarLista("Avanzados", "avanzados")
    basededatos.total_estudiantes = cargarLista("Estudiantes", "estudiantes")
    basededatos.inscriptos = cargarLista("Inscriptos", "inscriptos")

def guardar_datos():
    ''' guarda los las listas en archivos para la persistencia'''
    guardarDatos(basededatos.cursosbasicos, "Basicos", "basicos")
    guardarDatos(basededatos.cursosintermedios, "Intermedios", "intermedios")
    guardarDatos(basededatos.cursosavanzados, "Avanzados", "avanzados")
    guardarDatos(basededatos.total_estudiantes, "Estudiantes", "estudiantes")
    guardarDatos(basededatos.inscriptos, "Inscriptos", "inscriptos")

# ---------------------------------------------------------------------------
def cargarLista(nombreArchivo, clave):
    ''' carga los datos al sistema cuando
     cuando el sist. se ejecuta'''
    try:
        archivo = shelve.open(nombreArchivo)
        lista = archivo[clave]

        return lista

    except KeyError:
        return []
