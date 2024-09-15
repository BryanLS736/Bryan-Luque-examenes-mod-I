class Persona:

    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = 'peruana'
        self.edad_1 = self.edad


    def solicitar(self):
        return print(f'El nombre de la persona es: {self.nombre}, y tiene la edad de {self.edad} años')


    def cumple(self):
        self.edad_1 += 1
        return print(f'Feliz cumpleaños, su nueva edad es: {self.edad_1}')


    def aumento_sueldo(self):
        self.saldo = self.saldo + (0.3 * self.saldo)
        return print(f'El nuevo saldo es: {self.saldo}')


    def edad_año(self, año):
        nueva_edad = self.edad + (año - 2024)

        return print(f'En el año {año} tendrá {nueva_edad} años.')

persona_1 = Persona('Bryan', 18, 1200)
persona_1.solicitar()
persona_1.cumple()
persona_1.aumento_sueldo()
persona_1.edad_año(2025)

persona_1 = Persona('Alexander', 22, 2200)
persona_1.solicitar()
persona_1.cumple()
persona_1.aumento_sueldo()
persona_1.edad_año(2026)