# Clase Automovil
class Automovil:
    def __init__(self, marca="", modelo="",color="", año=0,  precio_compra=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.00

    def recibir_datos(self):
        self.marca = input("Ingrese la marca del automóvil: ")
        self.modelo = input("Ingrese el modelo del automóvil: ")
        self.año = int(input("Ingrese el año del automóvil: "))
        self.color = input("Ingrese el color del automóvil: ")
        self.precio_compra = float(input("Ingrese el precio de compra: "))
        self.precio_venta = self.calcular_precio_venta()

    def mostrar_datos(self):
        print("\nDetalles del automóvil registrado:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Programa principal
def main():
    automovil1 = Automovil()
    automovil1.recibir_datos()
    automovil1.mostrar_datos()

    automovil2 = Automovil()
    automovil2.recibir_datos()
    automovil2.mostrar_datos()

if __name__ == "__main__":
    main()
