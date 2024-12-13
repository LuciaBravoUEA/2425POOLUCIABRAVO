
class Climadiario:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.__temperatura = temperatura
        # Uso de encapsulamiento

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if isinstance(valor, (int, float)):
            self.__temperatura = valor
        else:
            raise TypeError("La temperatura debe ser un número.")

class Semanaclimatica:
    def __init__(self):
        self.dias_clima = []

    def agregar_dia(self, dia, temperatura):
# Usar los parámetros 'dia' y 'temperatura'
        self.dias_clima.append(Climadiario(dia, temperatura))

    def calcular_promedio(self):
        if not self.dias_clima:
            return 0.0
        total_temperaturas = sum(dia.temperatura for dia in self.dias_clima)
        return total_temperaturas / len(self.dias_clima)

# Función para el programa con los días de la semana
def main():
    semana = Semanaclimatica()
    print("Ingrese las temperaturas diarias de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        while True:
            try:
                temperatura = float(input(f"{dia}: "))
                semana.agregar_dia(dia, temperatura)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    main()