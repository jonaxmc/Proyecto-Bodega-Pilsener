import pymysql
from tkinter import *
from tkinter import messagebox


ventana = Tk()

#Datos de la conexion con la base de datos
dbc = ("localhost","root","12345","proyectosl")

#Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2])

# Obtener el cursor
cursor = db.cursor()

#consultar la version de MySQL
cursor.execute("SELECT VERSION()")

# Obtener una sola fila
dato = cursor.fetchone()

# imprimir el dato
print("La version de MySQL es:", dato)

#Guardar Datos

def guarda():
    a=cant_productos.get()
    c=jabas_vendidas.get()
    resta=a-c

    sql = "INSERT INTO `proyectosl`.`venta`(`cant_productos`, `cant_disponibles`,`jabas_vendidas`) \
          VALUES('%s', '%s', '%s')" % \
                (a,resta,c)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    messagebox.showinfo("Guardado", "Se a registrado correctamente")
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
etiqueta2 = Label(ventana, text="Num. Jabas Vendidas: ").place(x=10,y=70)
ventaCaja = Entry(ventana, textvariable=jabas_vendidas).place(x=10,y=100)
boton = Button(ventana, text="INGRESAR", command=guarda).place(x=40,y=130)

#Pedidos
etiqueta3 = Label(ventana,text="Cantidad de jabas a pedir").place(x=500,y=130)
pedidocaja = Entry(ventana, textvariable=cant_pedido).place(x=500,y=160)
boton2 = Button(ventana, text="ENVIAR CORREO").place(x=530,y=320)

ventana.mainloop()
