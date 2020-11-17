# Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter.
# Escribir un programa que lea una palabra y la muestre usando el código morse.

codigo = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
          'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
          'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
          'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
          '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
          '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', ':': '---...',
          ';': '-.-.-.', '?': '..--..', '!': '-.-.--', '"': '.-..-.', "'": '.----.',
          '+': '.-.-.', "-": '-....-', '/': '-..-.', '=': '-...-', '_': '..--.-',
          "$": '...-..-', '@': '.--.-.', '&': '.-...', '(': '-.--.', ')': '-.--.-'}

frase = input("Introduzca la frase: ")
palabras = frase.split(" ")
for caracter in frase:
    if caracter.islower():
        caracter = caracter.upper()
    palabras.append(codigo[caracter])
print(" ".join(palabras))


palabras = input("Morse:")
morse = palabras.split(" ")
palabra = ""
for cod in morse:
    letra=[key for key,valor in codigo.items() if valor==cod][0]
    palabra=palabra+letra
print (palabra)
