import random

#tabla del 9 

for i in range(1,11):
    result= 9*i
    print(f"9 * {i}= {result}")
    i+=1


print("Intenta adividar el numero en 3 intentos")
number_guess = random.randint(1,10)
print(number_guess)
i=0
while i<3:
    i+=1
    option = int(input(f"intento {i}: "))

if option==number_guess:
    print(f"Felicidades adivinaste era el numero {number_guess}")
else:
    print("No adivinaste")