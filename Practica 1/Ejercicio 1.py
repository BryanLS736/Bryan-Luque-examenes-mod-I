"""Escribimos nuestras variables"""

nombre = 'Bryan'
salario = 200
edad = '18'
compañia = 'Compañia de usuario'

"""Imprimimos sus tipos de variables"""

print("El tipo de variable de 'nombre' es: {}".format(type(nombre)))
print("El tipo de variable de 'salario' es: {}".format(type(salario)))
print("El tipo de variable de 'edad' es: {}".format(type(edad)))
print("El tipo de variable de 'compañia' es: {}".format(type(compañia)))

"""Convertimos la variable edad que es string a int"""

edad_int = int(edad)
print(type(edad_int))
print(edad_int)

"""Realizamos nuestra condicional"""

if edad_int > 30:
    print('Usted tiene un bono de 10% en el mes de diciembre')
    bono_final = (salario**2)+0.10*salario
    print(bono_final)
else:
    print('Usted tiene un bono del 5% en el mes de diciembre')
    bono_final = (salario ** 2) + 0.05 * salario
    print(bono_final)