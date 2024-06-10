from tkinter import *
from tkinter import messagebox

janela = Tk()

class Aplication:

    def __init__(self):
        self.config_janela()
        self.tema_principal()
        self.frame_calculadora()
        self.numeros()
        self.operadores()
        self.calculando()

        janela.mainloop()

    def config_janela(self):
        janela.resizable(width=False, height=False)
        janela.geometry('450x450+750+300')
        janela.title('Calculadora')
        janela.config(bg="#363636")

    def tema_principal(self):
        frame_principal = Frame(janela, bd='5', width='250', height='50')
        frame_principal.place(x=80, y=5)

        label_cal = Label(frame_principal, text='Calculadora', font='Arial 15')
        label_cal.place(x=65, y=5)

    def frame_calculadora(self):
        self.valor = Frame(janela, bd='6', width=380, height=370)
        self.valor.place(x=35, y='65')

        self.mostrar_result = Frame(self.valor, bd='5', width=330, height=50,)
        self.mostrar_result.config(bg='#586e75')
        self.mostrar_result.place(x=10, y=10)

        info_valor = Label(self.mostrar_result, text='Valor:', bd='5', font='Arial, 15', bg='#586e75')
        info_valor.place(x=10, y=5)

    def numeros(self):
        buttons = [
            ('1', 10, 70), ('2', 95, 70), ('3', 180, 70),
            ('4', 10, 140), ('5', 95, 140), ('6', 180, 140),
            ('7', 10, 210), ('8', 95, 210), ('9', 180, 210),
            ('0', 10, 280)
        ]
        
        for (text, x, y) in buttons:
            button = Button(self.valor, text=text, bd=5, font='Arial 15', width=5, height=1, command=lambda t=text: self.adicionar_entrada(t))
            button.place(x=x, y=y)

    def operadores(self):
        buttons = [
            ('+', 270, 70), ('-', 270, 140), 
            ('x', 270, 210), ('/', 270, 280), 
            ('AC', 95, 280),('=', 180, 280)
        ]

        for (text, x, y) in buttons:
            if text == '=':
                button = Button(self.valor, text=text, bd=5, font='Arial 15', width=5, height=1, command=self.calcular)

            elif text == 'AC':
                button = Button(self.valor, text=text, bd=5, font='Arial 15', width=5, height=1, command=self.limpar_entrada)
                
            else:
                button = Button(self.valor, text=text, bd=5, font='Arial 15', width=5, height=1, command=lambda t=text: self.adicionar_entrada(t))

            button.place(x=x, y=y)

    def adicionar_entrada(self, valor):
        self.valor_entry.config(state='normal')
        self.valor_entry.insert(END, valor)
        self.valor_entry.config(state='readonly')

    def calcular(self):
        self.valor_entry.config(state='normal')

        try:
            expressao = self.valor_entry.get().replace('x', '*')
            resultado = eval(expressao)
            self.valor_entry.delete(0, END)
            self.valor_entry.insert(0, str(resultado))

        except Exception as e:
            messagebox.showerror("Erro", "Entrada inválida")
            self.valor_entry.delete(0, 'end')

        self.valor_entry.config(state='readonly')

    def calculando(self):
        self.valor_entry = Entry(self.mostrar_result, font='Arial 15', bd='5', width=15)
        self.valor_entry.config(state='readonly')
        self.valor_entry.place(x=90, y=3)

    def limpar_entrada(self):
        self.valor_entry.config(state='normal')
        self.valor_entry.delete(0, END)
        self.valor_entry.config(state='readonly')

app = Aplication()