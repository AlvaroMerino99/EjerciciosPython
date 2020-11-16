#Crea un programa en python que lea una cadena de caracteres y muestre la siguiente
#información:
#a. La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus,
#debe devolver USB.
#b. Dicha cadena con la primera letra de cada palabra en mayúsculas. Por
#ejemplo, si recibe república argentina, debe devolver República Argentina.
#c. Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de
#ayer, debe devolver Antes ayer

cadena=input("Cadena:")

# A)
lista=cadena.split(" ")
for palabra in lista:
    print (palabra[0],end="")
print()
# B)
for palabra in lista:
    print (palabra.capitalize(),end=" ")
print()
# C)
for palabra in lista:
    if palabra.startswith("a") or palabra.startswith("A"):
        print (palabra,end=" ")
print()