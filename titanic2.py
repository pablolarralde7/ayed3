class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, pasajero):
        nuevo_nodo = nuevo_nodo(pasajero)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def ordenamiento_burbuja(self):
        if not self.cabeza:
            return

        cambios = True
        while cambios:
            cambios = False
            actual = self.cabeza
            while actual.siguiente:
                if actual.pasajero.edad > actual.siguiente.pasajero.edad:
                    actual.pasajero, actual.siguiente.pasajero = actual.siguiente.pasajero, actual.pasajero
                    cambios = True
                actual = actual.siguiente

    def busqueda_binaria(self, edad):
        if not self.cabeza:
            return None
        
        # Primero ordenamos la lista enlazada
        self.ordenamiento_burbuja()

        inicio = 0
        fin = self.contar_nodos() - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            actual = self.obtener_nodo_en_posicion(medio)
            if actual.pasajero.edad == edad:
                return actual.pasajero
            elif actual.pasajero.edad < edad:
                inicio = medio + 1
            else:
                fin = medio - 1

        return None

    def obtener_lista_clase(self, clase):
        lista_clase = ListaEnlazada()
        actual = self.cabeza
        while actual:
            if actual.pasajero.Pclass == clase:
                lista_clase.insertar_al_final(actual.pasajero)
            actual = actual.siguiente
        return lista_clase

    def obtener_lista_mayor_edad(self):
        lista_mayores = ListaEnlazada()
        lista_menores = ListaEnlazada()
        actual = self.cabeza
        while actual:
            if actual.pasajero.edad >= 18:
                lista_mayores.insertar_al_final(actual.pasajero)
            else:
                lista_menores.insertar_al_final(actual.pasajero)
            actual = actual.siguiente
        return lista_mayores, lista_menores

    def escribir_totales(self, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Contar sobrevivientes mayores a 18 años
            contador_mayores_sobrevivientes = 0
            contador_menores_sobrevivientes = 0
            contador_clase_1_sobrevivientes = 0
            contador_clase_2_sobrevivientes = 0
            contador_clase_3_sobrevivientes = 0

            actual = self.cabeza
            while actual:
                if actual.pasajero.Survived == '1':
                    if actual.pasajero.edad >= 18:
                        contador_mayores_sobrevivientes += 1
                    else:
                        contador_menores_sobrevivientes += 1
                    if actual.pasajero.Pclass == '1':
                        contador_clase_1_sobrevivientes += 1
                    elif actual.pasajero.Pclass == '2':
                        contador_clase_2_sobrevivientes += 1
                    elif actual.pasajero.Pclass == '3':
                        contador_clase_3_sobrevivientes += 1
                actual = actual.siguiente

            # Contar totales de pasajeros mayores y menores
            contador_mayores_total = self.contar_mayores_edad()
            contador_menores_total = self.contar_nodos() - contador_mayores_total

            # Contar totales por clase
            contador_clase_1_total = self.obtener_lista_clase('1').contar_nodos()
            contador_clase_2_total = self.obtener_lista_clase('2').contar_nodos()
            contador_clase_3_total = self.obtener_lista_clase('3').contar_nodos()

            # Escribir en el archivo CSV
            writer.writerow(['Sobrevivientes mayores a 18 años', contador_mayores_sobrevivientes])
            writer.writerow(['Sobrevivientes menores a 18 años', contador_menores_sobrevivientes])
            writer.writerow(['Sobrevivientes por clase'])
            writer.writerow(['Clase 1', contador_clase_1_sobrevivientes])
            writer.writerow(['Clase 2', contador_clase_2_sobrevivientes])
            writer.writerow(['Clase 3', contador_clase_3_sobrevivientes])
            writer.writerow(['Cantidad total mayores', contador_mayores_total])
            writer.writerow(['Cantidad total menores', contador_menores_total])
            writer.writerow(['Cantidad total por clase'])
            writer.writerow(['Clase 1', contador_clase_1_total])
            writer.writerow(['Clase 2', contador_clase_2_total])
            writer.writerow(['Clase 3', contador_clase_3_total])

    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def contar_mayores_edad(self):
        contador = 0
        actual = self.cabeza
        while actual:
            if actual.pasajero.edad >= 18:
                contador += 1
            actual = actual.siguiente
        return contador

    def obtener_nodo_en_posicion(self, posicion):
        contador = 0
        actual = self.cabeza
        while actual:
            if contador == posicion:
                return actual
            actual = actual.siguiente
            contador += 1
        return None