class Alumno:
    def __init__(self, nombre, apellido, edad, DNI, materias):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.DNI = DNI
        self.materias = materias

    def obtener_promedio_anio(self, anio):
        notas_anio = [materia['nota'] for materia in self.materias if materia['anio'] == anio]
        if notas_anio:
            return sum(notas_anio) / len(notas_anio)
        else:
            return None

    def obtener_promedio_general(self):
        notas = [materia['nota'] for materia in self.materias]
        return sum(notas) / len(notas)

    def mejor_materia(self):
        mejor = max(self.materias, key=lambda x: x['nota'])
        return mejor['nombre']

    def materias_desaprobadas(self, nota_minima):
        desaprobadas = [materia['nombre'] for materia in self.materias if materia['nota'] < nota_minima]
        return desaprobadas

# Ejemplo de uso
materias_juan = [
    {'nombre': 'Matemáticas', 'anio': 2023, 'nota': 8},
    {'nombre': 'Física', 'anio': 2023, 'nota': 7},
    {'nombre': 'Química', 'anio': 2023, 'nota': 5},
    {'nombre': 'Historia', 'anio': 2023, 'nota': 6}
]

juan = Alumno("Juan", "Perez", 18, 12345678, materias_juan)

print("Promedio de Juan en 2023:", juan.obtener_promedio_anio(2023))
print("Promedio general de Juan:", juan.obtener_promedio_general())
print("Mejor materia de Juan:", juan.mejor_materia())
print("Materias desaprobadas de Juan:", juan.materias_desaprobadas(6))