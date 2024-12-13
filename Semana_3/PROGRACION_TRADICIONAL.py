#Programa para calculara el promedio semanal de temperatiras
# utilizando progrmación tradicional
# definimos la función
def guardar_temperaturas():

# pedimos al usuario que ingrese las temperaruras diarias de la semana

    temperaturas = []
    print("Ingrese las temperatura diarias de la semana:")
    for dia in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]:
        while True:
            try:
                temperatura = float(input(f"{dia}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Entrada inválida. por favor, ingrese un número.")
    return temperaturas
# Calcular el promedio de la lista de temperaturas
def calcular_promedio(temperaturas):

    return sum(temperaturas)/len(temperaturas)
#funcion principal que organiza el programa
def main():
    temperaturas = guardar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio: .2f}°C")
# EJECUCION DEL PROGRAMA
if __name__ == "__main__":
    main()