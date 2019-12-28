from abc import ABCMeta, abstractmethod
from COntrolador.Util import Util


class Evaluacion(metaclass=ABCMeta):
    def __init__(self,porcentaje = 0):
        self.porcentaje = porcentaje

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict({
            "porcentaje": Util.input_entero_r("Porcentaje.") })
    prompt_init = staticmethod(prompt_init)

    def __str__(self):
        return "\t {}".format(self.porcentaje)



#**************************************************************
class Writing(Evaluacion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "\t Writing: {}" + Evaluacion.__str__(self)

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        text = 'Write'
        parent_init = Evaluacion.prompt_init(text)
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def abs():
        pass

class Reading(Evaluacion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "\t Reading: {}" + Evaluacion.__str__(self)


    def prompt_init():
        text = 'Read'
        parent_init = Evaluacion.prompt_init(text)
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def abs():
        pass

class Listening(Evaluacion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "\t Listening: {}" + Evaluacion.__str__(self)

    def prompt_init():
        text = 'Listen'
        parent_init = Evaluacion.prompt_init(text)
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def abs():
        pass

class Speaking(Evaluacion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "\t Speaking: {}" + Evaluacion.__str__(self)


    def prompt_init():
        text = 'Speak'
        parent_init = Evaluacion.prompt_init(text)
        return parent_init

    prompt_init = staticmethod(prompt_init)

    def abs():
        pass

