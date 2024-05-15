class CuentaBancaria:
    def __init__(self, nombre_cuenta, saldo):
        self.nombre_cuenta = nombre_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente.")

    def obtener_saldo(self):
        return self.saldo

# Ejemplo de uso
cuenta = CuentaBancaria("Cuenta de Ahorros", 1000)
print("Saldo inicial:", cuenta.obtener_saldo())
cuenta.depositar(500)
print("Después de depositar 500:", cuenta.obtener_saldo())
cuenta.retirar(200)
print("Después de retirar 200:", cuenta.obtener_saldo())