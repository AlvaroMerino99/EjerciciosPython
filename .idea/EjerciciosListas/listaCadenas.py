#Dada una lista de cadenas, pide una cadena por teclado e indica si está en la lista,
# indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista,
# y por último borra la cadena de la lista.

def Lista() :
    numero = int(input("Dígame cuántos elementos tiene la lista: "))
    if numero < 1 :
        print("¡Imposible!")
    else :
        lista = []
        for i in range(numero) :
            print("Dígame la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            lista += [palabra]
    return lista


lista=Lista()
buscar = input("Dígame la palabra a buscar: ")
contador = 0
for i in lista:
    if i == buscar:
        contador += 1;
if contador == 0:
    print("La palabra " + buscar + " no está en la lista.")
elif contador == 1:
    print("La palabra " + buscar + " aparece una vez")
else:
    print("La palabra " + buscar + " aparece", contador, "veces")
buscar = input("Sustituir la palabra: ")
sustituir = input("por la palabra: ")
for i in range(len(lista)):
    if lista[i] == buscar:
        lista[i] = sustituir
print("La lista es ahora:", lista)





