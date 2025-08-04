# Aplicacion de derivadas 
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Variable y función para evaluar 
x = sp.Symbol('x')
f = x**3 - 4*x**2 + 4*x-1  

# Derivamos
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)

# Puntos críticos
criticos = sp.solve(f1, x)

# Funciones numéricas
f_func = sp.lambdify(x, f, 'numpy')
f1_func = sp.lambdify(x, f1, 'numpy')
f2_func = sp.lambdify(x, f2, 'numpy')

# Clasificación con prueba de la primera derivada
extremos = []
epsilon = 0.001
for c in criticos:
    if c.is_real:
        x0 = float(c)
        izquierda = f1_func(x0 - epsilon)
        derecha = f1_func(x0 + epsilon)
        valor_funcion = f_func(x0)
        if izquierda > 0 and derecha < 0:
            tipo = 'máximo local'
        elif izquierda < 0 and derecha > 0:
            tipo = 'mínimo local'
        else:
            tipo = 'no clasificado'
        extremos.append((x0, valor_funcion, tipo))

# Puntos de inflexión
inflexion = sp.solve(f2, x)
inflexion_reales = sorted([round(float(i), 3) for i in inflexion if i.is_real])

# Análisis de concavidad 
concavo=[]
for c in criticos:
    if c.is_real:
        x0 = float(c)
        valor_funcion = f2_func(x0)
        if valor_funcion > 0 :
            concavidad= 'hacia arriba'
        elif valor_funcion < 0:
            concavidad= 'hacia abajo'
        concavo.append((x0, valor_funcion, concavidad))
                
# Resultados
print("\n📌 Función:", f)
print("🧮 f'(x):", f1)
print("🧮 f''(x):", f2)

print("\n🟢 Puntos críticos y su clasificación (con prueba de la 1ª derivada):")
for x0, y0, tipo in extremos:
    print(f"  x = {x0:.3f}, f(x) = {y0:.3f} → {tipo}")
print("\n🟣 Concavidad en intervalos:")
for x0, valor_funcion, concavidad in concavo:
    print(f"(f''(x) = {valor_funcion:.3f}) x = {x0:.3f}: Concavidad {concavidad}")

print("\n🔵 Puntos de inflexión (f''(x) = 0):", inflexion_reales)


# Gráficas
x_vals = np.linspace(-2, 4, 800)  
y_vals = f_func(x_vals)
y1_vals = f1_func(x_vals)
y2_vals = f2_func(x_vals)

plt.figure(figsize=(10, 6))

plt.plot(x_vals, y_vals, label='f(x)', color='blue')

plt.plot(x_vals, y1_vals, label="f'(x)", color='green')

plt.plot(x_vals, y2_vals, label="f''(x)", color='red')

for x0, y0, tipo in extremos:
    color = 'ro' if 'máximo' in tipo else 'go'
    plt.plot(x0, y0, color)
    plt.text(x0, y0, tipo, fontsize=8, ha='left')


for i in inflexion_reales:
    plt.plot(i, f2_func(i), 'mo')

plt.title('Función Original, Primera y Segunda Derivada')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.ylim(-10, 10)
plt.grid(True)
plt.tight_layout()
plt.show()

