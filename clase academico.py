class Academico:
    def __init__(self, nombre_institucion, alumnos):
        self.nombre_institucion = nombre_institucion
        self.alumnos = alumnos

    def promedio_general(self):
        total_notas = 0
        total_materias = 0
        for alumno in self.alumnos:
            for materia in alumno.materias:
                total_notas += materia['nota']
                total_materias += 1
        if total_materias > 0:
            return total_notas / total_materias
        else:
            return None

    def alumnos_graduados(self):
        graduados = []
        for alumno in self.alumnos:
            if all(materia['nota'] >= 6 for materia in alumno.materias):
                graduados.append(alumno)
        return graduados

# Ejemplo de uso
alumno1 = alumno("Juan", "Perez", 18, 12345678, [
    {'nombre': 'Matemáticas', 'nota': 8},
    {'nombre': 'Física', 'nota': 7},
    {'nombre': 'Química', 'nota': 5}
])
alumno2 = alumno1("María", "González", 19, 98765432, [
    {'nombre': 'Matemáticas', 'nota': 7},
    {'nombre': 'Física', 'nota': 6},
    {'nombre': 'Química', 'nota': 6}
])

academia = Academico("Universidad XYZ", [alumno1, alumno2])

print("Promedio general de la institución:", academia.promedio_general())
print("Alumnos graduados:")
for alumno in academia.alumnos_graduados():
    print(f"{alumno.nombre} {alumno.apellido}")