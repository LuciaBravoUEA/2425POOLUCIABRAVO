# Creación de una Aplicación GUI Básica

# Libreria Tkinter
import tkinter as tk
from tkinter import messagebox

def insertar_dato():
    dato = entry.get()
    if dato:
        listbox.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning( "Advertencia",  "El campo de texto esta vacio")

def limpiar_lista():
    listbox.delete(0, tk.END)

#Crear ventana principal
root = tk.Tk()
root.title("Sistema GUI Lucy Bravo")
root.geometry("400x400")

#Crear widgets
label = tk.Label(root, text="Ingrese un dato") #etiqueta
entry = tk.Entry(root)
btn_agregar = tk.Button(root, text="Agregar", command=insertar_dato)
btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
listbox = tk.Listbox(root)

# ubicar widgets en la ventana
label.pack(pady=5)
entry.pack(pady=5)
btn_agregar.pack(pady=5)
listbox.pack(pady=5, fill=tk.BOTH, expand=True)
btn_limpiar.pack(pady=5)

#Ejecutar la aplicación
root.mainloop()


