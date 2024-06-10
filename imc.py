import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora de IMC")
        
        # Labels
        self.label_height = tk.Label(self.window, text="Altura (m):")
        self.label_height.grid(row=0, column=0)
        self.label_weight = tk.Label(self.window, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0)
        
        # Entries
        self.entry_height = tk.Entry(self.window)
        self.entry_height.grid(row=0, column=1)
        self.entry_weight = tk.Entry(self.window)
        self.entry_weight.grid(row=1, column=1)
        
        # Button
        self.button_calculate = tk.Button(self.window, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calculate.grid(row=2, columnspan=2)
        
        # Result Label
        self.label_result = tk.Label(self.window, text="Resultado do IMC")
        self.label_result.grid(row=3, columnspan=2)
        
    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            bmi = weight / (height ** 2)
            self.label_result.config(text=f"IMC: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
    
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria do IMC", f"Você está na categoria: {category}")

if __name__ == "__main__":
    app = BMICalculator()
    app.window.mainloop()