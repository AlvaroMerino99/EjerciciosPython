import  csv
fichero = open("personas.csv", 'r', encoding="utf8")
contenido = csv.reader(fichero)
for row in contenido:
    print(str(row))
fichero.close()