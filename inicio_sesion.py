from tkinter import *

ventana = Tk()
correo = StringVar()
contraseña = StringVar()

ventana.title("LOGIN")
ventana.geometry("250x200")
etiqueta = Label(ventana, text="CORREO: ").place(x=10,y=10)
generoCaja = Entry(ventana, textvariable=correo).place(x=10,y=40)
etiqueta2 = Label(ventana, text="CONTRASEÑA: ").place(x=10,y=70)
tituloCaja = Entry(ventana, textvariable=contraseña).place(x=10,y=100)

boton = Button(ventana, text="Iniciar Sesion").place(x=10,y=130)
boton = Button(ventana, text="Registrar").place(x=150,y=130)
ventana.mainloop()