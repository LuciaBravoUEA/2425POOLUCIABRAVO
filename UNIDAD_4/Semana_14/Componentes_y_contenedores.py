#Creación de una aplicación para una agenda personal
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime


# Función para agregar un evento a la lista
def agregar_evento():
    # Obtener los valores de los campos de entrada
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Validar si todos los campos están llenos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Entrada incompleta", "Por favor, complete todos los campos.")
        return

    try:
        # Validar formato de fecha (DD/MM/YYYY)
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
    except ValueError:
        messagebox.showerror("Error de fecha", "El formato de la fecha es incorrecto. Usa DD/MM/YYYY.")
        return

    # Agregar el evento a la lista
    treeview.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada
    entrada_fecha.delete(0, tk.END)
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)


# Función para eliminar un evento seleccionado
def eliminar_evento():
    # Obtener el evento seleccionado
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione un evento para eliminar.")
        return

    # Confirmación de eliminación
    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este evento?")
    if confirmacion:
        treeview.delete(selected_item)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Crear un Frame para la lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Crear el Treeview para mostrar los eventos
treeview = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")
treeview.pack()

# Crear un Frame para la entrada de nuevos eventos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiqueta y campo de entrada para la fecha
etiqueta_fecha = tk.Label(frame_entrada, text="Fecha (DD/MM/YYYY):")
etiqueta_fecha.grid(row=0, column=0, padx=5)
entrada_fecha = tk.Entry(frame_entrada)
entrada_fecha.grid(row=0, column=1, padx=5)

# Etiqueta y campo de entrada para la hora
etiqueta_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
etiqueta_hora.grid(row=1, column=0, padx=5)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=5)

# Etiqueta y campo de entrada para la descripción
etiqueta_descripcion = tk.Label(frame_entrada, text="Descripción:")
etiqueta_descripcion.grid(row=2, column=0, padx=5)
entrada_descripcion = tk.Entry(frame_entrada)
entrada_descripcion.grid(row=2, column=1, padx=5)

# Crear un Frame para los botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botón para agregar evento
boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=5)

# Botón para eliminar evento
boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=5)

# Botón para salir de la aplicación
boton_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
boton_salir.grid(row=0, column=2, padx=5)

# Iniciar la aplicación
ventana.mainloop()
