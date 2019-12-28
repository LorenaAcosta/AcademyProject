
#**********************************************
#__VERSION GRAFICA DE LA APLICACION - TKINTER_
#***********************************************
from tkinter import Tk

from Vistas.Index import MainMenu

ventana = Tk()
v_prin = "600x480+700+100"
fondo = "#fff"
ventana.geometry(v_prin)
ventana.resizable(width=0, height=0)
ventana.title("GESTOR ACADEMICO")
ventana.protocol("WM_DELETE_WINDOW", "onexit")
ventana.config(bg=fondo)

exe = MainMenu(ventana)
exe.mainloop()
