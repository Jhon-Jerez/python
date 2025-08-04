
import numpy as np

# Constantes
I0 = 10**(-16)       # Umbral auditivo en W/cm²
beta = 40        # Nivel dB a 100 cm
r = 100          # Distancia inicial en cm
I1 = I0 * 10**(beta / 10)

# Calcular potencia de la fuente
P = I1 * 4 * np.pi * r**2

print("📊 Tabla de distancias y niveles:")
print(f"{'Distancia (cm)':>15} | {'Nivel (dB)':>10}")
print("-" * 30)
beta_actual=100
while beta_actual>0:
    I = P / (4 * np.pi * r**2)
    beta_actual = 10 * np.log10(I / I0)
    print(f"{r:15} | {beta_actual:10.1f}")
    r += 100

