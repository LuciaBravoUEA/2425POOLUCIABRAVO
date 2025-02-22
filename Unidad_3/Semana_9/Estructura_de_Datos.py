# desarrollo de un sistema de gestión de inventarios simple para una tienda de costemticos de belleza
# definir la clase
# Desarrollo de un sistema de gestión de inventarios simple para una tienda
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.set_id_producto(id_producto)
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    def __str__(self):
        return f"ID: {self.get_id_producto()} | Nombre: {self.get_nombre()} | Cantidad: {self.get_cantidad()} | Precio: ${self.get_precio()}"

    # Métodos getter y setter para id_producto
    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    # Métodos getter y setter para nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Métodos getter y setter para cantidad
    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Métodos getter y setter para precio
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if any(p.get_id_producto() == id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id_producto() != id_producto]
        print("Producto eliminado exitosamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")
if __name__ == "__main__":
    inventario = Inventario()
    inventario.agregar_producto("001", "labial", 10, 7.50)
    inventario.agregar_producto("002", "Base", 50, 4.80)
    inventario.agregar_producto("003", "lápiz labial", 30, 1.50)
    inventario.agregar_producto("004", "Rubor", 80, 4.50)
    inventario.agregar_producto("005", "Polvo translucido", 40, 7.00)
    inventario.agregar_producto("006", "Sombras", 90,  3.00)
    inventario.agregar_producto("007", "Serum", 20, 5.00)
    inventario.agregar_producto("008", "Crema", 10, 8.00)
    inventario.agregar_producto("009", "Corrector de ojeras", 150, 3.50)
    inventario.agregar_producto("010", "Paleta de contornos", 60, 8.00)
    inventario.agregar_producto("011", "Delineador", 30, 4.70)

    inventario.mostrar_inventario()


