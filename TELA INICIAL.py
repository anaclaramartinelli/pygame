# ----- Importa e inicia pacotes
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
    
    # ----- Desenha o quadrado branco
    cor_quadrado = (255, 255, 255)  # Cor do quadrado branco
    tamanho_quadrado = 150  # Tamanho do quadrado branco
    x_quadrado = window.get_width() // 2 - tamanho_quadrado // 2  # Posição X para centralizar o quadrado branco
    y_quadrado = window.get_height() // 2 - tamanho_quadrado // 2  # Posição Y para centralizar o quadrado branco
    
    pygame.draw.rect(window, cor_quadrado, pygame.Rect(x_quadrado, y_quadrado, tamanho_quadrado, tamanho_quadrado))
    
    # ----- Desenha o triângulo preto
    cor_triangulo = (0, 0, 0)  # Cor preta para o triângulo
    tamanho_triangulo = 100  # Tamanho do triângulo
    x_triangulo = window.get_width() // 2 - tamanho_triangulo // 2  # Posição X para centralizar o triângulo
    y_triangulo = y_quadrado + tamanho_quadrado // 2  # Posição Y abaixo do quadrado branco
    
    pygame.draw.polygon(window, cor_triangulo, [(x_triangulo, y_triangulo + tamanho_triangulo), (x_triangulo, y_triangulo), (x_triangulo + tamanho_triangulo, y_triangulo + tamanho_triangulo // 2)])
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
