def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    if anio % 4 == 0:
        return True
    return False

def dias_en_mes(mes, anio):
    if mes == 2:
        return 29 if es_bisiesto(anio) else 28
    if mes in [4, 6, 9, 11]:
        return 30
    return 31

def fecha_a_dias(anio, mes, dia):
    total = dia
    m = 1
    while m < mes:
        total += dias_en_mes(m, anio)
        m += 1
    a = 1
    while a < anio:
        total += 366 if es_bisiesto(a) else 365
        a += 1
    return total

def dias_entre(fecha1, fecha2):
    a1, m1, d1 = [int(x) for x in fecha1.split('-')]
    a2, m2, d2 = [int(x) for x in fecha2.split('-')]
    
    dias1 = fecha_a_dias(a1, m1, d1)
    dias2 = fecha_a_dias(a2, m2, d2)
    
    return dias2 - dias1 if dias2 > dias1 else dias1 - dias2

# Ejemplo de uso
f1 = "2025-01-01"
f2 = "2024-01-01"
print(dias_entre(f1, f2))  


