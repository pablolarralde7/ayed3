
class Materia:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def esta_aprobada(self):
        return self.nota >= 6



from materia import Materia

class Alumno:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def materias_aprobadas(self):
        return all(materia.esta_aprobada() for materia in self.materias)



from alumno import Alumno

class Academia:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def cantidad_alumnos_aprobados_por_año(self, año):
        return sum(1 for alumno in self.alumnos if alumno.año == año and alumno.materias_aprobadas())

    def alumnos_egresados(self):
        return [alumno for alumno in self.alumnos if alumno.materias_aprobadas()]



from alumno import Alumno
from academia import Academia
from materia import Materia


materia1 = Materia("Matemáticas", 8)
materia2 = Materia("Historia", 7)
materia3 = Materia("Física", 5)

alumno1 = Alumno("Juan", 2020)
alumno1.agregar_materia(materia1)
alumno1.agregar_materia(materia2)
alumno1.agregar_materia(materia3)

alumno2 = Alumno("María", 2020)
alumno2.agregar_materia(materia1)
alumno2.agregar_materia(materia2)

alumno3 = Alumno("Pedro", 2021)
alumno3.agregar_materia(materia1)
alumno3.agregar_materia(materia2)
alumno3.agregar_materia(materia3)

academia = Academia()
academia.agregar_alumno(alumno1)
academia.agregar_alumno(alumno2)
academia.agregar_alumno(alumno3)

print("Cantidad de alumnos aprobados en 2020:", academia.cantidad_alumnos_aprobados_por_año(2020))
print("Alumnos egresados:", [alumno.nombre for alumno in academia.alumnos_egresados()])