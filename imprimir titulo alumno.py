import csv

class Academia:
    def __init__(self):
        self.alumnos = []

    # Otras funciones de la clase Academia...

    def imprimir_titulo_alumno(self, dni_alumno):
        # Buscar el alumno por su DNI
        alumno = next((alumno for alumno in self.alumnos if alumno.dni == dni_alumno), None)
        if alumno is None:
            print("No se encontró al alumno con ese DNI.")
            return

        # Verificar si el alumno ha egresado
        if not alumno.materias_aprobadas():
            print("El alumno no ha egresado aún.")
            return

        # Crear el archivo de título para el alumno
        nombre_archivo = f"titulo_{dni_alumno}.txt"
        with open(nombre_archivo, "w") as archivo_titulo:
            archivo_titulo.write(f"Felicidades {alumno.nombre} {alumno.apellido} aprobaste todas las materias!\n\n")
            
            # Leer el archivo libro_actas.csv
            try:
                with open("libro_actas.csv", "r") as archivo_csv:
                    lector = csv.DictReader(archivo_csv)
                    materias_alumno = [materia for materia in lector if materia['dni_alumno'] == dni_alumno]
                    # Ordenar las materias por año de menor a mayor
                    materias_alumno.sort(key=lambda x: int(x['año_materia']))

                    # Escribir las materias en el archivo de título
                    for materia in materias_alumno:
                        archivo_titulo.write(f"{materia['año_materia']} - {materia['nombre_materia']} - {materia['nota_materia']}\n")
            except FileNotFoundError:
                print("No se encontró el archivo libro_actas.csv.")

        print(f"El título del alumno ha sido generado y guardado en {nombre_archivo}.")

# Suponiendo que las clases Materia y Alumno están definidas previamente