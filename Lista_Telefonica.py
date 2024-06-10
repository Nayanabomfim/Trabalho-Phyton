import tkinter as tk
from tkinter import messagebox

# Definição da classe ListaTelefonica
class ListaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone
        return f"Contato {nome} adicionado com sucesso."

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            return f"Contato {nome} removido com sucesso."
        else:
            return f"Contato {nome} não encontrado."

    def buscar_contato(self, nome):
        if nome in self.contatos:
            return f"{nome}: {self.contatos[nome]}"
        else:
            return f"Contato {nome} não encontrado."

    def listar_contatos(self):
        if self.contatos:
            return "\n".join([f"{nome}: {telefone}" for nome, telefone in self.contatos.items()])
        else:
            return "A lista de contatos está vazia."

# Funções para interagir com a interface
def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    if nome and telefone:
        mensagem = lista_telefonica.adicionar_contato(nome, telefone)
        messagebox.showinfo("Informação", mensagem)
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

def remover_contato():
    nome = entry_nome.get()
    if nome:
        mensagem = lista_telefonica.remover_contato(nome)
        messagebox.showinfo("Informação", mensagem)
        entry_nome.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha o campo nome.")

def buscar_contato():
    nome = entry_nome.get()
    if nome:
        mensagem = lista_telefonica.buscar_contato(nome)
        messagebox.showinfo("Informação", mensagem)
    else:
        messagebox.showwarning("Aviso", "Preencha o campo nome.")

def listar_contatos():
    contatos = lista_telefonica.listar_contatos()
    messagebox.showinfo("Lista de Contatos", contatos)

# Criação da interface gráfica
root = tk.Tk()
root.title("Lista Telefônica")

lista_telefonica = ListaTelefonica()

frame = tk.Frame(root)
frame.pack(pady=20)

label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_telefone = tk.Label(frame, text="Telefone:")
label_telefone.grid(row=1, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(frame)
entry_telefone.grid(row=1, column=1, padx=10, pady=5)

button_adicionar = tk.Button(frame, text="Adicionar Contato", command=adicionar_contato)
button_adicionar.grid(row=2, column=0, columnspan=2, pady=5)

button_remover = tk.Button(frame, text="Remover Contato", command=remover_contato)
button_remover.grid(row=3, column=0, columnspan=2, pady=5)

button_buscar = tk.Button(frame, text="Buscar Contato", command=buscar_contato)
button_buscar.grid(row=4, column=0, columnspan=2, pady=5)

button_listar = tk.Button(frame, text="Listar Contatos", command=listar_contatos)
button_listar.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
