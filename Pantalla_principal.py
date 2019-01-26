import mysql.connector

from tkinter import *
from tkinter import messagebox

ventana = Tk()
#Conexio Base de Datos

cnx = mysql.connector.connect(user='root', password='12345',
                              host='3306',
                              database='proyectosl')
db = mysql.connect(cnx[0],cnx[1],cnx[2])
cursor = db.cursor()

#Guardar Datos

def guarda():
    a=cant_productos.get()
    c=jabas_vendidas.get()

    sql = "INSERT INTO reporte(productos, \
            jabas) \
          VALUES('%d', '%s')"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    messagebox.showinfo("Guardado", "Se a registrado la pelicula")
    db.close()

#Reporte
cant_productos = IntVar()
cant_disponibles = IntVar()
jabas_vendidas = IntVar()


cant_pedido = IntVar()
total = IntVar()


# Interfaz
imagen1=PhotoImage(file="C:\pro\pilsener.gif")
label1 = Label(ventana, image=imagen1)
label1.grid(row=0,column=1)


ventana.title('Principal')
ventana.config(bg='#717D7E')
ventana.geometry('700x350')

#Cantidad Productos
etiqueta1 = Label(ventana, text="Cantidad de Productos").place(x=10,y=10)
productosCaja = Entry(ventana, textvariable=cant_productos).place(x=10,y=40)
etiqueta2 = Label(ventana, text="Cantidad Disponible ").place(x=10,y=70)
disponibleCaja = Entry(ventana, textvariable=cant_disponibles).place(x=10,y=100)
etiqueta3 = Label(ventana, text="Num. Jabas Vendidas: ").place(x=10,y=130)
ventaCaja = Entry(ventana, textvariable=jabas_vendidas).place(x=10,y=170)

boton = Button(ventana, text="INGRESAR, command= guarda").grid(row=5, column=1)

#Pedidos
etiqueta4 = Label(ventana,text="Cantidad de jabas a pedir").place(x=500,y=130)
pedidocaja = Entry(ventana, textvariable=cant_pedido).place(x=500,y=160)
boton2 = Button(ventana, text="ENVIAR CORREO").place(x=530,y=320)

cnx.close()
ventana.mainloop()
