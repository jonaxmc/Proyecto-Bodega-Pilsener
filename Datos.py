import pymysql
from tkinter import *
from tkinter import messagebox


ventana = Tk()

dbc = ("localhost","root","12345","proyectosl")
db = pymysql.connect(dbc[0],dbc[1],dbc[2])
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
dato = cursor.fetchone()
print("La version de MySQL es:", dato)


conexion = pymysql.connect("localhost","root","12345","proyectosl")
cur = conexion.cursor()
tabla = "SELECT cant_disponibles FROM venta order by id_venta DESC LIMIT 1;"
cur.execute(tabla)
filas = cur.fetchall()

#Creando una lista
lstVentas=Listbox(ventana,width=10,height=10)
for fila in filas:
   print(fila)
   lstVentas.insert(0,fila)
lstVentas.place(x=530,y=70)

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



lblVentas=Label(ventana,text="Cantidad Disponible:").place(x=500,y=40)

#Cantidad Productos
etiqueta1 = Label(ventana, text="Cantidad de Productos").place(x=10,y=180)
productosCaja = Entry(ventana, textvariable=cant_productos).place(x=10,y=210)

etiqueta2 = Label(ventana, text="Num. Jabas Vendidas: ").place(x=10,y=240)
ventaCaja = Entry(ventana, textvariable=jabas_vendidas).place(x=10,y=270)

boton = Button(ventana, text="INGRESAR", command=guarda).place(x=40,y=300)

#Pedidos
etiqueta3 = Label(ventana,text="Cantidad de jabas a pedir").place(x=300,y=40)
pedidocaja = Entry(ventana, textvariable=cant_pedido).place(x=300,y=70)
boton2 = Button(ventana, text="ENVIAR CORREO").place(x=320,y=115)


conexion.commit()
conexion.close()
ventana.mainloop()
