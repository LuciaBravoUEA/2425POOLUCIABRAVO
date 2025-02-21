# desarrollo del sistema de inventario  utilizando archivos para archivos de
# almacenar y recuperar la información del inventario y manejo de excepciones.

import json
import os

# Definir la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto} Nombre: {self.nombre} Cantidad: {self.cantidad} Precio: $ {self.precio}"


# Definir la clase Inventario
class Inventario:
# agregamos el nombre del archivo que se almacenera la lista de productos
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                json.dump([p.__dict__ for p in self.productos], file)
            print("Inventario guardado exitosamente.")
# usamor PermissionError para dar permisos y poder escribir en el archivo
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            print("Archivo no encontrado, creando nuevo archivo de inventario.")
            self.guardar_en_archivo()  # Crea el archivo si no existe
        try:
            with open(self.archivo, "r") as file:
                productos_cargados = json.load(file)
                self.productos = [Producto(**p) for p in productos_cargados]
            print("Inventario cargado exitosamente.")
    # usamos FiliNotFoundError si el archivo no existe, no esta en el directorio.
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = []
            print("Error al cargar el inventario, archivo corrupto o vacío.")

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: ya existe un producto con este ID.")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no existe.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no existe.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("Error: No se encontraron productos.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("Error: No hay productos en el inventario.")

    def menu(self):
        while True:
            print("\n1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Mostrar inventario")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "6":
                print("Saliendo del sistema...")
                break

            elif opcion == "1":
                id_producto = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    precio = float(input("Ingrese el precio del producto: "))
                    producto = Producto(id_producto, nombre, cantidad, precio)
                    self.agregar_producto(producto)  # Se usa self en lugar de inventario
                except ValueError:
                    print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

            elif opcion == "2":
                id_producto = input("Ingrese el ID del producto a eliminar: ")
                self.eliminar_producto(id_producto)  # Se usa self

            elif opcion == "3":
                id_producto = input("Ingrese el ID del producto a actualizar: ")
                cantidad = input("Ingrese la nueva cantidad del producto (dejar en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio del producto (dejar en blanco para no cambiar): ")

                cantidad = int(cantidad) if cantidad.strip() else None
                precio = float(precio) if precio.strip() else None

                self.actualizar_producto(id_producto, cantidad, precio)  # Se usa self

            elif opcion == "4":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                self.buscar_producto(nombre)  # Se usa self

            elif opcion == "5":
                self.mostrar_inventario()  # Se usa self

            else:
                print("Error: Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    inventario = Inventario()
    inventario.menu()
