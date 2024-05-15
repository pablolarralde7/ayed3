from datetime import datetime

def tiempo_para_proximo_cumpleaños(fecha_nacimiento):
    # Obtener la fecha actual
    hoy = datetime.now()

    # Convertir la cadena de fecha de nacimiento en un objeto datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')

    # Calcular el próximo cumpleaños
    proximo_cumpleaños = datetime(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)
    if proximo_cumpleaños < hoy:
        proximo_cumpleaños = datetime(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

    # Calcular la diferencia de tiempo entre hoy y el próximo cumpleaños
    tiempo_restante = proximo_cumpleaños - hoy

    # Imprimir el tiempo restante para el próximo cumpleaños
    print("Falta {} días, {} horas, {} minutos y {} segundos para tu próximo cumpleaños.".format(
        tiempo_restante.days,
        tiempo_restante.seconds // 3600,
        (tiempo_restante.seconds % 3600) // 60,
        tiempo_restante.seconds % 60
    ))


# Solicitar al usuario la fecha de nacimiento
fecha_nacimiento_usuario = input("Ingrese su fecha de cumpleaños (dd/mm/aaaa): ")

# Calcular y mostrar el tiempo restante para el próximo cumpleaños
tiempo_para_proximo_cumpleaños(fecha_nacimiento_usuario)