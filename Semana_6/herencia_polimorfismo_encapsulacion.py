#Crear un programa que incluya herencia, polimorfismo y encapsulación.

class Persona:    # herencia
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Encapsulación: atributo protegido
        self._edad = edad      # Encapsulación: atributo protegido

    def descripcion(self):
        return f"{self._nombre} tiene {self._edad} años."

    def actividad(self):
        return "Realiza actividades generales."


class Estudiante(Persona):       # herencia
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def descripcion(self):
        return f"{super().descripcion()} Estudia {self.carrera}."

    def actividad(self):       # Polimorfismo
        return "Estudia y hace tareas."


class Profesor(Persona):   # herencia
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def descripcion(self):
        return f"{super().descripcion()} Enseña {self.materia}."

    def actividad(self):     # Polimorfismo
        return "Da clases y prepara material educativo."


# Creación de instancias
estudiante = Estudiante("Valentina", 25, "Filosofia")
profesor = Profesor("Dra. Maldonado", 47, "Historia")

# Uso de polimorfismo y encapsulación
personas = [estudiante, profesor]

for persona in personas:
    print(persona.descripcion())
    print(f"Actividad: {persona.actividad()}\n")

