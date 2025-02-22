# desarrollo de un sistema de gestión de inventarios simple para una tienda de costemticos de belleza
# definir la clase
# Desarrollo de un sistema de gestión de inventarios simple para una tienda
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id_producto(self):
        return self._id_producto

    def set_id_producto(self, value):
        self._id_producto = value

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, value):
        self._nombre = value

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, value):
        self._cantidad = value

    def get_precio(self):
        return self._precio

    def set_precio(self, value):
        self._precio = value

    def __str__(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]
        print("Producto eliminado (si existía).")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for p in self.productos:
                print(p)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu()
