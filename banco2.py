class CuentaCorriente:
    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    # Métodos get/set para los atributos
    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"Titular: {self.titular}, Número: {self.numero}, Saldo: {self.saldo:.2f}"

    # Método para abonar al saldo
    def abonar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    # Método para cargar al saldo
    def cargar(self, cantidad):
        if cantidad > 0:
            self.saldo = max(self.saldo - cantidad, 0)

def menu():
    print("1. Crear nueva cuenta corriente")
    print("2. Consultar saldo")
    print("3. Abonar saldo")
    print("4. Cargar saldo")
    print("5. Cambiar titular")
    print("6. Cambiar número de cuenta")
    print("7. Salir")
    return int(input("Seleccione una opción: "))

def main():
    cuenta = None

    while True:
        opcion = menu()

        if opcion == 1:
            titular = input("Ingrese el nombre del titular: ")
            numero = int(input("Ingrese el número de cuenta: "))
            saldo = input("Ingrese el saldo inicial (opcional, presione enter para omitir): ")
            saldo = float(saldo) if saldo else 0.0
            cuenta = CuentaCorriente(titular, numero, saldo)
            print("Cuenta creada exitosamente.")
        
        elif opcion == 2:
            if cuenta:
                print(cuenta)
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 3:
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a abonar: "))
                cuenta.abonar(cantidad)
                print(f"Saldo actualizado: {cuenta.get_saldo()}")
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 4:
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a cargar: "))
                cuenta.cargar(cantidad)
                print(f"Saldo actualizado: {cuenta.get_saldo()}")
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 5:
            if cuenta:
                nuevo_titular = input("Ingrese el nuevo nombre del titular: ")
                cuenta.set_titular(nuevo_titular)
                print(f"Titular actualizado: {cuenta.get_titular()}")
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 6:
            if cuenta:
                nuevo_numero = int(input("Ingrese el nuevo número de cuenta: "))
                cuenta.set_numero(nuevo_numero)
                print(f"Número de cuenta actualizado: {cuenta.get_numero()}")
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
