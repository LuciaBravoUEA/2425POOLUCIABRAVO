# Creamos un programa para convertir de millas a kilómetros, donde el programa coge una distancia en miilas
#para convertirla en kilómetros

#funciones y variables: shake_case ( palabras separadas con guines)

 #Llamamos a la función  para convertir de millas a kilómetros
def millas_a_kilometros(millas):
# millas es un float

     return millas * 160934
def kilometros_a_millas(kilometros):
#kilometros es un float
   return kilometros / 160934

# solicitamos al usuario que ingrese la distancia
opcion = input(
    "¿Deseas convertir millas a kilómetros o kilómetros a millas? (Escribe 'millas' o 'kilometros'): ").strip().lower()

#usamos float para las distancias

if opcion == 'millas':
    distancia = float(input("Ingresa la distancia en millas: "))
    resultado = millas_a_kilometros(distancia)
    print(f"{distancia} millas son equivalentes a {resultado:.2f} kilómetros.")
elif opcion == 'kilometros':
    distancia = float(input("Ingresa la distancia en kilómetros: "))
    resultado = kilometros_a_millas(distancia)
    print(f"{distancia} kilómetros son equivalentes a {resultado:.2f} millas.")
else:
    print("Opción no válida. Por favor, elige 'millas' o 'kilómetros'.")
