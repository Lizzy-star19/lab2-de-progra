# Clase Moto
class Moto:
    def __init__(self):
        self.marca = input("Ingrese la marca de la moto: ")
        self.modelo = input("Ingrese el modelo de la moto: ")
        self.año = input("Ingrese el año de la moto: ")
        self.color = input("Ingrese el color de la moto: ")
        self.tipo_combustible = input("Ingrese el tipo de combustible (Gasolina/Eléctrica): ")
        self.transmision = input("Ingrese el tipo de transmisión (Automática/Manual): ")
        self.motor = input("Ingrese el tipo de motor (e.g., 250cc): ")
        self.origen = input("Ingrese el origen de la moto (Nacional/Importada): ")
        self.precio_compra = float(input("Ingrese el precio de compra de la moto: "))
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 2  # Las motocicletas suelen tener 2 ruedas.
        self.capacidad = 2  # Generalmente, las motocicletas tienen capacidad para 2 personas.

    def calcular_precio_venta(self):
        return self.precio_compra * 1.35  

    def mostrar_datos(self):
        print("\nCaracterísticas de la motocicleta registrada:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Motor: {self.motor}")
        print(f"Origen: {self.origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Programa principal
def main():
    print("Registro de la primera moto:")
    moto1 = Moto()
    moto1.mostrar_datos()

    print("\nRegistro de la segunda moto:")
    moto2 = Moto()
    moto2.mostrar_datos()

if __name__ == "__main__":
    main()
