def Lista() :
    numero = int(input("Dígame cuántos elementos tiene la lista: "))
    if numero < 1 :
        print("¡Imposible!")
    else :
        lista = []
        for i in range(numero) :
            print("Dígame el elemento", str(i + 1) + ": ", end="")
            elemento = input()
            lista += [elemento]
    return lista


lista=Lista()
lista1=sorted(lista)
if(lista==lista1):
    print("LA LISTA ESTÁ ORDENADA!!")
else:
    print("LA LISTA NO ESTÁ ORDENADA")