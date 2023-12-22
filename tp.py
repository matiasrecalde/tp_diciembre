import tkinter
from tkinter import ttk


contactos = []

def agregar_contacto():
    nombre=caja_nombre.get()
    telefono=caja_telefono.get()
    contacto={"Nombre" :nombre, "Telefono" :telefono}
    contactos.append(contacto)
    treeview.insert("", tkinter.END , values=(telefono))

def eliminar_contacto():
    selection = treeview.selection()
    for a in selection:
        treeview.delete(a)

def salir_contactos():
    ventana.destroy()


#Creando la ventana tk
ventana = tkinter.Tk()
ventana.title("Gestor de contactos") # titulo a la ventana

etiqueta_nombre = tkinter.Label(text= "Nombre:")
etiqueta_nombre.pack()
caja_nombre = tkinter.Entry(ventana)
caja_nombre.pack()


etiqueta_numero = tkinter.Label(text= "Numero:")
etiqueta_numero.pack()
caja_telefono = tkinter.Entry(ventana)
caja_telefono.pack()


boton_eliminar= tkinter.Button(ventana,text="eliminar",bg= "red", command= eliminar_contacto,width=20)
boton_eliminar.pack()

boton_agregar= tkinter.Button(ventana,text="agregar",bg= "light green", command= agregar_contacto,width=20)
boton_agregar.pack()

boton_salir= tkinter.Button(ventana,text="salir",bg= "sky blue", command= salir_contactos ,width=20)
boton_salir.pack()


treeview = ttk.Treeview(ventana,columns=("tel"))
treeview.heading("#0" , text="Nombre")
treeview.heading("tel" , text = "Telefono")
treeview.pack()


ventana.mainloop()
