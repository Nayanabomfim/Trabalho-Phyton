import tkinter as tk
from tkinter import messagebox

def adicionar_tarefa():
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    if titulo and descricao:
        nova_tarefa = {'titulo': titulo, 'descricao': descricao}
        lista_tarefas.append(nova_tarefa)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
        entry_titulo.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

def mostrar_tarefas():
    if not lista_tarefas:
        messagebox.showinfo("Lista de Tarefas", "Não há tarefas na lista.")
    else:
        tarefas_text = "Lista de tarefas:\n\n"
        for i, tarefa in enumerate(lista_tarefas, 1):
            tarefas_text += f"{i}. {tarefa['titulo']}: {tarefa['descricao']}\n"
        messagebox.showinfo("Lista de Tarefas", tarefas_text)

# Lista vazia de tarefas
lista_tarefas = []

# Criando a janela principal
root = tk.Tk()
root.title("Lista de Tarefas")

# Criando os widgets
label_titulo = tk.Label(root, text="Título:")
label_titulo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_titulo = tk.Entry(root, width=50)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

label_descricao = tk.Label(root, text="Descrição:")
label_descricao.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_descricao = tk.Entry(root, width=50)
entry_descricao.grid(row=1, column=1, padx=5, pady=5)

botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

botao_mostrar = tk.Button(root, text="Mostrar Tarefas", command=mostrar_tarefas)
botao_mostrar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Iniciando o loop da interface gráfica
root.mainloop()
