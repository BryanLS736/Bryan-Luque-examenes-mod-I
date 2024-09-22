import datetime


def funcion_decoradora(funcion):

    def funcion_dec(*args):
        resultado = funcion(*args)
        if len(args) > 1:
            print(f'La cantidad de argumentos es: {len(args)}')
        else:
            print('El total de argumentos debe ser mayor a 1.')
        print(resultado)

    return funcion_dec


@funcion_decoradora
def capturar(nombre, edad):
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    return (f'La función "capturar" fue ejecutada con éxito.'
            f'Bienvenido {nombre}, usted tiene {edad} años y'
            f' son las {hora} horas con {minuto} minutos')


@funcion_decoradora
def notas(nota1, nota2, nota3, nota4):
    media = float(nota1 + nota2 + nota3 + nota4)/4
    return (f'La funcion "notas" fue ejecutada con éxito,'
            f'la media de las notas es: {media}')


capturar('Bryan', 18)
notas(18, 14, 11, 8)
