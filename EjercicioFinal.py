from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


raiz=Tk()
raiz.title('Modulos y paquetes')

nombre = StringVar()
aPaterno = StringVar()
aMaterno = StringVar()
correo = StringVar()
movil = StringVar()
dedicacion = StringVar()
estado=StringVar()
leer = BooleanVar()
musica = BooleanVar()
videojuegos = BooleanVar()

#-----------------------------------------------------BOTONES-------------------------------------------------------------------------
def guardarBDD():
    nombreUsuario=nombreEntry.get()
    aPaternoUsuario=aPaternoEntry.get()
    aMaternoUsuario=aMaternoEntry.get()
    correoUsuario=correoEntry.get()
    movilUsuario=movilEntry.get()
    dedicacionUsuario=dedicacion.get()
    estadoUsuario=estado.get()
    leerUsuario=leer.get()
    if leerUsuario==True:
        leerUser="si"
    else:
        leerUser="no"
    musicaUsuario=musica.get()
    if musicaUsuario==True:
        musicaUser="si"
    else:
        musicaUser="no"
    videojuegosUsuario=videojuegos.get
    if videojuegosUsuario==True:
        videojuegosUser="si"
    else:
        videojuegosUser="no"

    if not nombreUsuario :  # si el Entry está vacío
        messagebox.showerror("Error", "Por favor ingrese un nombre")
    elif not aPaternoUsuario:
        messagebox.showerror("Error", "Por favor ingrese un apellido paterno")
    elif not aMaternoUsuario:
        messagebox.showerror("Error", "Por favor ingrese un apellido materno")
    elif not correoUsuario:
        messagebox.showerror("Error", "Por favor ingrese un correo")
    elif not movilUsuario:
        messagebox.showerror("Error", "Por favor ingrese un movil")
    elif not dedicacionUsuario:
        messagebox.showerror("Error", "Por favor seleccione una ocupacion")
    elif not estadoUsuario:
        messagebox.showerror("Error", "Por favor seleccione un estado")
        
    else:
        tv2.insert("","end", values=(nombreUsuario, aPaternoUsuario, aMaternoUsuario, correoUsuario, movilUsuario, dedicacionUsuario, estadoUsuario, leerUser, musicaUser, videojuegosUser))
        conexion = sqlite3.connect('ejerciciofinal.db')
        c= conexion.cursor()

        #c.execute('''CREATE TABLE usuariosBD (nombre text, aPaterno text, aMaterno text, correo text, movil text, dedicacion text, estado text, leer text, musica text, videojuegos text)''')

        usuarios = [(nombreUsuario, aPaternoUsuario,aMaternoUsuario,correoUsuario,movilUsuario,dedicacionUsuario,estadoUsuario,leerUser,musicaUser,videojuegosUser)]
        c.executemany('INSERT INTO usuariosBD VALUES (?,?,?,?,?,?,?,?,?,?)', usuarios)

        conexion.commit()
        conexion.close()
        cancelar()


def guardar():
    nombreUsuario=nombreEntry.get()
    aPaternoUsuario=aPaternoEntry.get()
    aMaternoUsuario=aMaternoEntry.get()
    correoUsuario=correoEntry.get()
    movilUsuario=movilEntry.get()
    dedicacionUsuario=dedicacion.get()
    estadoUsuario=estado.get()
    leerUsuario=leer.get()
    if leerUsuario==True:
        leerUser="si"
    else:
        leerUser="no"
    musicaUsuario=musica.get()
    if musicaUsuario==True:
        musicaUser="si"
    else:
        musicaUser="no"
    videojuegosUsuario=videojuegos.get
    if videojuegosUsuario==True:
        videojuegosUser="si"
    else:
        videojuegosUser="no"

    if not nombreUsuario :  # si el Entry está vacío
        messagebox.showerror("Error", "Por favor ingrese un nombre")
    elif not aPaternoUsuario:
        messagebox.showerror("Error", "Por favor ingrese un apellido paterno")
    elif not aMaternoUsuario:
        messagebox.showerror("Error", "Por favor ingrese un apellido materno")
    elif not correoUsuario:
        messagebox.showerror("Error", "Por favor ingrese un correo")
    elif not movilUsuario:
        messagebox.showerror("Error", "Por favor ingrese un movil")
    elif not dedicacionUsuario:
        messagebox.showerror("Error", "Por favor seleccione una ocupacion")
    elif not estadoUsuario:
        messagebox.showerror("Error", "Por favor seleccione un estado")
        
    else:
        with open ("CSVEjercicio.csv", "a") as file:
            file.write(f"{nombreUsuario}, {aPaternoUsuario}, {aMaternoUsuario}, {correoUsuario}, {movilUsuario}, {dedicacionUsuario}, {estadoUsuario}, {leerUser}, {musicaUser}, {videojuegosUser}, \n")

        tv.insert("","end", values=(nombreUsuario, aPaternoUsuario, aMaternoUsuario, correoUsuario, movilUsuario, dedicacionUsuario, estadoUsuario, leerUser, musicaUser, videojuegosUser))
        cancelar()
    
    

def cancelar():
    nombreEntry.delete(0,END)
    aPaternoEntry.delete(0,END)
    aMaternoEntry.delete(0,END)
    correoEntry.delete(0,END)
    movilEntry.delete(0,END)
    dedicacion.set(None)
    estado.set("")
    leer.set(False)
    musica.set(False)
    videojuegos.set(False)





#-----------------------------------------------------FRAME 1-------------------------------------------------------------------------
frame1=ttk.Frame(raiz, padding="20 30 20 30", relief="raised")
frame1.grid(column=0, row=0)
frameImagen=ttk.Frame(frame1, padding="20 5 20 5")
frameImagen.grid(column=0, row=0)
frameDatos=ttk.Frame(frame1, padding="20 5 243 5")
frameDatos.grid(column=1, row=0)

#ENTRYS
nombreEntry=ttk.Entry(frameDatos, width=40 ,textvariable=nombre)
nombreEntry.grid(column=3,row=1, sticky=(W), padx=10, pady=5)
aPaternoEntry=ttk.Entry(frameDatos, width=40 ,textvariable=aPaterno)
aPaternoEntry.grid(column=3,row=2, sticky=(W), padx=10, pady=5)
aMaternoEntry=ttk.Entry(frameDatos, width=40 ,textvariable=aMaterno)
aMaternoEntry.grid(column=3,row=3, sticky=(W), padx=10, pady=5)
correoEntry=ttk.Entry(frameDatos, width=40 ,textvariable=correo)
correoEntry.grid(column=3,row=4, sticky=(W), padx=10, pady=5)
movilEntry=ttk.Entry(frameDatos, width=40 ,textvariable=movil)
movilEntry.grid(column=3,row=5, sticky=(W), padx=10, pady=5)

#IMAGENES
imagenUsuario = PhotoImage(file="Usuario.png")
imagenUsuario_resized = imagenUsuario.subsample(2, 2) # Reducir a la mitad en ambos ejes

etqImagen=ttk.Label(frameImagen)
etqImagen.grid(sticky=(W), column=0, row=0, padx=0, pady=0)
etqImagen["image"] = imagenUsuario_resized


#LABELS        
ttk.Label(frameDatos, text="Nombre: ").grid(column=2, row=1, sticky=(W), padx=10, pady=5)
ttk.Label(frameDatos, text="A.Paterno: ").grid(column=2, row=2, sticky=(W), padx=10, pady=5) 
ttk.Label(frameDatos, text="A.Materno: ").grid(column=2, row=3, sticky=(W), padx=10, pady=5)
ttk.Label(frameDatos, text="Correo: ").grid(column=2, row=4, sticky=(W), padx=10, pady=5) 
ttk.Label(frameDatos, text="Movil: ").grid(column=2, row=5, sticky=(W), padx=10, pady=5)
ttk.Label(frameDatos, text="Datos: ", font=("arial",11, "bold")). grid(column=2, row=0, sticky=(W), padx=10, pady=5)
ttk.Label(frameDatos, text="Aficiones: ", font=("arial",11, "bold")).grid(column=4, row=0, sticky=(W), padx=10, pady=5)
ttk.Label(frameDatos, text="Ocupacion: ", font=("arial",11, "bold")).grid(column=5, row=0, sticky=(W), padx=10, pady=5)
ttk.Label(frameDatos, text="Estado: ", font=("arial",11, "bold")).grid(column=6, row=0, sticky=(W), padx=10, pady=5)

#CheckButton
rbleer = ttk.Checkbutton(frameDatos, text='Leer',variable=leer)
rbmusica = ttk.Checkbutton(frameDatos, text='Musica',variable=musica)
rbvideojuegos = ttk.Checkbutton(frameDatos, text='Videojuegos',variable=videojuegos)

rbleer.grid(column=4, row=1, sticky=(W), padx=10, pady=5)
rbmusica.grid(column=4, row=2, sticky=(W), padx=10, pady=5)
rbvideojuegos.grid(column=4, row=3, sticky=(W), padx=10, pady=5)


#BOTONES
Button(frameDatos, text="Guardar CSV", command=guardar, background='SpringGreen3', foreground='white',activebackground='SpringGreen4',font=("arial",11)).grid(column=2, row=9, sticky=(W), padx=10, pady=5)
Button(frameDatos, text="Cancelar", command=cancelar, background='firebrick3', foreground='white',activebackground='firebrick4',font=("arial",11)).grid(column=6, row=9, sticky=(E), padx=10, pady=5)
Button(frameDatos, text="Guardad BD", command=guardarBDD, background='DodgerBlue2', foreground='white',activebackground='DodgerBlue3',font=("arial",11)).grid(column=3, row=9, sticky=(W), padx=10, pady=5)


#RadioButton
rbestudiante = ttk.Radiobutton(frameDatos, text='Estudiante', value="Estudiante", variable=dedicacion)
rbempleado = ttk.Radiobutton(frameDatos, text='Empleado', value="Empleado", variable=dedicacion)
rbdesempleado = ttk.Radiobutton(frameDatos, text='Desempleado', value="Desempleado", variable=dedicacion)

rbestudiante.grid(column=5, row=1, sticky=(W), padx=10, pady=5)
rbempleado.grid(column=5, row=2, sticky=(W), padx=10, pady=5)
rbdesempleado.grid(column=5, row=3, sticky=(W), padx=10, pady=5)


#COMBOBOX
comboEstados = ttk.Combobox(frameDatos, textvariable=estado, state="readonly")
comboEstados.grid(column=6, row=1, sticky=(W), padx=10, pady=5)
comboEstados['values'] = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila", 
                        "Colima", "Chiapas", "Chihuahua", "Ciudad de Mexico", "Durango", "Guanajuato", 
                        "Guerrero", "Hidalgo", "Jalisco", "Mexico", "Michoacan", "Morelos", "Nayarit", 
                        "Nuevo Leon", "Oaxaca", "Puebla", "Queretaro", "Quintana Roo", "San Luis Potosi", 
                        "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatan", "Zacatecas")

#-----------------------------------------------------FRAME 2-------------------------------------------------------------------------
frameTabla=ttk.Frame(raiz, padding="20 30 20 30", relief="raised")
frameTabla.grid(column=0, row=1)

tabPanel = ttk.Notebook(frameTabla)

# Crear pestañas dentro del notebook
CSV = ttk.Frame(tabPanel)
BDD = ttk.Frame(tabPanel)

# Agregar las pestañas al notebook
tabPanel.add(CSV, text="CSV")
tabPanel.add(BDD, text="BDD")


# Empaquetar el notebook en la ventana
tabPanel.grid(column=0,row=0)

#Tabla CSV
tv = ttk.Treeview(CSV, columns=("nombre","aPaterno", "aMaterno", "correo", "movil", "dedicacion", "estado", "lee", "musica", "videojuegos"))
tv.grid(column=2, row=0, padx=0, pady=0)
tv.column("#0",width=30, anchor=CENTER)
tv.column("nombre",width=130, anchor=CENTER)
tv.column("aPaterno",width=130, anchor=CENTER)
tv.column("aMaterno",width=130, anchor=CENTER)
tv.column("correo",width=130, anchor=CENTER)
tv.column("movil",width=130, anchor=CENTER)
tv.column("dedicacion",width=130, anchor=CENTER)
tv.column("estado",width=130, anchor=CENTER)
tv.column("lee",width=130, anchor=CENTER)
tv.column("musica",width=130, anchor=CENTER)
tv.column("videojuegos",width=130, anchor=CENTER)

tv.heading("#0", text="#", anchor=CENTER)
tv.heading("nombre", text="Nombre", anchor=CENTER)
tv.heading("aPaterno", text="APaterno", anchor=CENTER)
tv.heading("aMaterno", text="AMaterno", anchor=CENTER)
tv.heading("correo", text="Correo", anchor=CENTER)
tv.heading("movil", text="Movil", anchor=CENTER)
tv.heading("dedicacion", text="Dedicacion", anchor=CENTER)
tv.heading("estado", text="Estado", anchor=CENTER)
tv.heading("lee", text="Lee", anchor=CENTER)
tv.heading("musica", text="Musica", anchor=CENTER)
tv.heading("videojuegos", text="Videojuegos", anchor=CENTER)

#Tabla BDD
tv2 = ttk.Treeview(BDD, columns=("nombre","aPaterno", "aMaterno", "correo", "movil", "dedicacion", "estado", "lee", "musica", "videojuegos"))
tv2.grid(column=2, row=0, padx=0, pady=0)
tv2.column("#0",width=30, anchor=CENTER)
tv2.column("nombre",width=130, anchor=CENTER)
tv2.column("aPaterno",width=130, anchor=CENTER)
tv2.column("aMaterno",width=130, anchor=CENTER)
tv2.column("correo",width=130, anchor=CENTER)
tv2.column("movil",width=130, anchor=CENTER)
tv2.column("dedicacion",width=130, anchor=CENTER)
tv2.column("estado",width=130, anchor=CENTER)
tv2.column("lee",width=130, anchor=CENTER)
tv2.column("musica",width=130, anchor=CENTER)
tv2.column("videojuegos",width=130, anchor=CENTER)

tv2.heading("#0", text="#", anchor=CENTER)
tv2.heading("nombre", text="Nombre", anchor=CENTER)
tv2.heading("aPaterno", text="APaterno", anchor=CENTER)
tv2.heading("aMaterno", text="AMaterno", anchor=CENTER)
tv2.heading("correo", text="Correo", anchor=CENTER)
tv2.heading("movil", text="Movil", anchor=CENTER)
tv2.heading("dedicacion", text="Dedicacion", anchor=CENTER)
tv2.heading("estado", text="Estado", anchor=CENTER)
tv2.heading("lee", text="Lee", anchor=CENTER)
tv2.heading("musica", text="Musica", anchor=CENTER)
tv2.heading("videojuegos", text="Videojuegos", anchor=CENTER)


#---------------------------------------------------ARCHIVO CSV-----------------------------------------------------------------------
with open ("CSVEjercicio.csv", "r") as file:
    for i, line in enumerate(file):
        datos=line.strip().split(",")
        nombreA=datos[0]
        aPaternoA=datos[1]
        aMaternoA=datos[2]
        correoA=datos[3]
        movilA=datos[4]
        dedicacionA=datos[5]
        estadoA=datos[6]
        leeA=datos[7]
        musicaA=datos[8]
        videojuegosA=datos[9]
        tv.insert("","end",text=str(i), values=(nombreA, aPaternoA, aMaternoA, correoA, movilA, dedicacionA, estadoA, leeA, musicaA, videojuegosA))

#---------------------------------------------------ARCHIVO BDD-----------------------------------------------------------------------
conexion = sqlite3.connect('ejerciciofinal.db')
c= conexion.cursor()
i=0
for row in c.execute("SELECT * FROM  usuariosBD"):
    userBDD = c.fetchall()
    for usuariobase in userBDD:
        i+=1
        tv2.insert("","end",text=str(i), values=(usuariobase[0], usuariobase[1], usuariobase[2], usuariobase[3], usuariobase[4], usuariobase[5], usuariobase[6], usuariobase[7], usuariobase[8], usuariobase[9]))

conexion.close()






raiz.mainloop()