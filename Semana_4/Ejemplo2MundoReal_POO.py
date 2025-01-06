# Creación de un sistema para reservar un boleto de avión
class Pasajero:
    def __init__(self, id_pasajero, nombre, documento):
        self.id_pasajero = id_pasajero
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return f"Pasajero {self.nombre} (ID: {self.id_pasajero}, documento: {self.documento})"


class Vuelo:
    def __init__(self, id_vuelo, origen, destino, capacidad):
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad
        self.reservas = []

    def __str__(self):
        return f"Vuelo {self.id_vuelo} Origen: {self.origen}, Destino: {self.destino}, Asientos disponibles: {self.asientos_disponibles}/{self.capacidad}"

    def reservar_asiento(self, pasajero):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            self.reservas.append(pasajero)
            print(f"Asiento reservado con éxito para {pasajero.nombre} en el vuelo {self.id_vuelo}.")
        else:
            print("No hay asientos disponibles en este vuelo.")

    def cancelar_reserva(self, id_pasajero):
        for pasajero in self.reservas:
            if pasajero.id_pasajero == id_pasajero:
                self.reservas.remove(pasajero)
                self.asientos_disponibles += 1
                print(f"Reserva cancelada para {pasajero.nombre} en el vuelo {self.id_vuelo}.")
                return
        print(f"No se encontró ninguna reserva con ID de pasajero: {id_pasajero}.")

    def mostrar_reservas(self):
        if self.reservas:
            print(f"Reservas para el vuelo {self.id_vuelo}:")
            for pasajero in self.reservas:
                print(pasajero)
        else:
            print(f"No hay reservas para el vuelo {self.id_vuelo}.")


class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def mostrar_vuelos(self):
        print("Vuelos disponibles:")
        for vuelo in self.vuelos:
            print(vuelo)

    def buscar_vuelo(self, id_vuelo):
        for vuelo in self.vuelos:
            if vuelo.id_vuelo == id_vuelo:
                return vuelo
        return None


if __name__ == "__main__":
    # Crear la aerolínea
    aerolinea = Aerolinea("Aerolínea Bianca")

    # Agregar vuelos
    vuelo1 = Vuelo(102, "Ciudad México", "Ciudad Cancún", 5)
    vuelo2 = Vuelo(103, "Ciudad Chicago", "Ciudad Miami", 3)
    aerolinea.agregar_vuelo(vuelo1)
    aerolinea.agregar_vuelo(vuelo2)

    # Mostrar vuelos disponibles
    aerolinea.mostrar_vuelos()

    # Crear pasajeros
    pasajero1 = Pasajero(1, "Adrian Torres", "175237364-7")
    pasajero2 = Pasajero(3, "Jose Luis Velasco", "171323438-1")

    # Reservar asientos
    vuelo = aerolinea.buscar_vuelo(103)
    if vuelo:
        vuelo.reservar_asiento(pasajero1)
        vuelo.reservar_asiento(pasajero2)

    # Mostrar reservas del vuelo
    vuelo.mostrar_reservas()

    # Cancelar una reserva
    vuelo.cancelar_reserva(1)

    # Mostrar reservas después de la cancelación
    vuelo.mostrar_reservas()

    # Mostrar vuelos disponibles después de las reservas
    aerolinea.mostrar_vuelos()





