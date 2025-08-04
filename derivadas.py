import tkinter as tk
from tkinter import messagebox, scrolledtext
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class AnalizadorFunciones:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Análisis de Funciones")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        self.x = sp.Symbol('x')
        self.fx = None
        self.dfx = None
        self.d2fx = None
        self.criticos = []
        self.inflexion = []
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        titulo = tk.Label(main_frame, text="ANALIZADOR DE FUNCIONES", 
                         font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2c3e50")
        titulo.pack(pady=(0, 20))
        
        entrada_frame = tk.Frame(main_frame, bg="#f0f0f0")
        entrada_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(entrada_frame, text="Ingrese la función f(x):", 
                font=("Arial", 12), bg="#f0f0f0").pack(anchor="w")
        
        self.entrada_fx = tk.Entry(entrada_frame, width=50, font=("Arial", 11))
        self.entrada_fx.pack(fill="x", pady=(5, 10))
        
        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.pack(fill="x", pady=(0, 20))
        
        tk.Button(botones_frame, text="CALCULAR", command=self.calcular, 
                 bg="#3498db", fg="white", font=("Arial", 11, "bold"), 
                 width=12, height=2).pack(side="left", padx=(0, 10))
        
        tk.Button(botones_frame, text="GRAFICAR", command=self.graficar, 
                 bg="#27ae60", fg="white", font=("Arial", 11, "bold"), 
                 width=12, height=2).pack(side="left", padx=(0, 10))
        
        tk.Button(botones_frame, text="LIMPIAR", command=self.limpiar, 
                 bg="#e74c3c", fg="white", font=("Arial", 11, "bold"), 
                 width=12, height=2).pack(side="left")
        
        resultados_frame = tk.Frame(main_frame, bg="#f0f0f0")
        resultados_frame.pack(fill="both", expand=True)
        
        tk.Label(resultados_frame, text="RESULTADOS:", 
                font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#2c3e50").pack(anchor="w")
        
        self.texto_resultados = scrolledtext.ScrolledText(
            resultados_frame, height=25, width=70, font=("Consolas", 10),
            bg="white", fg="#2c3e50", wrap=tk.WORD
        )
        self.texto_resultados.pack(fill="both", expand=True, pady=(10, 0))
    
    def calcular(self):
        try:
            fx_exp = self.entrada_fx.get().strip()
            if not fx_exp:
                messagebox.showwarning("Advertencia", "Por favor ingrese una función")
                return
            
            self.fx = sp.sympify(fx_exp)
            self.dfx = sp.diff(self.fx, self.x)
            self.d2fx = sp.diff(self.dfx, self.x)
            
            # Calculo puntos criticos
            self.criticos = sp.solve(self.dfx, self.x)
            criticos_reales = [c for c in self.criticos if c.is_real]
            
            # Calcular inflexion
            self.inflexion = sp.solve(self.d2fx, self.x)
            inflexion_reales = [i for i in self.inflexion if i.is_real]
            
            # Mostrar resultados
            self.mostrar_resultados(criticos_reales, inflexion_reales)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar la función: {str(e)}")
    
    def mostrar_resultados(self, criticos_reales, inflexion_reales):
        self.texto_resultados.delete(1.0, tk.END)
        
        resultado = "=" * 48 + "\n"
        resultado += "              ANÁLISIS DE LA FUNCIÓN\n"
        resultado += "=" * 48 + "\n\n"
        
        # Funciones
        resultado += "FUNCIONES:\n"
        resultado += "-" * 40 + "\n"
        resultado += f"f(x)  = {self.fx}\n"
        resultado += f"f'(x) = {self.dfx}\n"
        resultado += f"f''(x) = {self.d2fx}\n\n"
        
        resultado += "PUNTOS CRÍTICOS:\n"
        resultado += "-" * 40 + "\n"
        if criticos_reales:
            for i, c in enumerate(criticos_reales, 1):
                c_val = float(c.evalf())
                y_val = float(self.fx.subs(self.x, c).evalf())
                
                segunda_derivada = self.d2fx.subs(self.x, c).evalf()
                if segunda_derivada > 0:
                    tipo = "MÍNIMO LOCAL"
                elif segunda_derivada < 0:
                    tipo = "MÁXIMO LOCAL"
                else:
                    tipo = "PUNTO DE SILLA (indeterminado)"
                
                resultado += f"{i}. Coordenadas: ({c_val:.2f}, {y_val:.2f})\n"
                resultado += f"   Tipo: {tipo}\n"
                resultado += f"   f''({c_val:.2f}) = {float(segunda_derivada):.2f}\n\n"
        else:
            resultado += "No se encontraron puntos críticos reales.\n\n"
        
        resultado += "PUNTOS DE INFLEXIÓN:\n"
        resultado += "-" * 40 + "\n"
        if inflexion_reales:
            for i, inf in enumerate(inflexion_reales, 1):
                inf_val = float(inf.evalf())
                y_inf_val = float(self.fx.subs(self.x, inf).evalf())
                
                resultado += f"{i}. Coordenadas: ({inf_val:.2f}, {y_inf_val:.2f})\n"
                resultado += f"   f''({inf_val:.2f}) = 0\n\n"
        else:
            resultado += "No se encontraron puntos de inflexión reales.\n\n"
        
        if criticos_reales:
            resultado += "CONCAVIDAD EN PUNTOS CRÍTICOS:\n"
            resultado += "-" * 40 + "\n"
            for c in criticos_reales:
                c_val = float(c.evalf())
                segunda_derivada = float(self.d2fx.subs(self.x, c).evalf())
                
                if segunda_derivada > 0:
                    concavidad = "Cóncava hacia ARRIBA"
                elif segunda_derivada < 0:
                    concavidad = "Cóncava hacia ABAJO"
                else:
                    concavidad = "Punto de inflexión posible"
                
                resultado += f"x = {c_val:.2f}: {concavidad}\n"
            resultado += "\n"
        
        resultado += "=" * 48 + "\n"
        resultado += "Análisis completado. Use 'GRAFICAR' para visualizar.\n"
        resultado += "=" * 48
        
        self.texto_resultados.insert(tk.END, resultado)
    
    def graficar(self):
        if self.fx is None:
            messagebox.showwarning("Advertencia", "Primero debe calcular una función")
            return
        
        try:
            if self.criticos:
                x_min = min([float(c.evalf()) for c in self.criticos if c.is_real]) - 2
                x_max = max([float(c.evalf()) for c in self.criticos if c.is_real]) + 2
            else:
                x_min, x_max = -5, 5
            
            x_vals = np.linspace(x_min, x_max, 400)
            
            # Evaluar funciones
            fx_vals = []
            dfx_vals = []
            d2fx_vals = []
            
            for val in x_vals:
                try:
                    fx_vals.append(float(self.fx.subs(self.x, val).evalf()))
                    dfx_vals.append(float(self.dfx.subs(self.x, val).evalf()))
                    d2fx_vals.append(float(self.d2fx.subs(self.x, val).evalf()))
                except:
                    fx_vals.append(np.nan)
                    dfx_vals.append(np.nan)
                    d2fx_vals.append(np.nan)
            
            plt.figure(figsize=(8, 6))
            
            plt.plot(x_vals, fx_vals, label="f(x)", color="blue", linewidth=2)
            plt.plot(x_vals, dfx_vals, label="f'(x)", color="red", linestyle="--", linewidth=2)
            plt.plot(x_vals, d2fx_vals, label="f''(x)", color="green", linestyle=":", linewidth=2)
            
            criticos_reales = [c for c in self.criticos if c.is_real]
            if criticos_reales:
                criticos_x = [float(c.evalf()) for c in criticos_reales]
                criticos_y = [float(self.fx.subs(self.x, c).evalf()) for c in criticos_reales]
                plt.scatter(criticos_x, criticos_y, color="purple", marker="o", 
                           s=100, label="Puntos críticos", zorder=5, edgecolors='white', linewidth=2)
            
            # Marcar puntos de inflexión
            inflexion_reales = [i for i in self.inflexion if i.is_real]
            if inflexion_reales:
                inflexion_x = [float(i.evalf()) for i in inflexion_reales]
                inflexion_y = [float(self.fx.subs(self.x, i).evalf()) for i in inflexion_reales]
                plt.scatter(inflexion_x, inflexion_y, color="orange", marker="s", 
                           s=100, label="Puntos de inflexión", zorder=5, edgecolors='white', linewidth=2)
            
            # Líneas de referencia
            plt.axhline(0, color="black", linewidth=0.8, linestyle="-", alpha=0.3)
            plt.axvline(0, color="black", linewidth=0.8, linestyle="-", alpha=0.3)
            
            # Configurar gráfica
            plt.xlabel("x", fontsize=12)
            plt.ylabel("y", fontsize=12)
            plt.title(f"Análisis gráfico de f(x) = {self.fx}", fontsize=14, fontweight='bold')
            plt.legend(fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            plt.show()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al graficar: {str(e)}")
    
    def limpiar(self):
        self.entrada_fx.delete(0, tk.END)
        self.texto_resultados.delete(1.0, tk.END)
        self.fx = None
        self.dfx = None
        self.d2fx = None
        self.criticos = []
        self.inflexion = []
        
        mensaje_inicial = "=" * 48 + "\n"
        mensaje_inicial += "           ANALIZADOR DE FUNCIONES MATEMÁTICAS\n"
        mensaje_inicial += "=" * 48 + "\n\n"
        mensaje_inicial += "INSTRUCCIONES:\n"
        mensaje_inicial += "-" * 40 + "\n"
        mensaje_inicial += "1. Ingrese una función matemática en términos de 'x'\n"
        mensaje_inicial += "2. Presione 'CALCULAR' para obtener el análisis\n"
        mensaje_inicial += "3. Presione 'GRAFICAR' para visualizar las funciones\n"
        mensaje_inicial += "4. Use 'LIMPIAR' para ingresar una nueva función\n\n"
        mensaje_inicial += "EJEMPLOS DE FUNCIONES:\n"
        mensaje_inicial += "-" * 40 + "\n"
        mensaje_inicial += "• x**2 + 3*x - 5\n"
        mensaje_inicial += "• sin(x) + cos(x)\n"
        mensaje_inicial += "• exp(x) - x**2\n"
        mensaje_inicial += "• x**3 - 6*x**2 + 9*x + 1\n\n"
        mensaje_inicial += "¡Ingrese su función y comience el análisis!"
        
        self.texto_resultados.insert(tk.END, mensaje_inicial)
    
    def ejecutar(self):
        self.limpiar()
        self.root.mainloop()

if __name__ == "__main__":
    app = AnalizadorFunciones()
    app.ejecutar()