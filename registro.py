from tkinter import *

ventana = Tk()
nombre = StringVar()
apellido = StringVar()
correo = StringVar()
contraseña=StringVar()

ventana.title("LOGIN")
ventana.geometry("250x400")
etiqueta = Label(ventana, text="NOMBRE: ").place(x=10,y=10)
generoCaja = Entry(ventana, textvariable=nombre).place(x=10,y=40)
etiqueta2 = Label(ventana, text="APELLIDO: ").place(x=10,y=70)
tituloCaja = Entry(ventana, textvariable=apellido).place(x=10,y=100)
etiqueta3 = Label(ventana, text="CORREO: ").place(x=10,y=130)
resumenCaja = Entry(ventana, textvariable=correo).place(x=10,y=170)
etiqueta4 = Label(ventana, text="CONTRASEÑA: ").place(x=10,y=200)
añoCaja = Entry(ventana, textvariable=contraseña).place(x=10,y=230)

boton = Button(ventana, text="REGISTAR").place(x=50,y=320)
ventana.mainloop()