while True:

    option= int(input(" 1. Suma\n 2. Resta\n 3. Division\n 4. Multiplicacion\n 5. Potencia\n"))
    match option:
        case 1: 
            print("Digite los numeros a sumar")
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            addition = a+b
            print(f"La suma de {a} y {b} es : {addition:.2f}")
        
        case 2: 
            print("Digite los numeros a restar")
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            subtraction = a-b
            print(f"La resta de {a} y {b} es : {subtraction:.2f}")

        case 3: 
            print("Digite los numeros a dividir")
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            division = a/b
            print(f"La division de {a} y {b} es : {division:.2f}")

        case 4: 
            print("Digite los numeros a multiplicar")
            a = float(input("Primer numero: "))
            b = float(input("Segundo numero: "))
            multiplication = a*b
            print(f"La multilplicacion de {a} y {b} es : {multiplication:.2f}")

        case 5: 
            print("Digite los numeros para la pontencia")
            a = float(input("Numero base: "))
            b = float(input("Numero elevado: "))
            power = a**b
            print(f"La potencia de {a} elevado a la {b} es : {power:.2f}")