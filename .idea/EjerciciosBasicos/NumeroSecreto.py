#Realiza un programa que calcule el número secreto introducido por teclado.

import os

secreto = int(input("Introduzca un numero secreto: "))

print("Intentamos adividar el número secreto...")
numero=0
cont = 1
while(numero != secreto):
    numero=int(input("Introduzca el numero: "))
    if(numero<secreto):
        print("El numero es menor que el secreto...")
        cont+=1
    elif(numero>secreto):
        print("El número es mayor que el secreto...")
        cont+=1
    else:
        print("CORRECTO!!")
        print("Has necesitado %d intentos" % cont)
