import tkinter as tk
import time

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronômetro")

        self.tempo_inicial = 0
        self.tempo_corrente = 0
        self.executando = False

        self.label_tempo = tk.Label(janela, text="00:00:00", font=("Arial", 24))
        self.label_tempo.pack(pady=10)

        self.botao_iniciar = tk.Button(janela, text="Iniciar", command=self.iniciar_cronometro)
        self.botao_iniciar.pack()

        self.botao_parar = tk.Button(janela, text="Parar", command=self.parar_cronometro)
        self.botao_parar.pack()

    def iniciar_cronometro(self):
        if not self.executando:
            self.tempo_inicial = time.time() - self.tempo_corrente
            self.executando = True
            self.atualizar_cronometro()

    def parar_cronometro(self):
        if self.executando:
            self.janela.after_cancel(self.atualizacao)
            self.executando = False
            self.botao_iniciar.config(state=tk.NORMAL)

    def atualizar_cronometro(self):
        if self.executando:
            self.tempo_corrente = time.time() - self.tempo_inicial
            minutos, segundos = divmod(self.tempo_corrente, 60)
            horas, minutos = divmod(minutos, 60)
            tempo_formatado = "{:02d}:{:02d}:{:02d}".format(int(horas), int(minutos), int(segundos))
            self.label_tempo.config(text=tempo_formatado)
            self.atualizacao = self.janela.after(1000, self.atualizar_cronometro)

    def iniciar(self):
        self.janela.mainloop()

janela = tk.Tk()
cronometro = Cronometro(janela)
cronometro.iniciar()
