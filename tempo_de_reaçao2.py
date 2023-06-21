import pygame
import time
import random

# Inicialização do pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulador de Tempo de Reação")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Variáveis de controle
contador_aleatorio = 0
tempo_inicio_contagem = 0
tempo_inicio_reacao = 0
tempo_reacao = 0
contagem_finalizada = False
reacao_iniciada = False

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            if not contagem_finalizada:
                contador_aleatorio = random.randint(2, 6)  # Tempo aleatório para mudar a cor da tela
                contagem_finalizada = True
                tempo_inicio_contagem = time.time()
    
    # Preenche a janela com a cor branca ou azul
    if contagem_finalizada and not reacao_iniciada:
        janela.fill(AZUL)
    else:
        janela.fill(BRANCO)

    if contagem_finalizada and not reacao_iniciada:
        tempo_atual_contagem = time.time() - tempo_inicio_contagem
        if tempo_atual_contagem >= contador_aleatorio:
            reacao_iniciada = True 
            tempo_inicio_reacao = time.time()
    elif reacao_iniciada:
        if pygame.mouse.get_pressed()[0] == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
            tempo_fim_reacao = time.time()
            tempo_reacao = tempo_fim_reacao - tempo_inicio_reacao
            print(f"Seu tempo de reação foi de {tempo_reacao:.3f} segundos.")
            contagem_finalizada = False
            reacao_iniciada = False
    
    # Atualiza a janela
    pygame.display.update()

# Encerra o pygame
pygame.quit()
