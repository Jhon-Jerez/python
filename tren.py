# trenes datos

distancia = 200
velocidad_trenes= 50
velocidad_mosca= 75
distancia_entre_trenes= distancia
t=0.1
dt=0.1
distacia_total_mosca=0
posicion_tren1=0
posicion_tren2=distancia
posicion_mosca=0
direccion_mosca=1

print("t | p_tren1 | p_tren2 | d_trenes | p_mosca | d_T_mosca")

while distancia_entre_trenes >0:
    posicion_tren1 += velocidad_trenes*dt
    posicion_tren2 -= velocidad_trenes*dt
    distancia_entre_trenes-= 2*velocidad_trenes*dt
    distancia_mosca = velocidad_mosca*dt
    distacia_total_mosca +=distancia_mosca
    posicion_mosca += direccion_mosca*distancia_mosca

    if posicion_mosca>= posicion_tren2:
        posicion_mosca =posicion_tren2
        direccion_moscas=-1
    elif posicion_mosca<=posicion_tren1:
        posicion_mosca=posicion_tren1
        direccion_mosca=1


    print(f"{t:.1} | {posicion_tren1:.2f} | {posicion_tren2:.2f} | {distancia_entre_trenes:.2f} | {posicion_mosca:.2f} | {distacia_total_mosca:.2f}")
    t+= dt