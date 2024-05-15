class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.puntero
        return contador

    def insertar_al_principio(self, dato):
        nuevo_nodo = nuevo_nodo(dato)
        nuevo_nodo.puntero = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = nuevo_nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.puntero:
                actual = actual.puntero
            actual.puntero = nuevo_nodo

    def eliminar_elemento(self, dato):
        if self.esta_vacia():
            return False

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.puntero
            return True

        actual = self.cabeza
        while actual.puntero:
            if actual.puntero.dato == dato:
                actual.puntero = actual.puntero.puntero
                return True
            actual = actual.puntero

        return False

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.puntero
        print("None")

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.puntero
        return contador