#Desarrollar una aplicación GUI que permita a los usuarios gestionar una lista de tareas pendientes
import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea a la lista
def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

# Función para marcar una tarea como completada
def mark_completed(event=None):
    try:
        selected_index = task_list.curselection()[0]
        task = task_list.get(selected_index)
        if not task.startswith("✔ "):
            task_list.delete(selected_index)
            task_list.insert(selected_index, f"✔ {task}")
            task_list.itemconfig(selected_index, {'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Entrada de texto para escribir una nueva tarea
task_entry = tk.Entry(root, width=45)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

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

# Atajos de teclado
root.bind("<c>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", lambda event: root.quit())

# Iniciar la aplicación
root.mainloop()