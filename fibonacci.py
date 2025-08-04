#Fibonacci iterativo
a=0
b=1
n=int(input('Cantidad de numeros de la serie de fibonacci: '))

for _ in range(n):
    print(a, end=',')
    a , b= b, a+b

#fibonacci recursivo
def fibonacci(n):
    if n<=0:
        return []
    if n==1:
        return [0]
    if n==2:
        return[0,1]
    else:
        serie=fibonacci(n-1)
        serie.append(serie[-1]+serie[-2])
    return serie

n=int(input('\nCantidad de numeros de la serie de fibonacci: '))
print(fibonacci(n))