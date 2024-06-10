from tkinter import *
from tkinter import messagebox
import random

class Application:

    def __init__(self, master=None, palavras_com_dicas=[]):
        self.master = master
        self.palavras_com_dicas = palavras_com_dicas
        self.config_janela()
        self.criar_widgets()
        self.iniciar_jogo()

    def config_janela(self):
        self.master.resizable(width=False, height=False)
        self.master.geometry('450x300+600+250')
        self.master.title('Jogo da Forca')
        self.master.config(bg="#363636")

    def iniciar_jogo(self):
        self.palavra_secreta, self.dica = self.escolher_palavra()
        self.letras_corretas = []
        self.letras_erradas = []
        self.tentativas_restantes = 6
        self.atualizar_palavra()
        self.atualizar_tentativas()
        self.atualizar_dica()

    def escolher_palavra(self):
        return random.choice(self.palavras_com_dicas)

    def atualizar_palavra(self):
        palavra_mostrada = " ".join([letra if letra.upper() in self.letras_corretas else "_" for letra in self.palavra_secreta])
        self.lbl_palavra.config(text=palavra_mostrada)

    def atualizar_tentativas(self):
        self.lbl_tentativas.config(text=f"Tentativas restantes: {self.tentativas_restantes}")

    def atualizar_dica(self):
        self.lbl_dica.config(text=f"Dica: {self.dica}")

    def processar_palpite(self):
        palpite = self.ent_palpite.get().upper().strip()
        self.ent_palpite.delete(0, END)

        if len(palpite) != 1 or not palpite.isalpha():
            messagebox.showwarning("Entrada inválida", "Por favor, digite apenas uma letra do alfabeto.")
            return

        if palpite in self.letras_corretas or palpite in self.letras_erradas:
            messagebox.showwarning("Letra repetida", "Você já tentou essa letra.")
            return

        if palpite in self.palavra_secreta.upper():
            self.letras_corretas.append(palpite)
            if all(letra.upper() in self.letras_corretas for letra in self.palavra_secreta):
                messagebox.showinfo("Vitória", f"Parabéns! Você adivinhou a palavra '{self.palavra_secreta}'.")
                self.iniciar_jogo()
        else:
            self.letras_erradas.append(palpite)
            self.tentativas_restantes -= 1
            messagebox.showinfo("Errou", f"A letra '{palpite}' não está na palavra.")
            if self.tentativas_restantes == 0:
                messagebox.showinfo("Derrota", f"Você perdeu! A palavra era: '{self.palavra_secreta}'.")
                self.iniciar_jogo()

        self.atualizar_palavra()
        self.atualizar_tentativas()

    def criar_widgets(self):
        self.lbl_palavra = Label(self.master, font=("Helvetica", 24), bg="#363636", fg="#FFFFFF")
        self.lbl_palavra.pack(pady=20)

        self.lbl_tentativas = Label(self.master, text="Tentativas restantes: 6", font=("Helvetica", 14), bg="#363636", fg="#FFFFFF")
        self.lbl_tentativas.pack(pady=10)

        self.lbl_dica = Label(self.master, text="Dica: ", font=("Helvetica", 14), bg="#363636", fg="#FFFFFF")
        self.lbl_dica.pack(pady=10)

        self.ent_palpite = Entry(self.master, font=("Helvetica", 18), justify='center')
        self.ent_palpite.pack(pady=10)

        self.btn_palpite = Button(self.master, text="Enviar Palpite", command=self.processar_palpite, font=("Helvetica", 14))
        self.btn_palpite.pack(pady=20)

if __name__ == "__main__":
    palavras_com_dicas = [
        ("python", "Linguagem de programação"),
        ("tkinter", "Biblioteca de interface gráfica do Python"),
        ("programacao", "Ato de escrever códigos"),
        ("computador", "Máquina que processa informações"),
        ("jogos", "Atividade lúdica"),
        ("forca", "Jogo de adivinhação de palavras")
    ]
    
    janela = Tk()
    app = Application(master=janela, palavras_com_dicas=palavras_com_dicas)
    janela.mainloop()
