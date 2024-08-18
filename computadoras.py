class Computadora:
    def __init__(self):
        self.tipo = "Computadora"
        self.marca = input("Ingrese la marca de la computadora: ")
        self.modelo = input("Ingrese el modelo de la computadora: ")
        self.procesador = input("Ingrese el tipo de procesador (e.g., Intel i7, AMD Ryzen 5): ")
        self.ram = input("Ingrese la cantidad de memoria RAM (e.g., 8GB, 16GB): ")
        self.almacenamiento = input("Ingrese la capacidad de almacenamiento (e.g., 512GB SSD, 1TB HDD): ")
        self.tamano_pantalla = input("Ingrese el tamaño de la pantalla (e.g., 15.6 pulgadas): ")
        self.grafica = input("Ingrese el tipo de tarjeta gráfica (e.g., NVIDIA GTX 1660): ")
        self.color = input("Ingrese el color de la computadora: ")
        self.precio_compra = float(input("Ingrese el precio de compra de la computadora: "))
        self.origen = "Importado"
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.6  

    def mostrar_datos(self):
        print("\nCaracterísticas de la computadora:")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Tamaño de Pantalla: {self.tamano_pantalla}")
        print(f"Tarjeta Gráfica: {self.grafica}")
        print(f"Color: {self.color}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

print("Registro de la primera computadora:")
computadora1 = Computadora()
computadora1.mostrar_datos()

print("\nRegistro de la segunda computadora:")
computadora2 = Computadora()
computadora2.mostrar_datos()
