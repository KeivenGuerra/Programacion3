class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso
