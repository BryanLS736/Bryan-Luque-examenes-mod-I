def funcion_decoradora(funcion):
    def funcion_dec(*args):
        suma = 0
        for i in args:
            suma += i
        print(f'La suma de tus argumentos es: {suma}')
        resultado = funcion(*args)
        print(f'El numero mayor de tus argumentos es: {resultado}')
    return funcion_dec


@funcion_decoradora
def numeros(*args):
    mayor = max(args)
    return mayor


numeros(8, 14, 18, 4, 5)
