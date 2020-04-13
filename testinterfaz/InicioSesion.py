from tkinter import *
import Main

def codigoBoton():
    Main.iniciar()

# raiz
root = Tk()
root.title("Genesis - Iniciar sesion")
root.config(width=600,heigh=400)

# frame principal
MainFrame = Frame(root)
MainFrame.pack()
MainFrame.config(width=600,heigh=400)

# clase imagen
imagen = PhotoImage(file="images.png")

# cuadro de texto del titulo
Titulo = Label(MainFrame, text="Iniciar Sesion",font=("Arial",36))
Titulo.grid(row=0,column=1,columnspan=2)

# apartado del logo
Logo = Label(MainFrame,image=imagen)
Logo.grid(row=0,column=0,rowspan=3)

# cuadro de texto para el usuario
User = Label(MainFrame,text="Usuario: ")
User.grid(row=1,column=1)
UserEn = Entry(MainFrame)
UserEn.grid(row=1,column=2)

# cuadro de texto para la contraseña
Pass = Label(MainFrame,text="Contraseña: ")
Pass.grid(row=2,column=1)
PassEn = Entry(MainFrame)
PassEn.grid(row=2,column=2)
PassEn.config(show="·")

ContinuarBoton = Button(root, text="Continuar", command=codigoBoton)
ContinuarBoton.pack()

root.mainloop()
