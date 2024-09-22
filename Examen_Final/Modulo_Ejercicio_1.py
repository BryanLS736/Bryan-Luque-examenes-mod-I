import random


def numeros_aleatorios():
    lista = []
    for i in range(1, 11):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista


def numeros_no_repetidos(lista):

    # Lo convierto a conjunto ya que estos no pueden almacenar datos repetidos,
    # para luego convertilo a una lista nuevamente.

    return list(set(lista))


def orden(lista):
    lista.sort()
    lista_invertida = lista[::-1]
    return (f'La lista de menor a mayor es: {lista}, '
            f'la lista de mayor a menor es: {lista_invertida}')


def par_mayor(lista):
    lista_prueba = lista
    mayor_par = max(lista)

    while mayor_par % 2 == 1:
        lista_prueba.remove(mayor_par)
        mayor_par = max(lista)

    return f'El numero mayor par de la lista es: {mayor_par}'
