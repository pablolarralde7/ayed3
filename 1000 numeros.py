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
    
    def ordenamiento_burbuja(self):
        if not self.cabeza:
            return
        
        cambios = True
        while cambios:
            cambios = False
            actual = self.cabeza
            while actual.siguiente:
                if actual.valor > actual.siguiente.valor:
                    actual.valor, actual.siguiente.valor = actual.siguiente.valor, actual.valor
                    cambios = True
                actual = actual.siguiente
    
    def ordenamiento_por_seleccion(self):
        if not self.cabeza:
            return
        
        actual = self.cabeza
        while actual:
            minimo = actual
            siguiente = actual.siguiente
            while siguiente:
                if siguiente.valor < minimo.valor:
                    minimo = siguiente
                siguiente = siguiente.siguiente
            actual.valor, minimo.valor = minimo.valor, actual.valor
            actual = actual.siguiente
    
    def ordenamiento_por_insercion(self):
        if not self.cabeza:
            return
        
        actual = self.cabeza.siguiente
        while actual:
            valor_actual = actual.valor
            anterior = actual
            while anterior.valor > anterior.siguiente.valor and anterior != self.cabeza:
                anterior.valor = anterior.siguiente.valor
                anterior.siguiente.valor = valor_actual
                anterior = anterior.siguiente
            actual = actual.siguiente

# Generar lista de 1000 números aleatorios
lista = ListaEnlazada()
for _ in range(1000):
    lista.agregar(random.randint(1, 1000))

# Imprimir lista sin ordenar
print("Lista sin ordenar:")
lista.imprimir()

# Ordenar la lista utilizando burbuja y medir el tiempo de ejecución
inicio = time.time()
lista.ordenamiento_burbuja()
tiempo_burbuja = time.time() - inicio
print("\nLista ordenada con ordenamiento burbuja:")
lista.imprimir()
print("Tiempo de ejecución de ordenamiento burbuja:", tiempo_burbuja, "segundos")

# Ordenar la lista utilizando selección y medir el tiempo de ejecución
inicio = time.time()
lista.ordenamiento_por_seleccion()
tiempo_seleccion = time.time() - inicio
print("\nLista ordenada con ordenamiento por selección:")
lista.imprimir()
print("Tiempo de ejecución de ordenamiento por selección:", tiempo_seleccion, "segundos")

# Ordenar la lista utilizando inserción y medir el tiempo de ejecución
inicio = time.time()
lista.ordenamiento_por_insercion()
tiempo_insercion = time.time() - inicio
print("\nLista ordenada con ordenamiento por inserción:")
lista.imprimir()
print("Tiempo de ejecución de ordenamiento por inserción:", tiempo_insercion, "segundos")