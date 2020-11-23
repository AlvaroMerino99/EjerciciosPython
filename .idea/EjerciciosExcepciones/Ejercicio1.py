# Realiza la función agregar_una_vez(lista,el) que reciba una lista y un elemento. la funcion debe
#añadir el elemento al final con la condición de no repetir ningún elemento.

def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError #("El número ya existe en la lista")
        else:
            print("Añadido correctamente: ",el)
            lista.append(el)
    except ValueError:
        print("No se puede añadir: ",el)

lista = [10,20,30]
agregar_una_vez(lista, 0)
agregar_una_vez(lista,10)
print(lista)
