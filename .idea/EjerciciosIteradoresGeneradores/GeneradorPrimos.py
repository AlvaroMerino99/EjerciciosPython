#Implementa un generador primos que genere todos los números primos.
# Por eficiencia, el generador debe ir almacenando los primos encontrados hasta el momento en una lista.
#! /usr/bin/env python

# Función para comprobar si un número es primo
def esPrimo(n):
    if n <= 0:
        return False

    for x in range(2, n):
        if n % x == 0:
            return False
    return True


# Función que nos genera los números primos entre un rango
# que damos por parametro
def generadorPrimos(ini, fin):
    n = ini
    while n <= fin:
        if esPrimo(n):
            yield n
        n += 1


# Metodo que recorre una lista y la imprime
def imprimirLista(lista):
    for i in lista:
        print(i, end=" ")


# Utilizamos el generador para iterar por los números primos:
primos = generadorPrimos(0, 50)
imprimirLista(primos)