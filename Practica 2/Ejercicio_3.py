class BilleteraElectronica:
    def __init(self, nombre, apellido, cuenta_soles, cuenta_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta_soles = cuenta_soles
        self.cuenta_dolares = cuenta_dolares


    def transferir(self, moneda_usar):

        if moneda_usar.lower == 'soles':
            """Pasando de dolares a soles"""
            cuenta_dolares = self.cuenta_dolares * 0.27

        return print(cuenta_dolares)


    def retirar(self, monto_retirar):
        if monto_retirar > self.cuenta_dolares and monto_retirar > self.cuenta_soles:
            print('No tiene fondos suficientes para el retiro.')
        else:
            self.cuenta_soles = self.cuenta_soles - monto_retirar
            self.cuenta_dolares = self.cuenta_dolares - monto_retirar


persona_1 = BilleteraElectronica()
