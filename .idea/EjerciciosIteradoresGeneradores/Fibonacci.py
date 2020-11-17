#Implementa un generador fibonacci que produce los diferentes de la secuencia de Fibonacci, que tiene la forma:
#0, 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
    if n==0:
        sucesion_fibonacci=[]
    elif n==1:
        sucesion_fibonacci=[1]
    elif n==2:
        sucesion_fibonacci=[0,1]
    elif n>2:
        sucesion_fibonacci=[0,1]
        i=1
        while i<n-1:
            sucesion_fibonacci.append(sucesion_fibonacci[i]+sucesion_fibonacci[i-1])
            i+=1
    return sucesion_fibonacci

if __name__== '__main__':
    resultado=fibonacci(8)
    print(resultado)