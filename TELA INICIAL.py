import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Ana Clara')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((229, 35, 151))  # Preenche com a cor branca

    # ----- Desenha a frase
    font = pygame.font.Font(None, 70)  # Define a fonte e o tamanho
    text = font.render("PYGAME", True, (255, 255, 255))  # Renderiza o texto
    text_rect = text.get_rect(center=(window.get_width() // 2, window.get_height() // 2-50))  # Obtém o retângulo do texto
    window.blit(text, text_rect)  # Desenha o texto na tela

    font = pygame.font.Font(None, 40)  # Define a fonte e o tamanho
    texto = font.render("iniciar", True, (255, 255, 255))  # Renderiza o texto
    texto_rect = texto.get_rect(center=(window.get_width() // 2, window.get_height() // 2+50))  # Obtém o retângulo do texto
    window.blit(texto, texto_rect)  # Desenha o texto na tel

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados