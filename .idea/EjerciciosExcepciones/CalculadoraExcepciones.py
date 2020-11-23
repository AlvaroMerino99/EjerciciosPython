print("CALCULADORA")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("'S'. Salir")

opcion=(input("Elija la opcion: "))
while opcion!='S':
    try:
        if(opcion=='1'):
            x = int(input("Ingrese Numero: "))
            y = int(input("Ingrese Otro Numero: "))
            print("La suma es: ",x+y)
            opcion = (input("Selecione Opcion: "))
        elif(opcion=='2'):
            x = int(input("Ingrese Numero: "))
            y = int(input("Ingrese Otro Numero: "))
            print("La resta es: ",x-y)
            opcion = (input("Selecione Opcion: "))
        elif(opcion=='3'):
            x = int(input("Ingrese Numero: "))
            y = int(input("Ingrese Otro Numero: "))
            print("La multiplicacion es: ",x*y)
            opcion = (input("Selecione Opcion: "))
        elif(opcion=='4'):
            x = int(input("Ingrese Numero: "))
            y = int(input("Ingrese Otro Numero: "))
            print("La division es: ",x/y)
            opcion = (input("Selecione Opcion: "))
        elif(opcion=='5'):
            x = int(input("Ingrese Numero: "))
            y = int(input("Ingrese Otro Numero: "))
            print("La potencia es: ",x**y)
            opcion = (input("Selecione Opcion: "))
        else:
            print("Valor no válido")
            opcion= input("Introduzca una opcion válida: ")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except ValueError:
        print("Valor no válido")
    except:
        print("Otro tipo de error")
print("Fin del programa...")

