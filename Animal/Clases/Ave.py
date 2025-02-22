from Animal import Animal

class Ave(Animal):
    def __init__(self, nombre, peso, año_nacimiento, propietario):
        super().__init__(nombre, peso)
        self.año_nacimiento = año_nacimiento
        self.propietario = propietario

    def calcular_edad(self):
        edad = 2025 - self.año_nacimiento
        if edad >= 5:
            print(f"El ave {self.get_nombre()} es MAYOR DE EDAD.")
        else:
            print(f"El ave {self.get_nombre()} es MENOR DE EDAD.")

    def get_año_nacimiento(self):
        return self.año_nacimiento

    def set_año_nacimiento(self, año_nacimiento):
        self.año_nacimiento = año_nacimiento

    def get_propietario(self):
        return self.propietario

    def set_propietario(self, propietario):
        self.propietario = propietario
