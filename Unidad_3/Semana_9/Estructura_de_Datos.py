# desarrollo de un sistema de gestión de inventarios simple para una tienda
# definir la clase
# Desarrollo de un sistema de gestión de inventarios simple para una tienda

# Definir la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto} Nombre: {self.nombre} Cantidad: {self.cantidad} Precio: $ {self.precio}"


# definir la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: ya existe un producto con este ID.")
            return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
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

