from COntrolador.Util import Util

class Contacto():
    '''Clase que contiene los contactos de las personas'''
    #emails = []

    def __init__(self, tel='', cel='', email=''):
        super(Contacto, self).__init__()
        self.tel = tel
        self.cel = cel
        self.emails = []
        self.emails.append(email)

    def __str__(self):
        return  (str(self.tel) +" "+ str(self.cel) + " "+ str(self.emails))

    def prompt_init():
        """Se crea un diccionario con los indices y valores necesarios para
        instanciar al objeto"""
        return dict({
            "tel": Util.input_entero_r("Tel."),
            "cel": Util.input_entero_r("Cel."),
            "email": Util.input_alpha("Ingrese email")})
    prompt_init = staticmethod(prompt_init)


    def add_email(self, email):
        '''Permite anhadir una direccion de correo sin eliminar las demas'''
        self.emails.append(email)
