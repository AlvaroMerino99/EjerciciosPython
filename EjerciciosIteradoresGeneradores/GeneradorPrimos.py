#Implementa un generador primos que genere todos los números primos.
# Por eficiencia, el generador debe ir almacenando los primos encontrados hasta el momento en una lista.

def calcularPrimos():
    primos=[]
    for x in count(2):
        posibles = takewhile(lambda p: p*p<x, primos)
        if not any (map(lambda p: x%p==0, posibles)):
            primos.append(x)
            yield x
if __name__ == '__main__':
    p=calcularPrimos()
    print(p,10)