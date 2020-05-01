from tkinter import *
import Main

def codigoBoton():
    Main.iniciar()

# Raiz
root = Tk()
root.title("Genesis - Iniciar sesion")
root.config(width=600,heigh=400)

# Frame Principal
MainFrame = Frame(root)
MainFrame.pack()
MainFrame.config(width=600,heigh=400)

# Clase Imagen
imagen = PhotoImage(file="images.png")

# Cuadro de Texto del Titulo
Titulo = Label(MainFrame, text="Iniciar Sesion",font=("Arial",36))
Titulo.grid(row=0,column=1,columnspan=2)

# Apartado del Logo
Logo = Label(MainFrame,image=imagen)
Logo.grid(row=0,column=0,rowspan=3)

# Cuadro de Texto Para el Usuario
User = Label(MainFrame,text="Usuario: ")
User.grid(row=1,column=1)
UserEn = Entry(MainFrame)
UserEn.grid(row=1,column=2)

# Cuadro de Texto Para la Contraseña
Pass = Label(MainFrame,text="Contraseña: ")
Pass.grid(row=2,column=1)
PassEn = Entry(MainFrame)
PassEn.grid(row=2,column=2)
PassEn.config(show="·")

ContinuarBoton = Button(root, text="Continuar", command=codigoBoton)
ContinuarBoton.pack()

root.mainloop()
