import os
from tkinter import *

#**************************Iniciar interfaz*************************#

def iniciar():
    # raiz
    root = Tk()
    root.title("Genesis - Sesion Iniciada")
    root.config(width=600,heigh=400)

    # frame principal
    MainFrame = Frame(root)
    MainFrame.pack()
    MainFrame.config(width=600,heigh=400)

    Titulo = Label(MainFrame, text="Iniciada Correctamente",font=("Arial",36))
    Titulo.grid(row=0,column=0)

    root.mainloop()

    os.system('cls')
