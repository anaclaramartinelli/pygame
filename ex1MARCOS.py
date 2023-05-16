# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Jogo do Marcos')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key != pygame.K_ESCAPE):
            game = False

    # ----- Gera saídas
    window.fill((0, 100, 250))  # Preenche com a cor azul

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
