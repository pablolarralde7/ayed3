import random
import time

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    
    def busqueda_lineal(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1
    
    def busqueda_binaria(self, valor):
        lista_ordenada = self._convertir_a_lista()
        izquierda = 0
        derecha = len(lista_ordenada) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if lista_ordenada[medio] == valor:
                return medio
            elif lista_ordenada[medio] < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return -1

    def _convertir_a_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.valor)
            actual = actual.siguiente
        return lista

# Generar lista de 1000 números aleatorios
lista = ListaEnlazada()
for _ in range(1000):
    lista.agregar(random.randint(1, 1000))

# Imprimir lista
print("Lista:")
lista.imprimir()

# Realizar búsqueda lineal de un valor aleatorio
valor_busqueda = random.randint(1, 1000)
inicio = time.time()
indice_lineal = lista.busqueda_lineal(valor_busqueda)
tiempo_lineal = time.time() - inicio
print("\nBúsqueda lineal de", valor_busqueda, ":", indice_lineal)
print("Tiempo de ejecución de búsqueda lineal:", tiempo_lineal, "segundos")

# Ordenar la lista para realizar búsqueda binaria
lista.ordenamiento_burbuja()

# Realizar búsqueda binaria de un valor aleatorio
inicio = time.time()
indice_binaria = lista.busqueda_binaria(valor_busqueda)
tiempo_binaria = time.time() - inicio
print("\nBúsqueda binaria de", valor_busqueda, ":", indice_binaria)
print("Tiempo de ejecución de búsqueda binaria:", tiempo_binaria, "segundos")