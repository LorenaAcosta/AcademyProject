# -*- coding: utf-8 -*-
import os
import Bdatos.basededatos as bd

#________________________________Util__________________________________________
#COntrolador para distintos casos y necesidades
class Util:

    def input_cedula(text):
        """ Solicita cedula que sea positiva y que no este repetda en la BD """
        while True:
            valor = input("{} *: ".format(text))
            try:
                valor = int(valor)
                if not (Util.existe(valor)):
                    return valor
                else:
                    print("Esta cedula ya esta registrada. Reintentar.")
            except ValueError:
                pass

    def no_esta_inscripto(ced):
        for var in bd.inscriptos:
            if (var[0] == ced):
                print('esta inscripto')
                return False
        print('NO inscripto')
        return True

    def existe(ced):

        for alumno in bd.total_estudiantes:
            if (alumno.cedula == ced):
                return True
        return False


    def input_mes(text):
        while True:
            valor = input("{} *: ".format(text))
            try:
                valor = int(valor)
                if (valor <= 12 ):
                    valor = int(valor)
                    return valor
            except ValueError:
                pass



    def input_range(text, men, may):
        """ Solicita un valor entero dentro de un rango y se devuelve
            Se introduce el texto a mostrar y el rango de valor minimo y maximo"""
        while True:
            valor = input("{} ({}-{}) *: ".format(text, men, may))
            try:
                valor = int(valor)
                if (valor <= may and valor >= men):
                    return valor
                else:
                    raise(ValueError)
            except ValueError:
                pass


    def input_opcion(text, opciones):
        """ Solicita un valor que debe estar presente en la lista opciones"""
        text += " ({})*: ".format(", ".join(opciones))
        val = input(text)
        while val.lower() not in opciones:
            val = input(text)
        return val.lower()

    def input_tipo(text, opciones):
        text += " ({})*: ".format(", ".join(opciones))
        val = input (text)
        while val not in opciones:
            val = input(text)

        if (val == "CD"):
            return True
        else:
            return False


    def input_opcion_r(text, opciones):
        """ Solicita un valor que debe estar presente en la lista opciones
        :rtype: object
        """
        text += " ({})*: ".format(", ".join(opciones))
        val = input(text)
        while val not in opciones:
            val = input(text)
        return str(val)


    def input_entero_r(text):
        """ Solicita un valor entero y lo devuelve. (es requerido)
            Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
        while True:
            valor = input("{} *: ".format(text))
            try:
                valor = int(valor)
                return valor
            except ValueError:
                pass


    def input_alpha(text):
        """ Solicita una cadena"""
        while True:
            valor = input("{}: ".format(text))
            try:
                return valor
            except ValueError:
                pass


    def input_alpha_r(text):
        """ Solicita una cadena (requerido)"""
        while True:
            valor = input("{} *: ".format(text))
            try:
                if valor is not '':
                    return valor
                else:
                    raise (ValueError)
            except ValueError:
                pass

    def message(self, text):
        print(str(text))

    def rango_puntaje_u(text):
        while True:
            valor = input("{} *: ".format(text))
            valor = int(valor)
            try:
                if ( valor >= 0 and valor <= 20):
                    valor = int(valor)
                    return valor
            except ValueError:
                pass

    def rango_puntaje_c(text):
        while True:
            valor = input("{} *: ".format(text))
            valor = int(valor)
            try:
                if (valor >= 0 and valor <= 100):
                    valor = int(valor)
                    return valor
            except ValueError:
                pass



