# aplicacion de listas, tuplas y diccionarios

favorite_food = ['hamburguesa', 'pera','pizza', 'carne']
favorite_food.sort(key=len) #ordenado por tamaño de palabra

print(favorite_food)

dictionary={'nombre':'Jhon', 
            'edad': '26',
            'programa': 'Ingenieria de sitemas',
            'nota':{'programacion':'3.5',
                    'calculo': '4.8',
                     'redes': '5.0' }
            }
print(f" Estudiante: {dictionary['nombre']}\n Programa: {dictionary['programa']}\n Nota Programacion: {dictionary['nota']['programacion']}")


def potencia(a,b):
    if b==0:
        return 1
    else:
        return a* potencia(a ,(b-1))
a=2
b=3

print(f"Potencia de {a} a la {b}:  {potencia(a,b)}")

def average(**kwargs):
    total=0
    amount=0
    for _, valor in kwargs.items():
        total+= float(valor)
        amount+=1
    return total/amount
    

notas={'programacion': '3.5',
       'calculo': '4.0',
       'redes': '5'}

print(f" {average(**notas):.2f}")

def average2(*args):
    total=0
    amount=0
    for valor in args:
        total+=valor
        amount+=1
    return total/amount

notas=(4,5,2,4,3)

print(f"Promedio : {average2(*notas):.2f}")