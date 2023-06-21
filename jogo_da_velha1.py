import tkinter as tk
from tkinter import messagebox

class JogoDaVelhaGUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")

        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

        self.criar_quadros()
    
    def criar_quadros(self):
        self.quadros = []

        for linha in range(3):
            for coluna in range(3):
                quadro = tk.Frame(
                    self.janela,
                    width=100,
                    height=100,
                    relief=tk.RAISED,
                    borderwidth=2
                )
                quadro.grid(row=linha, column=coluna)
                quadro.bind("<Button-1>", lambda event, l=linha, c=coluna: self.realizar_jogada(l, c))
                
                label = tk.Label(quadro, font=("Arial", 40), text=self.tabuleiro[linha][coluna])
                label.pack()

                self.quadros.append((quadro, label))

    def realizar_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual

            for quadro, _ in self.quadros:
                quadro.unbind("<Button-1>")

            self.quadros[linha * 3 + coluna][1].config(text=self.jogador_atual)

            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo("Fim de jogo", f"Jogador {self.jogador_atual} venceu!")
                self.janela.quit()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.janela.quit()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self, jogador):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha.count(jogador) == 3:
                return True

        # Verificar colunas
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] == jogador:
                return True

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador:
            return True

        return False

    def verificar_empate(self):
        return all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3))

    def iniciar(self):
        self.janela.mainloop()

jogo = JogoDaVelhaGUI()
jogo.iniciar()
