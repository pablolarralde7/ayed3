class Calculadora:
    def __init__(self):
        self.num1 = int(input("Introduce el primer número entero: "))
        self.num2 = int(input("Introduce el segundo número entero: "))

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre cero."

# Crear un objeto de la clase Calculadora
mi_calculadora = Calculadora()

# Calcular y mostrar los resultados
print("La suma es:", mi_calculadora.suma())
print("La resta es:", mi_calculadora.resta())
print("La multiplicación es:", mi_calculadora.multiplicacion())
print("La división es:", mi_calculadora.division())