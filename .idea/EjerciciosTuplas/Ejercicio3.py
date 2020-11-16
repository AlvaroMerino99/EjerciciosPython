#Escribir un programa en python, que dada una palabra diga si es un palíndromo. Un
#palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia
#atrás. Ejemplo: reconocer.

cadena=input("Introduce la cadena:")
if cadena.lower()==cadena[::-1].lower():
    print("ES PALINDROMO!!")
else:
    print("NO ES PALINDROMO!!")