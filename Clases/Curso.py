from abc import ABCMeta, abstractmethod
from COntrolador.Util import Util


class Curso(metaclass=ABCMeta):
    '''Clase que contiene los objetos de tipo Curso'''


    def __init__(self, nombre='', duracion= 0, horario = '', monto= 0,
                 write=0, read= 0, listen=0, speak=0):
        self.nombre = nombre
        self.duracion = duracion
        self.horario = horario
        self.monto = monto
        self.write = write
        self.read =read
        self.listen= listen
        self.speak = speak


    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(nombre=Util.input_alpha_r('Nombre del Curso: '),
                    duracion=Util.input_mes('Duracion en meses(en nros): '),
                    horario = Util.input_alpha_r('Horario: '),
                    monto=Util.input_entero_r('Monto mensual: '),
                    write = Util.input_entero_r('Puntajes minimos para Writing:'),
                    read=Util.input_entero_r('Puntajes minimos para Reading:'),
                    listen=Util.input_entero_r('Puntajes minimos para Listening:'),
                    speak=Util.input_entero_r('Puntajes minimos en el Speaking:'))

    prompt_init = staticmethod(prompt_init)

    def __str__(self):
        return (self.nombre +" "+ str(self.duracion) + " " +  self.horario + " " +  str(self.monto) + " "
                + str(self.write) + " "+ str(self.read) + " " + str(self.listen) + " " +  str(self.speak))


    def get_puntajes(self):
        if self.puntajes_mins:
            for punt in self.puntajes_mins:
                puntajes.get_values()
        else:
            print("--No posee puntajes--")


    @abstractmethod
    def abs():
      pass



#***********************************************************************

class basico(Curso):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return Curso.__str__(self)

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Curso.prompt_init()
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def abs():
        pass


class intermedio(Curso):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return Curso.__str__(self)


    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Curso.prompt_init()
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def abs():
        pass

class avanzado(Curso):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return Curso.__str__(self)

    def abs():
        pass

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        parent_init = Curso.prompt_init()
        return parent_init

    prompt_init = staticmethod(prompt_init)
