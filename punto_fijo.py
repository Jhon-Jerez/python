# Metodo de punto fijo
import math as m

def g(x):
    return 0.4* m.e**(x**2)

x_i=0
error =0.01
err=1
i=0

while err>error:
    x_n=g(x_i)
    err=abs(x_n-x_i)/x_n
    x_i=x_n
    i+=1
    print(f"iteracion {i}:\n x_i: {x_i:.4f} error:{err:.4f}")

print(f"solucion de la raiz: {x_i:.4f} error: {err*100:.2f}%")
