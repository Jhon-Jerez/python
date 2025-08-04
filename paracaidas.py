import math
import matplotlib.pyplot as plt

print("t | Velocidad")
g=9.8
m=68.1
c=12.5
t=0
velocidad=[]
while t <=20:
    vel= (g*m/c)*(1-math.exp(-c/m*t))
    print(t,"| ","{vel:.2f}".format(vel=vel))
    velocidad.append(vel)
    t+=1

plt.plot(velocidad)
plt.title('Velocidad de un paracaidista')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.xlabel('Tiempo (s)')    

plt.show()