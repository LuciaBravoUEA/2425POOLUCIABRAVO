
#Desarrollar un sistema avanzado de gestión de inventarios para una tienda,que incorpore colecciones

import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }


class Inventario:
    def __init__(self, archivo_datos="inventario.json"):
        self.productos = {}
        self.archivo_datos = archivo_datos
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivos()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivos()
            return True
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_en_archivos()
            return True
        return False

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivos(self):
        with open(self.archivo_datos, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)
                for d in datos:
                    producto = Producto(d['id_producto'], d['nombre'], d['cantidad'], d['precio'])
                    self.productos[producto.id_producto] = producto
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def menu(self):
        while True:
            print("\n--- Sistema de gestión de Inventario ---")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto por nombre")
            print("5. Mostrar todos los productos")
            print("6. Salir")
            opcion = input("Escribe una opción: ")

            if opcion == "1":
                id_producto = input("Escribe el id del producto: ")
                nombre = input("Escribe el nombre del producto: ")
                cantidad = input("Escribe la cantidad del producto: ")
                precio = input("Escribe el precio del producto: ")

                try:
                    cantidad = int(cantidad)
                    precio = float(precio)
                    self.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
                    print("Producto agregado exitosamente")
                except ValueError:
                    print("Error: La cantidad y el precio deben ser valores numéricos.")

            elif opcion == "2":
                id_producto = input("Escribe el id del producto: ")
                if self.eliminar_producto(id_producto):
                    print("Producto eliminado exitosamente")
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                id_producto = input("ID del producto a actualizar: ")
                nueva_cantidad = input("Nueva cantidad (deje vacío para no cambiar): ")
                nuevo_precio = input("Nuevo precio (deje vacío para no cambiar): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                if self.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio):
                    print("Producto actualizado exitosamente")
                else:
                    print("Producto no encontrado.")

            elif opcion == "4":
                nombre = input("Escribe el nombre del producto: ")
                resultados = self.buscar_producto(nombre)
                if resultados:
                    for r in resultados:
                        print(r)
                else:
                    print("Producto no encontrado.")

            elif opcion == "5":
                productos = self.mostrar_todos()
                for p in productos:
                    print(p)

            elif opcion == "6":
                print("Saliendo...")
                break

            else:
                print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    inventario = Inventario()
    inventario.menu()








