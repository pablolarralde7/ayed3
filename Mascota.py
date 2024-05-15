class Mascota:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def saludar(self):
        return f"¡Hola! Soy {self.nombre}, de raza {self.raza} y tengo {self.edad} años."

# Ejemplo de uso
mi_mascota = Mascota("Firulais", "Labrador", 3)
print(mi_mascota.saludar())