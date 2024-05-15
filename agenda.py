class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        self.contactos.append(contacto)
        print("Contacto añadido con éxito.")

    def lista_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
        else:
            print("La agenda está vacía.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                contacto['telefono'] = nuevo_telefono
                contacto['email'] = nuevo_email
                print("Contacto editado correctamente.")
                return
        print("Contacto no encontrado.")

    def mostrar_menu(self):
        while True:
            print("\nMenú de la Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el teléfono del contacto: ")
                email = input("Ingrese el email del contacto: ")
                self.añadir_contacto(nombre, telefono, email)
            elif opcion == '2':
                self.lista_contactos()
            elif opcion == '3':
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Ingrese el nombre del contacto a editar: ")
                nuevo_telefono = input("Ingrese el nuevo teléfono del contacto: ")
                nuevo_email = input("Ingrese el nuevo email del contacto: ")
                self.editar_contacto(nombre, nuevo_telefono, nuevo_email)
            elif opcion == '5':
                print("Cerrando la agenda.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejemplo de uso
mi_agenda = Agenda()
mi_agenda.mostrar_menu()