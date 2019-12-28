from abc import ABCMeta, abstractmethod
from COntrolador.Util import Util
from Clases.Evaluacion import Writing, Reading, Listening, Speaking
import Bdatos.basededatos as basededatos


class Test():
    '''Clase que permite crear un obejto del tipo Test QUE CONTIENE cuantro modulos'''
    '''Write, read, listen, speak'''
    def __init__(self, write =0, read =0, listen = 0, speak = 0):
        self.write = write
        self.read = read
        self.listen = listen
        self.speak = speak

    def __str__(self):
        return ("Write: {}".format(self.write) + "\n"
                "Read: {}".format(self.read) + "\n"
                "Listen: {}".format(self.listen) + "\n"
                "SPeak: {}".format(self.speak) + "\n")

    @abstractmethod
    def abs():
        pass


#*********************************************************************
#____________________TEST DE CURSO__________________________________

class TestCurso (Test):
    def __init__(self, asistencia = 0, redcarpet = 0, **kwargs):
        super().__init__(**kwargs)
        self.asistencia = asistencia
        self.redcarpet = redcarpet

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(write=Util.rango_puntaje_c('Ingrese puntaje hecho en el Write:  '),
                    read=Util.rango_puntaje_c('Ingrese puntaje hecho en el Read '),
                    listen=Util.rango_puntaje_c('Ingrese puntaje hecho en el Listen'),
                    speak=Util.rango_puntaje_c('Ingrese puntaje hecho en el Speak: '),
                    asistencia=Util.rango_puntaje_c('Ingrese asistencia en porcentaje'),
                    redcarpet=Util.rango_puntaje_c('Ingrese la cantidad de Redcarpets'))

    prompt_init = staticmethod(prompt_init)

    def __str__(self):
        return Test.__str__(self)


    def eval_resultado(self):
        '''60% para notas, 25% aistencia y 15% para Redcarpets'''
        notas = (int(self.write) + int(self.read) + int(self.listen) + int(self.speak))* 60 /80
        asis= int(self.asistencia) *25/100
        red = int(self.redcarpet) *15/6

        return int(notas +asis +red)



    def mostrar_resultado(self, total):
        if (total >60 ):
            return 'APROBED'
        else:
            return 'NOT APROBED'




#************************************************************************************
#_______________________TEST DE UBICACION __________________________________________________

class TestUbi(Test):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict(write=Util.rango_puntaje_u('Ingrese puntaje hecho en el Write:  '),
                    read=Util.rango_puntaje_u('Ingrese puntaje hecho en el Read '),
                    listen=Util.rango_puntaje_u('Ingrese puntaje hecho en el Listen'),
                    speak=Util.rango_puntaje_u('Ingrese puntaje hecho en el Speak: '))
    prompt_init = staticmethod(prompt_init)

    def __str__(self):
        return Test.__str__(self)

    def eval_resultado(self):
        var = ((int(self.write) + int(self.read) + int(self.listen) + int(self.speak))*100 /80)
        return (var)

