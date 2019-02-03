import pymysql
from tkinter import *
from tkinter import messagebox


# datos de conexion
dbc = ("localhost","root","12345","proyectosl")

# Abrir conexion con MySQL
db = pymysql.connect(dbc[0],dbc[1],dbc[2],dbc[3])

# Obtener el cursor
cursor = db.cursor()

#consultar la version de MySQL
cursor.execute("SELECT VERSION()")

# Obtener una sola fila
dato = cursor.fetchone()

# imprimir el dato
print("La version de MySQL es:", dato)



def registrar_usuario():

    nom=nombre.get()
    email=correo.get()
    con=contraseña.get()
    ap=apellido.get()

    sql = "INSERT INTO `proyectosl`.`usuarios` (`nombre`, `correo`,`pass`, `apellido`) \
            VALUES( '%s', '%s', '%s', '%s')" % \
                (nom,email,con,ap)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    messagebox.showinfo("Guardado", "Se ha registrado el usuario")
    db.close()


ventana = Tk()
nombre = StringVar()
apellido = StringVar()
correo = StringVar()
contraseña=StringVar()

ventana.title("REGISTRO")
ventana.geometry("250x400")
etiqueta = Label(ventana, text="NOMBRE: ").place(x=10,y=10)
generoCaja = Entry(ventana, textvariable=nombre).place(x=10,y=40)
etiqueta2 = Label(ventana, text="APELLIDO: ").place(x=10,y=70)
tituloCaja = Entry(ventana, textvariable=apellido).place(x=10,y=100)
etiqueta3 = Label(ventana, text="CORREO(@gmail.com): ").place(x=10,y=130)
resumenCaja = Entry(ventana, textvariable=correo).place(x=10,y=170)
etiqueta4 = Label(ventana, text="CONTRASEÑA: ").place(x=10,y=200)
añoCaja = Entry(ventana, textvariable=contraseña).place(x=10,y=230)

boton = Button(ventana, text="REGISTAR", command=registrar_usuario).place(x=50,y=320)
ventana.mainloop()