def contar_caracteres(archivo_entrada):
    caracteres = {}
    with open(archivo_entrada, "r") as archivo:
        for linea in archivo:
            for caracter in linea.strip():
                if caracter in caracteres:
                    caracteres[caracter] += 1
                else:
                    caracteres[caracter] = 1
    return caracteres

def escribir_conteo(caracteres, archivo_salida):
    with open(archivo_salida, "w") as archivo:
        for caracter, cantidad in caracteres.items():
            archivo.write(f"{caracter} {cantidad}\n")

if __name__ == "__main__":
    archivo_entrada = "random_passwords.txt"
    archivo_salida = "conteo.txt"

    caracteres = contar_caracteres(archivo_entrada)
    escribir_conteo(caracteres, archivo_salida)

    print("El conteo de caracteres se ha guardado en el archivo conteo.txt.")