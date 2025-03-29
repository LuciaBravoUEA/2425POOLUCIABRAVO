# Realizar una aplicación GUI simple para gestionar una lista de tareas
import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea a la lista
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_index = task_list.curselection()[0]
        task = task_list.get(selected_index)  # Obtener la tarea seleccionada
        task_list.delete(selected_index)
        task_list.insert(selected_index, f"✔ {task}")  # Marcar como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Función para la pulsación de la tecla Enter
def on_enter_pressed(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Entrada de texto para escribir una nueva tarea
task_entry = tk.Entry(root, width=45)
task_entry.pack(pady=10)  # Corregido el uso de pack()
task_entry.bind("<Return>", on_enter_pressed)

# Botón para añadir una tarea
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()

# Lista de tareas donde se mostrarán las tareas
task_list = tk.Listbox(root, width=45, height=15)
task_list.pack(pady=10)

# Botón para marcar una tarea como completada
complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.pack()

# Botón para eliminar una tarea
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

# Iniciar la aplicación
root.mainloop()
