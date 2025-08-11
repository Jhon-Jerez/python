#aplicacion de listas, tuplas y diccionarios

# favorite_food = ['hamburguesa', 'pera','pizza', 'carne']
# favorite_food.sort(key=len) #ordenado por tamaño de palabra

# print(favorite_food)

dictionary={'nombre':'Jhon', 
            'edad': '26',
            'programa': 'Ingenieria de sitemas',
            'nota':{'programacion':'3.5',
                    'calculo': '4.8',
                     'redes': '5.0' }
            }
print(f" Estudiante: {dictionary['nombre']}\n Programa: {dictionary['programa']}\n Nota Programacion: {dictionary['nota']['programacion']}")