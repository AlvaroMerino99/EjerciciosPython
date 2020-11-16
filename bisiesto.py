
año = int(input("Introduzca el año: "))

if año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
    print("Es bisiesto")
else:
    print("No bisiesto")