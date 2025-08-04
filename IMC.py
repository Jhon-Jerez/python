name = input("Escriba su nombre: ")
age = int(input("Escriba su edad: "))
weight = float(input("Escriba su peso: "))# en kilogramos
height = float(input("Escriba su altura: "))

imc = weight/height**2

print(f"{name} tu IMC es {imc:.2f}")

if imc < 18.5:
    print("Peso isuficiente")
elif imc <= 24.9:
    print("Peso saludable")
elif imc<= 34.9:
    print("Obesidad clase I")
elif imc<= 39.9:
    print("Obesidad clase II")
else:
    print("Obesidad clase III")
