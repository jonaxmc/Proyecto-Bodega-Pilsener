from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import *
from tkinter import messagebox, StringVar
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
email=None
con=None


class Aplicacion():
    ''' Clase Aplicacion '''



    ventana = 0
    posx_y = 0

    def __init__(self):
        ''' Construye ventana de aplicación '''

        # Declara ventana de aplicación
        def base():

            global con
            con = contraseña.get()
            global email
            email = correo.get()

            loop = 'true'
            while (loop == 'true'):

                if (
                        cursor.execute(
                            "SELECT * FROM `usuarios` WHERE `correo`='" + email + "' AND `pass`='" + con + "'")):

                    db.commit()

                    self.raiz.destroy()
                    self.abrir()

                    loop = 'false'
                else:
                    db.commit()
                    r = Tk()
                    r.title('Datos Incorrectos:')
                    r.geometry('200x50')
                    rlbl = Label(r, text='\nUsuario o Contraseña Incorrectos!')
                    rlbl.pack()
                    r.mainloop()
                    loop = 'false'




        self.raiz = Tk()



        # Define dimensión de la ventana 300x200
        # que se situará en la coordenada x=500,y=50
        apellido = StringVar()
        usuario = StringVar()
        contraseña = StringVar()
        correo = StringVar()
        self.raiz.geometry("400x200")

        self.raiz.resizable(0, 0)
        self.raiz.title("Login")

        # Define botón 'Abrir' que se utilizará para
        # abrir las ventanas de diálogo. El botón
        # está vinculado con el método 'self.abrir'

        etiqueta1 = Label(self.raiz, text="Correo : ", font=('', 15), pady=5, padx=5).grid(sticky=W)
        cajaNombre = Entry(self.raiz, textvariable=correo, bd=3, font=('', 12)).grid(row=0, column=1)

        etiqueta3 = Label(self.raiz, text="Contraseña: ", font=('', 15), pady=5, padx=5).grid(sticky=W)
        cajaResumen = Entry(self.raiz, textvariable=contraseña, bd=3, font=('', 12), show='*').grid(row=1, column=1)

        boton = Button(self.raiz, text="Iniciar Sesión", bd=3, font=('', 15), padx=5, pady=5, command=base).grid(row=2,
                                                                                                                column=1)
        ##boton = Button(self.raiz, text="Registrarse", bd=3, font=('', 13), padx=5, pady=5,command=registrar.grid(row=3, column=1)



        self.raiz.mainloop()



    def abrir(self):
        ''' Construye una ventana de diálogo '''

        # Define una nueva ventana de diálogo


        self.dialogo = Tk()

        # Incrementa en 1 el contador de ventanas

        Aplicacion.ventana += 1

        # Recalcula posición de la ventana

        Aplicacion.posx_y += 50
        tamypos = '700x350+' + str(Aplicacion.posx_y) + \
                  '+' + str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)

        # Obtiene identicador de la nueva ventana

        ident = self.dialogo.winfo_id()

        # Construye mensaje de la barra de título

        titulo = str(Aplicacion.ventana) + ": " + str(ident)
        self.dialogo.title(titulo)



        #---------------------------------------------------------------------------------

        conexion = pymysql.connect("localhost", "root", "12345", "proyectosl")
        cur = conexion.cursor()
        tabla = "SELECT cant_disponibles FROM venta order by id_venta DESC LIMIT 1;"
        cur.execute(tabla)
        filas = cur.fetchall()

        # Creando una lista
        lstVentas = Listbox(self.dialogo, width=10, height=10)

        for fila in filas:
            lstVentas.insert(0, fila)
        lstVentas.place(x=530, y=70)

        # Guardar Datos

        def guarda():

            a = cant_productos.get()
            c = jabas_vendidas.get()
            resta = a - c

            sql = "INSERT INTO `proyectosl`.`venta`(`cant_productos`, `cant_disponibles`,`jabas_vendidas`) \
                          VALUES('%s', '%s', '%s')" % \
                  (a, resta, c)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            messagebox.showinfo("Guardado", "Se a registrado correctamente")


        def refrescar():
            conexion = pymysql.connect("localhost", "root", "12345", "proyectosl")
            cur = conexion.cursor()
            tabla = "SELECT cant_disponibles FROM venta order by id_venta DESC LIMIT 1;"
            cur.execute(tabla)
            filas = cur.fetchall()

            # Creando una lista
            lstVentas = Listbox(self.dialogo, width=10, height=10)
            for fila in filas:
                print(fila)
                lstVentas.insert(0, fila)
            lstVentas.place(x=530, y=70)


        # Reporte
        cant_productos = IntVar()
        cant_disponibles = IntVar()
        jabas_vendidas = IntVar()

        cant_pedido = IntVar()
        total = IntVar()

        # Interfaz
        imagen1 = PhotoImage(file="F:\pilsener.gif")
        label1 = Label(self.dialogo, image=imagen1)
        label1.grid(row=0, column=1)


        def enviar():


            c = cant_pedido.get()
            s = str(c)

            smail=str(email)
            scon=str(con)

            #user = smail
            #password = "bodega12345"

            # Para las cabeceras del email
            remitente = "<bodegapilsener@gmail.com>"
            destinatario = "<pazospaul@hotmail.com>"
            asunto = "Pedido de cerveza\n\n"
            mensaje = "Sr.Administrador\n\n" \
                      "Por medio de la presente, solicito muy cordialmente que se me envié la cantidad de " + s + " jabas de cerveza\n\n"



            # Host y puerto SMTP de Gmail
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            # protocolo de cifrado de datos utilizado por gmail
            gmail.starttls()

            # Credenciales
            gmail.login(smail, scon)

            # muestra la depuración de la operacion de envío 1=true
            gmail.set_debuglevel(1)

            header = MIMEMultipart()
            header['Subject'] = asunto
            header['From'] = remitente
            header['To'] = destinatario

            mensaje = MIMEText(mensaje, 'html')  # Content-type:text/html
            header.attach(mensaje)

            # Enviar email
            gmail.sendmail(remitente, destinatario, header.as_string())

            # Cerrar la conexión SMTP
            gmail.quit()

        lblVentas = Label(self.dialogo, text="Cantidad Disponible:").place(x=500, y=40)
        boton1 = Button(self.dialogo, text="ACTUALIZAR", command=refrescar).place(x=600, y=300)

        # Cantidad Productos
        etiqueta1 = Label(self.dialogo, text="Cantidad de Productos").place(x=10, y=180)
        productosCaja = Entry(self.dialogo, textvariable=cant_productos).place(x=10, y=210)

        etiqueta2 = Label(self.dialogo, text="Num. Jabas Vendidas: ").place(x=10, y=240)
        ventaCaja = Entry(self.dialogo, textvariable=jabas_vendidas).place(x=10, y=270)

        boton = Button(self.dialogo, text="INGRESAR", command=guarda).place(x=40, y=300)

        # Pedidos
        etiqueta3 = Label(self.dialogo, text="Cantidad de jabas a pedir").place(x=300, y=40)
        pedidocaja = Entry(self.dialogo, textvariable=cant_pedido).place(x=300, y=70)

        boton2 = Button(self.dialogo, text="ENVIAR CORREO", command=enviar).place(x=320, y=115)

        conexion.commit()
        conexion.close()



        #--------------------------------------------------------------------------------


        # Cuando la ejecución del programa llega a este
        # punto se utiliza el método wait_window() para
        # esperar que la ventana 'self.dialogo' sea
        # destruida.
        # Mientras tanto se atiende a los eventos locales
        # que se produzcan, por lo que otras partes de la
        # aplicación seguirán funcionando con normalidad.
        # Si hay código después de esta línea se ejecutará
        # cuando la ventana 'self.dialogo' sea cerrada.

        self.raiz.wait_window(self.dialogo)





def main():
    mi_app = Aplicacion()
    return (0)


if __name__ == '__main__':
    main()