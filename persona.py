class persona:
    def __init__(self, nombre, edad):              
        self.nombre = nombre
        self.edad = edad 
    def getNombre (self):
        return self.Nombre
    #def setNombre(self):

    
    def getEdad (self):
        return self.edad
    
    def mostrar_datos(self):
        print(f"{self.nombre} tiene {self.edad} años de edad")
    
    def es_mayor(self):
        return self.edad <= 18

persona1= persona("Pablo",28)
persona1.mostrar_datos()
persona2 = persona("Vero",500)
persona2.mostrar_datos()
persona3 = persona("leo", 25)
persona3.mostrar_datos()