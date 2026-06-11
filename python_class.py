"""if 5 < 3:
print("5 es menor que 3")
"""

# Comentarios en sola linea y multilinea

'''
print("Hola, todos")
"""Aqui los que estamos aprendiendo los distintos tipos de comentario"""

print("Suerte a todos")
'''

# Administracion de multiples variables, concatenacion

"""
name = "Camilo"
Last_name = " Rincon"
año_nacimiento = 1991
año_actual = 2026

print("mis datos:")
print(
    "Mi nombre es "
    + name
    + Last_name
    + " y tengo "
    + str(año_actual - año_nacimiento)
    + " años"
)

print("Ejemplo de cocatenacion con variables y variables en una sola linea")
nombre, apellido, año_nacimiento = "juan", "palacio", 1950

print(nombre + " " + apellido + " " + str(año_nacimiento))

"""

# Tipos de Datos

"""

comillasSimples = "Hola, soy un texto entre comillas simples"
comillasDobles = "Hola, soy un texto entre comillas dobles"
comillasSimplesDobles = 'Hola, soy un texto entre comillas simples y "comillas dobles"'

print(
    "imprimiendo los tipos de comillas aceptables en python"
    + "\n"
    + comillasSimples
    + "\n"
    + comillasDobles
    + "\n"
    + comillasSimplesDobles
)
"""

# Tipos de datos numericos

""" 
print("tipos de datos: Enteros, flotantes, complejos")

print("Enteros")
entero = 10
print(
    "El tipo de dato del numero entero es: "
    + str(entero)
    + " "
    + "y el tipo de dato es:"
    + str(type(entero))
)


print("flotantes")
float = 3.14
print(
    "El tipo de dato del numero flotante es: "
    + str(float)
    + " y el tipo de dato es: "
    + str(type(float))
)

print("complejos - complex")
complejo = 2 + 3j
print(
    "el tipo de dato del numero es: "
    + str(complejo)
    + " y el tipo de dato es: "
    + str(type(complejo))
)
"""

# listas

"""
print(
    "listas"
    + "\n"
    + "las listas son un tipo de dato que permite almacenar una coleccion de elementos ordenados y mutables"
)

lista1 = [1, 2, 3, 4, 5]
print(lista1)

tuplas = (1, 2, 3, 4, 5)

print(
    "tuplas"
    + "\n"
    + "las tuplas son un tipo de dato que permite almacenar una coleccion de elementos ordenados e inmutables"
)
print(tuplas)
"""

# diccionarios
"""
print(
    "diccionarios"
    + "\n"
    + "los diccionarios son un tipo de dato que permite almacenar una coleccion de elementos no ordenados, mutables y indexados por claves"
)
diccionario = {"nombre": "camilo", "apellido": "rincon", "edad": 35}
print(diccionario)
"""

# conjuntos

"""
print(
    "conjuntos"
    + "\n"
    + "los conjuntos son un tipo de dato que permite almacenar una coleccion de elementos no ordenados, mutables y sin elementos duplicados"
)
print("conjunto de numeros")
conjunto_numeros = {1, 2, 3, 4, 5}
print(conjunto_numeros)
print("conjunto de palabras")
conjunto_palabras = {"hola", "mundo", "python"}
print(conjunto_palabras)
"""

# booleanos
"""
print("booleanos")
esto_es_verdadero = True
esto_es_falso = False

print("el valor de esto_es_verdadero es: " + str(esto_es_verdadero))
print("el valor de esto_es_falso es: " + str(esto_es_falso))
"""

# numeros (enteros, flotantes, complejos) y su tipo de dato

"""
x = 10
y = 3.14
z = 2 + 3j
print(x)
print(y)
print(z)
print(str(type(x)))
print(str(type(y)))
print(str(type(z)))

print("casteo de numeros")

xf = float(x)
ye = int(y)
#zf = float(z) no se puede convertir un numero complejo a un numero flotante o entero, por lo tanto se genera un error
print(xf)
print(ye)

print(str(type(xf)))
print(str(type(ye)))

"""

# numero aleatorios
"""

import random

print("numeros aleatorios")
numero_aleatorio = random.randrange(1, 10)
print("el numero aleatorio generado es: " + str(numero_aleatorio))

"""

# disferentes tipos de texto
"""
texto = "este es un texto"

print(texto)
texto_mayuscula = texto.upper()
print(" se convierte a mayusculas: " + texto_mayuscula)

"""

# texto (conociendo cantidad de caracteres)

"""
texto2 = "hipopotamo"
print(texto2)
cantidad = len(texto2)
print("la palabra " + texto2 + " tiene " + str(cantidad) + " letras")

print("Para reemplazar una letra por otra o una palabra se debe usar REPLACE")

texto3 = "el perro es el mejor amigo del hombre"
texto3_reemplazado = texto3.replace("perro", "gato")
print(texto3)
print(texto3_reemplazado)
"""

# Dato None
"""
print("Dato None")
dato_none = None
print(dato_none)
print("el tipo de dato de dato_none es: " + str(type(dato_none)))
"""

# Operadores matematicos

"""
x = 10
y = 5

suma = x + y  # suma los resultado
print("la suma es: ", suma)

resta = x - y  # resta de los resultados
print("la resta es: ", resta)

multiplicacion = x * y
print("La multiplicacion es: ", multiplicacion)

division = (
    y / x
)  # siempre da numero flotante aunque el resultado sea un numero entero, para obtener un numero entero se debe usar la division entera (//)
print(" La division es ", division)

division_entera = y // x
print(
    "la division entera es: ", division_entera
)  # da como resultado un numero entero, redondeando hacia abajo

modulo = y % x  # da como resultado el residuo de la division
print("el modulo es: ", modulo)

exponente = x**y  # que hace? eleva el valor de x a la potencia de y
print("el exponente es: ", exponente)

# como usar el residuo de la division para saber si un numero es par o impar

par = 9

if par % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")
"""

# Operadores de asignacion
"""
x = 10

x += 5  # es lo mismo que x = x + 5, es decir, suma el valor de x con 5 y asigna el resultado a x
print(x)
x -= 5  # es lo mismo que x = x - 5, es decir, resta el valor de x con 5 y asigna el resultado a x
print(x)
x *= 2
print(x)
x /= 2  # recordar que la division siempre da como resultado un numero flotante, aunque el resultado sea un numero entero
print(x)
x //= 2
print(x)
"""

# Operadores de comparacion
"""como saber si un numero es igual o distinto a otro?"""
"""

x = 10
y = 5
print(
    x == y
)  # el operador de comparacion de igualdad, devuelve True si los valores son iguales, de lo contrario devuelve False
print(x != y)  # el operador de comparacion de desigualdad, devuelve True si
print(x < y)  # el operador de comparacion es menor que. Retorna false
print(x > y)  # Como el operador de comparacion es mayor que. Retorna TRUE
print(x <= y)
print(x >= y)
"""

# Operadores logicos
"""
x = 5
y = 10

print(x < y and y > 0)  # si son verdaderas, ambos es true, de lo contrario es false
print(x < y or y > 0)  # si una de las 2 se cumple es true, sino, es false
print(
    not (x < y)
)  # si la condicion es true, devuelve false, y si la condicion es false, devuelve true

"""

# Condicionales if, elif, else
"""
if 5 > 3:
    print("5 es mayor que 3")
else:
    print("5 es menor que 3")

x = 2
y = 4
z = 5

if x > y and x > z:
    print("x es el numero mayor")
elif y > x and y > z:
    print("y es el numero mayor")
else:
    print("z es el numero mayor")
"""

# ejercicio: Escribir un programa que solicite al usuario ingresar un número y determine si es par o impar.
"""
dato = input(print("ingresa el numero a evaluar: "))
print("el numero ingresado es: ", dato)

if int(dato) % 2 == 0:
    print("el numero es par")
else:
    print("el numeor es impar")

"""

# Ejercicio 2: Escribir un programa que solicite al usuario ingresar su edad y determine si es mayor de edad o menor de edad.
"""
edad = input("Ingresa tu edad: ")
edad_maxima = 18

print(edad + " Años")
if int(edad) >= edad_maxima:
    print("Felicidades! Eres mayor de edad")
else:
    print("Lo siento, aun eres menor de edad")
"""

# Ejercicio 3: Escribir un programa que solicite al usuario ingresar un número y determine si es positivo, negativo o cero.
"""
numero = input("Ingresar número a evaluar: ")
print("El numero ingresado es: ", numero)

if int(numero) < -1:
    print("El numero es negativo")
elif int(numero) > 1:
    print("El numero es positivo")
else:
    print("El numero es 0")
"""

# Ejercicio 4: Escribir un programa que solicite al usuario ingresar su nombre y edad, y luego imprima un mensaje
# personalizado que incluya su nombre y si es mayor o menor de edad.
"""
nombre = input("Ingresa tu nombre: ")
edad = input("ingresa tu edad: ")
edad_maxima = 18

if int(edad) >= edad_maxima:
    print(" El usuario ", nombre, " tiene ", int(edad), " años y es mayor de edad")
else:
    print("El usuario ", nombre, " tiene", int(edad), " años y es menor de edad")
"""

# Ejercicio 5: Escribir un programa que solicite al usuario ingresar un número y determine si es divisible por 3, por 5 o por ambos.

"""
valor = input("ingresa un valor a evaluar: ")
n = int(valor)

if n % 3 == 0 and n % 5 == 0:
    print("Ambos numeros son divisibles entre: ", n)
elif n % 3 == 0:
    print("El numero es divisible entre 3")
elif n % 5 == 0:
    print("El numero es divisible entre 5")
else:
    print("El numero no es divisible")
"""

# Ejercicio 6: Escribir un programa que solicite al usuario ingresar su calificación y determine si aprobó o reprobó,
#  considerando que la calificación mínima para aprobar es 60.
"""
nota = int(input("Ingresar nota estudiante: "))
nota_minima = 60

if nota >= nota_minima:
    print("El estudiante APROBÓ")
else:
    print(" El estudiante REPROBÓ")
"""

# Ejercicio 7: Escribir un programa que solicite al usuario ingresar un número y determine si es un número primo o no.

dato = int(input("ingresa numero a evaluar: "))
es_primo = True

if dato <= 1:
    print("El numero ingresado no es válido")
else:
    for i in range(2, dato):
        if dato % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"El numero ingresado es: {dato} y es primo")
    else:
        print(f"El numero ingresado es: {dato} y no es primo")
# Ejercicio 8: Escribir un programa que solicite al usuario ingresar su salario y determine si es elegible para recibir un aumento, considerando que el salario mínimo para ser elegible es de $1000.
# Ejercicio 9: Escribir un programa que solicite al usuario ingresar un número y determine si es un número perfecto o no, considerando que un número perfecto es aquel que es igual a la suma de sus divisores propios.
# Ejercicio 10: Escribir un programa que solicite al usuario ingresar su año de nacimiento y determine su signo zodiacal, considerando las fechas correspondientes a cada signo.
# Tu nuevo mini-reto Emistreaming: Escribe un bucle for que recorra una lista con los nombres de tus productos (["Netflix", "Max", "Disney+"]) e imprima un mensaje para cada uno (Ej: "Cargando inventario de: Netflix").
