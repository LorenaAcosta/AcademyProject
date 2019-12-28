from tkinter import *
import Bdatos.basededatos as bd
from Clases.Persona  import Estudiante
import re

class Util:

    def mi_label(self, **kwargs):
            Label.__init__(self, **kwargs)

    def limpiar_pantalla(self, frame):
        if (frame):
            frame.destroy()

    def validar_cedula(ced):
        val = False
        if ced.isdigit():
            val = True
        else:
            messagebox.showinfo("", "Ingrese numerico para cedula")
        return val

    def val_email(email):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
            return True
        else:
            messagebox.showinfo("", "Correo invalido")

    def validar_contacto( tel, cel):
        val = False
        if tel.isdigit() or cel.isdigit():
            val = True
        else:
            messagebox.showinfo("", "Ingrese numerico para telefono o celular")
        return val


    def verificar_estudiante(cedula):
        ''' utilizado para verificar si un estudiante
        ya esta registado o no, devuelve True si lo esta'''
        for item in bd.total_estudiantes:
            if (int(item.cedula) == int(cedula)):
                return True
        return False

    def comprueba_codigo(cedula):
        '''comprueba si un estudiante con cierto
        codigo existe o no en el sistema'''
        ced = int(cedula)
        for alumno in bd.total_estudiantes:
            if (alumno.cedula == ced):
                return True
                break
            else:
                return False
    def validar_puntajes(w, r, l, s):
        w= int(w)
        r = int(r)
        l= int(l)
        s= int(s)
        if (w>=0 and w <=20 and  r>=0 and r<=20 and  l>=0 and l<=20 and s>=0 and s<= 20):
            return True
        else:
            messagebox.showinfo("INFO", "Los modulos se puntuan hasta un max.de 20 puntos.")
            return False
    def get_position(nombre_curso):
        for i, item in enumerate(bd.cursosbasicos):
            if item.nombre == str(nombre_curso):
                return i
        for i, item in enumerate(bd.cursosintermedios):
            if item.nombre == str(nombre_curso):
                return i
        for i, item in enumerate(bd.cursosavanzados):
            if item.nombre == str(nombre_curso):
                return i

    def get_list(nombre_curso):
        for i, item in enumerate(bd.cursosbasicos):
            if item.nombre == str(nombre_curso):
                return 'basico'
        for i, item in enumerate(bd.cursosintermedios):
            if item.nombre == str(nombre_curso):
                return 'intermedio'
        for i, item in enumerate(bd.cursosavanzados):
            if item.nombre == str(nombre_curso):
                return 'avanzado'

    def no_esta_inscripto(ced):
        for var in bd.inscriptos:
            if (var[0] == ced):
                return False
        return True

    def val_asistencia(asis, redc):
        asis= int(asis)
        redc = int(redc)
        if( asis >=0 and asis <= 100 and redc>=0 and redc<=6 ):
            return True
        else:
            messagebox.showinfo("INFO", "Hasta un max. de 6 Red Carpets y asistencia hasta 100%")
            return False

    def es_ultima_cuota(alu, cuota_nro):
        long = len(alu.vectorCuotas)
        if int(long) == int(cuota_nro):
            return True
        return False


    def get_posicion_in_list(cedula):
        ''' Retorna la posicion de un alumno en el vector Estudiantes'''
        for i, valor in enumerate(bd.total_estudiantes):
            if int(valor.cedula) == int(cedula):
                return i
        print("No se obtuvo posicion")


    def verificar_curso(nombre, opcion):
        ''' utilizado para verificar si un estudiante
        ya esta registado o no, devuelve True si lo esta'''
        esta = False
        posicion = 0
        if (opcion == 'Basic'):
            while (posicion < len(bd.cursosbasicos)):
                if (bd.cursosbasicos[posicion].nombre == nombre):
                    print(bd.cursosbasicos[posicion].nombre)
                    esta = True
                    break
                else:
                    posicion += 1
            return esta
        if (opcion == 'Intermediate'):
            while (posicion < len(bd.cursosintermedios)):
                if (bd.cursosintermedios[posicion].nombre == nombre):
                    print(bd.cursosintermedios[posicion].nombre)
                    esta = True
                    break
                else:
                    posicion += 1
            return esta
        if (opcion == 'Advance'):
            while (posicion < len(bd.cursosavanzados)):
                if (bd.cursosavanzados[posicion].nombre == nombre):
                    print(bd.cursosavanzados[posicion].nombre)
                    esta = True
                    break
                else:
                    posicion += 1
            return esta

    def get_titulo(tipo):
        if tipo == 'inscripto':
            dataCols = ('CEDULA ', 'NOMBRE', 'CURSO ACTUAL')
            return dataCols

        elif tipo=='cuotas':
            dataCols = ('Nro', 'CUOTAS')
            return dataCols

        elif (tipo == 'curso' or tipo == 'vacio' or tipo == 'basico' or
                    tipo =='intermedio' or tipo =='avanzado'):
            dataCols = ('NOMBRE CURSO', 'MES', 'HORARIO CLASE', 'COSTO MES')
            return dataCols

        elif (tipo == 'basico_' or tipo =='intermedio_' or tipo =='avanzado_'):
            dataCols = ('NOMBRE', 'MES', 'HORARIO', 'MONTO', 'WRITE', 'READ', 'LISTEN', 'SPEAK')
            return dataCols

        elif (tipo == 'estudiante'):
            dataCols = ('CEDULA', 'NOMBRE', 'APELLIDO', 'DIRECCION')
            return dataCols

        elif (tipo == 'todos' or tipo ==  'activo' or  tipo == 'inactivo' or
                    self.tipo == 'cd' or tipo == 'sd'):
            dataCols = ('CEDULA', 'NOMBRE', 'APELLIDO', 'DIRECCION', 'TELEFONO', 'CELULAR', 'CORREO')
            return dataCols



    def get_lista(tipo):
        '''retorna una lista especifica al evaluar la variable tipo'''
        if tipo == 'inscripto':
            return bd.inscriptos
        elif tipo == 'cuotas':
            data = []
            return data

        elif tipo == 'curso':
            lista = bd.cursosbasicos + bd.cursosintermedios + bd.cursosavanzados
            return lista

        elif tipo == 'basico_' or tipo == 'basico':           return bd.cursosbasicos
        elif tipo == 'intermedio_' or tipo == 'intermedio':   return bd.cursosintermedios
        elif tipo == 'avanzado_' or tipo == 'avanzado':       return bd.cursosavanzados

        if tipo == 'estudiante' or tipo == 'todos':
            return bd.total_estudiantes

        def generar_activos(lista):
            for var in lista:
                if (var.estado == 1):
                    yield var
        def generar_inactivos(lista):
            for var in lista:
                if (var.estado == 0):
                    yield var

        if tipo == 'activo':
            x = generar_activos(bd.total_estudiantes)
            lista = list(x)
            return lista

        if tipo == 'inactivo':
            x = generar_inactivos(bd.total_estudiantes)
            lista = list(x)
            return lista



class MiLabel(Label):
    def __init__(self, padre, **kwargs):
        Label.__init__(self, master=padre, **kwargs)

class MiBoton (Button):
    def __init__(self,padre,**kwargs):
        Button.__init__(self,master=padre,**kwargs, activebackground="#F50743")


