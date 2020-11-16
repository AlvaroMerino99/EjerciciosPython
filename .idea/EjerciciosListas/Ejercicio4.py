#Escribe un programa que permita crear dos listas de palabras y que, a continuación,
# escriba las siguientes listas (en las que no debe haber repeticiones):
# a. Lista de palabras que aparecen en las dos listas.
# b. Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# c. Lista de palabras que aparecen en la segunda lista, pero no en la primera.

def Lista() :
    numero = int(input("Dígame cuántas palabras tiene la lista: "))
    lista = []
    for i in range(numero) :
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    return lista

lista1=Lista()
lista2=Lista()
#a
print("Lista de palabras que aparecen en las dos listas.")
comunes = []
for i in lista1:
    if i in lista2:
        comunes += [i]
print("Palabras que aparecen en las dos listas:", comunes)

#b
print("Lista de palabras que aparecen en la primera solo.")
soloPrimera = []
for i in lista1:
    if i not in lista2:
        soloPrimera += [i]
print("Palabras que sólo aparecen en la primera lista:", soloPrimera)

#c
print("Lista de palabras que aparecen en la primera solo.")
soloSegunda = []
for i in lista2:
    if i not in lista1:
        soloSegunda += [i]
print("Palabras que sólo aparecen en la segunda lista:", soloSegunda)
