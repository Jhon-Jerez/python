#calculo factorial iterativa

def factorial(n):
    resultado=1
    for i in range(1, n + 1):
      resultado *= i
    return resultado

n=int(input("ingrese numero: "))
print(factorial(n))


#factorial recursivo

def factorial_recursivo(p):
    if p<0:
        raise ValueError("No existe factorial de negativos")
    if p==0:
        return 1
    return p *factorial_recursivo(p-1)

p= int(input("Ingrese numero: "))
print(factorial_recursivo(p))
