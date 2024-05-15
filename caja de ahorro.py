class CuentaCorriente(Cuentabancaria):
    def __init__(self, nombre_cuenta, saldo, sobregiro):
        super().__init__(nombre_cuenta, saldo)
        self.sobregiro = sobregiro

    def retirar(self, cantidad):
        if cantidad <= self.saldo + self.sobregiro:
            self.saldo -= cantidad
        else:
            print("Retiro supera límite de sobregiro.")


class CajaDeAhorro(Cuentabancaria):
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Retiro supera saldo disponible.")


# Ejemplo de uso
cuenta_corriente = CuentaCorriente("Cuenta Corriente", 1000, 500)
caja_ahorro = CajaDeAhorro("Caja de Ahorro", 1500)

# Operaciones en cuenta corriente
cuenta_corriente.depositar(500)
cuenta_corriente.retirar(1500)
print("Saldo actual de la cuenta corriente:", cuenta_corriente.obtener_saldo())

# Operaciones en caja de ahorro
caja_ahorro.depositar(1000)
caja_ahorro.retirar(2000)
print("Saldo actual de la caja de ahorro:", caja_ahorro.obtener_saldo())