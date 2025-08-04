import tkinter as tk
from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np



root = tk.Tk()
root.title("Método de Newton-Raphson")
root.geometry("300x200")  

x = sp.Symbol('x')

def calcular():
    try:
        fx_exp = entrada_fx.get()
        fx_exp = fx_exp.replace("^", "**")  
        fx = sp.sympify(fx_exp)  
        dfx = sp.diff(fx, x)  

        x_i = float(entrada_xi.get())  
        error = float(entrada_error.get()) 
        err = 1
        i = 0

        resultado = "Iteraciones:\n"
        x_vals = [x_i]
        fx_vals = [fx.subs(x, x_i).evalf()]
        colores = plt.cm.viridis(np.linspace(0, 4, 10))
        funciones=f"f(x): {fx}\n f'(x): {dfx}"
        
        while err > error:
            fx_eva = fx.subs(x, x_i).evalf()
            dfx_eva = dfx.subs(x, x_i).evalf()

            if dfx_eva == 0:
                messagebox.showerror("Error", "La derivada es cero, no se puede continuar.")
                return

            x_n = x_i - (fx_eva / dfx_eva)
            err = abs(x_n - x_i) / abs(x_n)
            x_i = x_n
            i += 1
            x_vals.append(x_i)
            fx_vals.append(fx.subs(x, x_i).evalf())

            
            resultado += f" Iteración {i}: x_i = {x_i:.4f}  f(x) = {fx_eva:.4f}  f'(x) = {dfx_eva:.4f}, Error = {err:.3f}\n"

        resultado += f"\n Raíz Aproximada: {x_i:.4f} Error: {err*100:.2f}%"
        messagebox.showinfo("Resultado",f"{funciones}\n\n {resultado}")

        x_range = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 100)
        y_range = [fx.subs(x, val).evalf() for val in x_range]
        plt.figure(figsize=(6,4))
        plt.plot(x_range, y_range, label="Función f(x)", color="blue")

        for idx, x_val in enumerate(x_vals):
            plt.scatter(x_val, fx.subs(x, x_val).evalf(), color=colores[idx % len(colores)], marker="o", label=f"Iteración {idx+1}")

        plt.axhline(0, color="black", linewidth=1, linestyle="--")
        plt.xlabel("x_i")
        plt.ylabel("f(x)")
        plt.legend()
        plt.title("Método de Newton-Raphson - Convergencia a la Raíz")
        plt.grid()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

tk.Label(root, text="Ingrese la función f(x):").pack()
entrada_fx = tk.Entry(root, width=30)
entrada_fx.pack()

tk.Label(root, text="Valor inicial x₀:").pack()
entrada_xi = tk.Entry(root, width=10)
entrada_xi.pack()

tk.Label(root, text="Error tolerable:").pack()
entrada_error = tk.Entry(root, width=10)
entrada_error.pack()

tk.Button(root, text="Calcular Raíz", command=calcular,  bg="black", fg="white").pack(pady=15)

root.mainloop()

