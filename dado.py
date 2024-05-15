import random

class Dado:
    def __init__(self):
        self.ultimo_valor = None
        self.resultados = []

    def arrojar_dado(self):
        # Generar un número aleatorio del 1 al 6
        numero = random.randint(1, 6)
        
        # Guardar el último valor obtenido y agregarlo a la lista de resultados
        self.ultimo_valor = numero
        self.resultados.append(numero)
        
        # Retornar el número aleatorio generado
        return numero

    def obtener_ultimo_valor(self):
        return self.ultimo_valor

    def obtener_resultados(self):
        return self.resultados


# Ejemplo de uso
dado = Dado()

# Arrojar el dado varias veces y mostrar los resultados
for _ in range(5):
    resultado = dado.arrojar_dado()
    print("Resultado del lanzamiento:", resultado)

# Mostrar el último valor obtenido y todos los resultados
print("Último valor obtenido:", dado.obtener_ultimo_valor())
print("Todos los resultados obtenidos:", dado.obtener_resultados())