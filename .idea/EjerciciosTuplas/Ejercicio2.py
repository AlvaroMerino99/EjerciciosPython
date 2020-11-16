#Escribe dos funciones que dadas dos cadenas de caracteres:
#a. Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
#cadena es una subcadena de subcadena.
#b. Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe kde y
#gnome, debe devolver gnome.

cadena1=input("Cadena 1:")
cadena2=input("Cadena 2:")

if cadena1.find(cadena2)!=-1:
    print("cadena2 es subcadena de cadena1")
else:
    print("cadena2 no es subcadena de cadena1")

if cadena1<cadena2:
    print(cadena1)
else:
    print(cadena2)