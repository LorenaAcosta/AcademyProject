# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from COntrolador.Util import Util
from Clases.Contacto import Contacto
from Clases.Test import Test, TestUbi, TestCurso
import Bdatos.basededatos as basededatos

#________________________________PERSONA_______________________________________

class Persona():
    '''Clase padre que permite crear a un objeto de tipo persona'''

    def __init__(self, cedula=0, nombre='', apellido='', direccion='No indica',
    contacto=None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.contactos = contacto

    def __str__(self):
        return ( str(self.cedula) +" "+ self.nombre +" "+ self.apellido + " "+
                self.direccion+ " " + str(self.contactos.__str__()))

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(cedula=Util.input_cedula('Ingrese cedula'),
                    nombre=Util.input_alpha_r('Ingrese nombre'),
                    apellido=Util.input_alpha_r('Ingrese apellido'),
                    direccion=Util.input_alpha_r('Ingrese direccion'))

    prompt_init = staticmethod(prompt_init)

    def add_contactos(self, tel='', cel='', email=''):
        self.contactos = Contacto(tel, cel, email)

    def get_cedula(self):
        return self.cedula

    @abstractmethod
    def abs():
        pass


#********************************************************************************
#________________________________ESTUDIANTE______________________________________

class Estudiante(Persona):
    '''Clase extendida de Persona'''

    def __init__(self, tipo= 0, estado = 1, cursoActual= None, notas= None,
                 monto_total_curso = 0, **kwargs):
        super().__init__(**kwargs)
        self.tipo = tipo
        self.estado = estado
        self.cursoActual = cursoActual
        self.notas= []
        self.vectorCuotas = []

    def get_notas(self):
        if(self.notas):
            print("Notas")
            for val in self.notas:
                print(str(val))
        else:
            print("SIN NOTAS")


    def get_cuotas(self):
        if(self.vectorCuotas):
            return self.vectorCuotas


    def get_tipo(self):
        if (self.tipo == 1):
            return 'CD'
        else:
            return 'SD'


    def get_estado(self):
        if (self.estado == 1):
            return 'activo'
        else:
            return 'Inactivo'



    def set_curso(self, id_curso, opcion, alu):
        try:
           if (opcion=='basico'):
               curso = basededatos.cursosbasicos[id_curso]
           elif(opcion =='intermedio'):
                curso = basededatos.cursosintermedios[id_curso]
           elif(opcion =='avanzado'):
               curso = basededatos.cursosavanzados[id_curso]

           self.cursoActual = curso
           basededatos.inscriptos.append([alu.cedula, alu.nombre, curso.nombre])

           return "Inscripcion realizada al curso "
        except:
            return "Debe introducir el id correcto"


    def set_cuota(self, id):
        alu = basededatos.total_estudiantes[id]
        k = int(alu.cursoActual.duracion)
        curso = alu.cursoActual

        if (alu.tipo == 1):
            desc = int(curso.monto) * 0.1
            mes = int(curso.monto) - int(desc)
            for i in range (k):
                value = [i+1, mes]
                basededatos.total_estudiantes[id].vectorCuotas.append(value)
            return "Cuotas exitosamente generadas!"

        elif (alu.tipo ==0):
            for i in range (k):
                value= [i+1, curso.monto]
                basededatos.total_estudiantes[id].vectorCuotas.append(value)
            return "Cuotas exitosamente generadas!"


    def get_course(self):
        return (self.cursoActual.nombre)

    def habilitar(self, id):
        if basededatos.total_estudiantes[id].estado == 1:
            return ("ya esta habilitado.")
        else:
            basededatos.total_estudiantes[id].estado = 1
            return ("Habilitado!")


    def deshabilitar(self, pos):
        if basededatos.total_estudiantes[pos].estado == 0:
            return "ya esta deshabilitado."
        else:
            if (basededatos.total_estudiantes[pos].cursoActual== None):
                basededatos.total_estudiantes[pos].estado = 0
                return "Deshabilitado"

    def eval_resultado(self, notas):
        return ((notas[0] + notas[1]+ notas[2]+ notas[4]) * 100 / 80)

    def tomar_test_ubicacion(self,id, notas):
        puntaje = TestUbi(**notas)
        var = puntaje.eval_resultado()
        print("puntaje calculado", str(var))
        basededatos.total_estudiantes[id].notas.append(puntaje)  #[[ubicacion] [demas notas][demasnotas]]
        return (var)


    def tomar_test_curso(self, id, notas):
       # datos = TestCurso.prompt_init()
        puntaje = TestCurso(**notas)
        num = puntaje.eval_resultado()
        print("puntaje calculado", str(num))
        basededatos.total_estudiantes[id].notas.append(puntaje) #[[demas notas][demasnotas]]
        return (num)


    def pagarCuotas(self, pos):
        try:
            self.vectorCuotas.pop(pos)
            return ("Cuota pagada")
        except:
            return ("Valor incorrecto.")

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
                instanciar al objeto"""
        parent_init = Persona.prompt_init()
        datos = Contacto.prompt_init()
        contacto = Contacto(**datos)
        parent_init.update({
            "contacto": contacto})
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def __str__(self):
        return (Persona.__str__(self) + str(self.get_estado()))





