name = input("Escriba su nombre: ")
age = int(input("Escriba su edad: "))
weight = float(input("Escriba su peso: "))# en kilogramos
height = float(input("Escriba su altura: "))

imc = weight/height**2

print(f"{name} tu IMC es {imc:.2f}")

|