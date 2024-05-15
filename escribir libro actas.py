import csv

class Academia:
    def __init__(self):
        self.alumnos = []

    # Otras funciones de la clase Academia...

    def escribir_libro_actas(self, nombre_archivo):
        with open(nombre_archivo, "w", newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(["nombre_materia", "nota_materia", "año_materia", "nombre_alumno", "apellido_alumno", "dni_alumno"])
            
            for alumno in self.alumnos:
                for materia in alumno.materias:
                    escritor.writerow([materia.nombre, materia.nota, alumno.año, alumno.nombre, alumno.apellido, alumno.dni])