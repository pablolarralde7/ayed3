import random
import string
import sys

def generar_password():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(16))

def generar_passwords(cantidad):
    with open("random_passwords.txt", "w") as archivo:
        for _ in range(cantidad):
            password = generar_password()
            archivo.write(password + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <cantidad>")
        sys.exit(1)

    try:
        cantidad = int(sys.argv[1])
    except ValueError:
        print("El argumento debe ser un número entero.")
        sys.exit(1)

    generar_passwords(cantidad)
    print(f"Se han generado {cantidad} contraseñas en el archivo random_passwords.txt.")