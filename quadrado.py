import pygame

# Inicialização do Pygame
pygame.init()

# Definição das cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Definição do tamanho da janela
largura_janela = 500
altura_janela = 500

# Criação da janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Quadrado")

# Variáveis do quadrado
tamanho_quadrado = 100
pos_x = (largura_janela - tamanho_quadrado) // 2
pos_y = (altura_janela - tamanho_quadrado) // 2

# Loop principal do jogo
jogo_executando = True
while jogo_executando:
    # Verificação de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_executando = False

    # Preenchimento da janela com a cor branca
    janela.fill(BRANCO)

    # Desenho do quadrado na janela
    pygame.draw.rect(janela, PRETO, (pos_x, pos_y, tamanho_quadrado, tamanho_quadrado))

    # Atualização da janela
    pygame.display.update()

# Encerramento do Pygame
pygame.quit()