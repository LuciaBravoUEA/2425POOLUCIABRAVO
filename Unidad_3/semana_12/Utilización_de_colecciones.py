#desarrollo de un sistema  de gestión de Biblioteca Digital.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla para título y autor (inmutable)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} por {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para IDs de usuarios únicos
        self.prestamos = {}  # Diccionario para registrar préstamos (user_id -> lista de ISBNs)

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios.add(usuario.user_id)
            self.prestamos[usuario.user_id] = []
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            if not self.prestamos[user_id]:
                self.usuarios.remove(user_id)
                del self.prestamos[user_id]
                print(f"Usuario con ID {user_id} eliminado.")
            else:
                print("El usuario tiene libros prestados. No se puede eliminar.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            if isbn not in self.prestamos[user_id]:
                self.prestamos[user_id].append(isbn)
                print(f"Libro {self.libros[isbn]} prestado a usuario ID {user_id}.")
            else:
                print("El usuario ya tiene este libro prestado.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.prestamos[user_id]:
            self.prestamos[user_id].remove(isbn)
            print(f"Libro con ISBN {isbn} devuelto por usuario ID {user_id}.")
        else:
            print("Usuario o libro no encontrado en préstamos.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = [libro for libro in self.libros.values()
                      if (titulo is None or libro.titulo_autor[0].lower() == titulo.lower())
                      and (autor is None or libro.titulo_autor[1].lower() == autor.lower())
                      and (categoria is None or libro.categoria.lower() == categoria.lower())]
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            libros_prestados = [self.libros[isbn] for isbn in self.prestamos[user_id]]
            return libros_prestados
        return []


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    libro1 = Libro("Jane Eyre", "Charlotte Bronte", "Novela", "9788497945394")
    libro2 = Libro("La Ilíada", "Homero", "Epopeya", "97884891635533")
    libro3 = Libro("Orgullo y Perjuicio", "Jane Austen", "Ficción", "9788467070835")
    libro4 = Libro("Mac beth", "Jo Nesbo", "Policial", "9788426405043")
    libro5 = Libro("Mardame Bovary", "Gustave Flaubert", "Realismo", "9788415089155")
    libro6 = Libro("Pedro Páramo", "Juan Rulfo", "Ficción", "97886646091")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)
    biblioteca.agregar_libro(libro5)
    biblioteca.agregar_libro(libro6)


    usuario1 = Usuario("Lucia Bravo", "U001")
    biblioteca.registrar_usuario(usuario1)

    biblioteca.prestar_libro("U001", "97886646091")
    print("Libros prestados a Lucia Bravo:", biblioteca.listar_libros_prestados("U001"))

    biblioteca.devolver_libro("U001", "97886646091")
    print("Libros prestados a Lucia Bravo después de devolución:", biblioteca.listar_libros_prestados("U001"))

    usuario2 = Usuario("Diego Vega", "U002")
    biblioteca.registrar_usuario(usuario1)

    biblioteca.prestar_libro("U002", "9788415089155")
    print("Libros prestados a Diego Vega:", biblioteca.listar_libros_prestados("U002"))

    biblioteca.devolver_libro("U002", "9788415089155")
    print("Libros prestados a Diego Vega después de devolución:", biblioteca.listar_libros_prestados("U002"))