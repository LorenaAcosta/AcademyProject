# -*- coding: utf-8 -*-
from datetime import timedelta, datetime
from Clases.Persona import Estudiante
from Clases.Contacto import Contacto
from Clases.Curso import basico, intermedio, avanzado
from Clases.Test import TestCurso, TestUbi
from Clases.App import App
from COntrolador.Util import Util
import Bdatos.store as Store
import Bdatos.basededatos as basededatos
import shelve



#operaciones Iniciales
institucion = App()
# opcional cargar datos
institucion.datos_predeterminados()
Store.cargar_datos()



print("\n" + "---------------Todos los datos cargados---------------")
institucion.main_menu()



