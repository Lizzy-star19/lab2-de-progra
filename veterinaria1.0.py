class Veterinaria:
    def _init_(self, peso=0, nombre="", clase="", color="", edad=0, genero=""):
        self.Estado = "NO ATENDIDO"
        self.peso = peso
        self.tamaño = self.determinar_tamaño()
        self.Nombre = nombre
        self.Clase = clase  
        self.Color = color
        self.Edad = edad
        self.Género = genero 



    def determinar_tamaño(self):
        if self.peso <= 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def cambiar_estado(self):
        self.Estado = "DATOS ATENDIDOS"
        return self.Estado

    def entrada_datos(self):
        self.Nombre = input("Nombre del Perro: ")
        self.Clase = input("Ingrese qué raza es su mascota: ")
        self.Color = input("Ingrese el color de su mascota: ")
        self.Edad = input("Ingrese la edad de su mascota: ")
        self.peso = input("Ingrese el peso de su mascota en kg: ")
        self.Género = input("Ingrese el género de su mascota: ")
        self.tamaño = input("Determinar tamaño: ")  
    def muestra_datos(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Raza: {self.Clase}")
        print(f"Color: {self.Color}")
        print(f"Edad: {self.Edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamaño}")
        print(f"Género: {self.Género}")
        print(f"Estado: {self.Estado}")

perro = Veterinaria()  # Se puede crear la instancia sin valores iniciales
perro.entrada_datos()  # Se piden los datos al usuario
perro.cambiar_estado()  # Cambia el estado a "ATENDIDO"
perro.muestra_datos()  # Muestra todos los datos del perro