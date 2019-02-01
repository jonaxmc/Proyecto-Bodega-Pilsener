import pymysql
from tkinter import *
from tkinter import messagebox, StringVar

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



def base():


    user = usuario.get()
    con = contraseña.get()
    email = correo.get()

    loop = 'true'
    while (loop == 'true'):

        if (
                cursor.execute(
                    "SELECT * FROM `usuarios` WHERE `correo`='" + email + "' AND `pass`='" + con + "'")):

            db.commit()



            r = Tk()  # Opens new window
            r.title('Bodega Pilsener')
            r.geometry('200x50')  # Makes the window a certain size
            rlbl = Label(r, text='\nBienvenido '+ user)  # "logged in" label
            rlbl.pack()
            r.mainloop()
            loop= 'false'
        else:
            db.commit()
            r = Tk()
            r.title('Datos Incorrectos:')
            r.geometry('200x50')
            rlbl = Label(r, text='\nUsuario o Contraseña Incorrectos!')
            rlbl.pack()
            r.mainloop()
            loop = 'false'




ventana = Tk()
apellido=StringVar()
usuario=StringVar()
contraseña=StringVar()
correo=StringVar()
ventana.geometry("400x200")
ventana.title("Iniciar Sesion")

etiqueta1= Label(ventana,text="Usuario: ", font=('', 15), pady=5, padx=5).grid(sticky=W)
cajaNombre= Entry(ventana, textvariable=correo, bd=3, font=('', 12)).grid(row=0, column=1)

etiqueta3= Label(ventana,text="Contraseña: ", font=('', 15), pady=5, padx=5).grid(sticky=W)
cajaResumen= Entry(ventana, textvariable=contraseña, bd=3, font=('', 12), show='*').grid(row=1, column=1)

boton = Button(ventana,text="Iniciar Sesión", bd=3, font=('', 15), padx=5, pady=5, command=base).grid(row=2,column=1)
boton = Button(ventana,text="Registrarse", bd=3, font=('', 13), padx=5, pady=5, command=base).grid(row=3,
                                                                                                         column=1)


ventana.mainloop()














