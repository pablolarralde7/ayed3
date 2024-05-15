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

lista = ListaEnlazada()
lista.agregar(5)
lista.agregar(3)
lista.agregar(8)
lista.agregar(1)
lista.imprimir()  # Imprime: 5 -> 3 -> 8 -> 1 -> None

lista.ordenamiento_burbuja()
lista.imprimir()  # Imprime: 1 -> 3 -> 5 -> 8 -> None

lista.ordenamiento_por_seleccion()
lista.imprimir()  # Imprime: 1 -> 3 -> 5 -> 8 -> None

lista.ordenamiento_por_insercion()
lista.imprimir()  # Imprime: 1 -> 3 -> 5 -> 8 -> None