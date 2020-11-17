#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena.
#Por ejemplo, si recibe “Qué lindo día que hace hoy” debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1

#!/usr/bin/env python
diccionario=dict()
frase=input("Introduzca la frase: ")
palabras=frase.split(" ")
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra]+=1
    else:
        diccionario[palabra]=1

for termino,valor in diccionario.items():
    print (termino,": ",valor)