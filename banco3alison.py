
import os
import time

class CuentaCorriente:
    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def abonar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def cargar(self, cantidad):
        if cantidad > 0:
            self.saldo = max(self.saldo - cantidad, 0)

    def __str__(self):
        return f"Titular: {self.titular}, Número: {self.numero}, Saldo: {self.saldo:.2f}"

def mostrar_menu():
    os.system("cls")
    print("===MENU BANCO===")
    print("1. Crear nueva cuenta corriente")
    print("2. Consultar saldo")
    print("3. Abonar saldo")
    print("4. Cargar saldo")
    print("5. Salir")

def main():
    cuenta = None

    while True:
        os.system("cls")
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            os.system("cls")
            titular = input("Ingrese el nombre del titular: ")
            numero = int(input("Ingrese el número de cuenta: "))
            saldo = float(input("Ingrese el saldo inicial (opcional, presione enter para omitir): ") or 0.0)
            cuenta = CuentaCorriente(titular, numero, saldo)
            print("Cuenta creada exitosamente.")
        
        elif opcion == 2:
            if cuenta:
                print(cuenta)
                time.sleep(3)
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 3:
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a abonar: "))
                cuenta.abonar(cantidad)
                print(f"Saldo actualizado: {cuenta.saldo}")
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 4:
            if cuenta:
                cantidad = float(input("Ingrese la cantidad a cargar: "))
                cuenta.cargar(cantidad)
                print(f"Saldo actualizado: {cuenta.saldo}")
            else:
                print("Primero debe crear una cuenta.")
        
        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
