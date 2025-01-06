#creación de un sistema para una tienda online.
# Clase producto
class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        return f"Producto: {self.nombre} {self.precio} {self.stock}"

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_producto}) - Precio: {self.precio} - Stock: {self.stock}"

# Clase cliente
class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.carrito = []

    def agregar_carrito(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)
        else:
            print(f"Stock insuficiente para {producto.nombre}.")

    def ver_carrito(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            print(f"Carrito de {self.nombre}:")
            for producto, cantidad in self.carrito:
                print(f"{producto.nombre} - Cantidad: {cantidad}")

# Clase tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos disponibles.")
        else:
            print("Productos disponibles:")
            for producto in self.productos:
                print(producto)


if __name__ == "__main__":
    # Crear la tienda
    tienda = Tienda("Tienda Online")

    # Crear productos
    producto1 = Producto(1, "PlayStation 5", 2300, 5)
    producto2 = Producto(2, "iPhone", 950, 9)

    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    # Mostrar productos disponibles
    tienda.mostrar_productos()

    # Crear cliente
    cliente1 = Cliente(1, "Lucia Bravo")

    # Registrar cliente
    tienda.agregar_cliente(cliente1)

    # Cliente agrega productos al carrito
    cliente1.agregar_carrito(producto1, 2)
    cliente1.agregar_carrito(producto2, 1)

    # Ver carrito del cliente
    cliente1.ver_carrito()

    # Mostrar productos después de la compra
    print("\nProductos después de la compra:")
    tienda.mostrar_productos()















