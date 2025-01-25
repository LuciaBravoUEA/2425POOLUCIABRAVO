#Creación de un objeto
class Lápiz:
    #Metodo Constructor
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El método decontructor se ha ejecutadocon éxito")

    def datos(self):
        print(f"tu esfero es marca {self.marca} y color: {self.color}")

    #Metodo Destructor
    def __del__(self):
        print("El método destructor se ha ejecutado")

class Esfero:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("Método de la clse Esfero iniciado")

    def datos(self):
        print(f"tu Esfero es marca {self.marca} y color {self.color}")

    def __del__(self):
        print("El método destructor de la clase Esfero se ha ejecutado")
lápiz_de_Lucy = Lápiz("Staedtler", "Rojo")
esfero_de_Lucy = Esfero("Big", "Azul")


lápiz_de_Lucy.datos()
esfero_de_Lucy.datos()

