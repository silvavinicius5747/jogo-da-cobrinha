import pygame
import random

# Configurações do jogo
WIDTH = 800
HEIGHT = 600
FPS = 30

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inicialização do Pygame
pygame.init()

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobra")

# Cria um relógio para controlar a taxa de atualização da tela
clock = pygame.time.Clock()
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 1
        self.vy = 0
        self.body = [(self.x, self.y)]
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.body.insert(0, (self.x, self.y))
        self.body.pop()
        
    def draw(self, surface):
        for x, y in self.body:
            rect = pygame.Rect(x*20, y*20, 20, 20)
            pygame.draw.rect(surface, GREEN, rect)

class Coin:
    def __init__(self):
        self.x = random.randint(0, WIDTH//20-1)
        self.y = random.randint(0, HEIGHT//20-1)
        
    def draw(self, surface):
        rect = pygame.Rect(self.x*20, self.y*20, 20, 20)
        pygame.draw.rect(surface, BLUE, rect)
# Loop principal do jogo
game_over = False
while not game_over:
    # Processamento de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.vx = -1
                snake.vy = 0
            elif event.key == pygame.K_RIGHT:
                snake.vx = 1
                snake.vy = 0
            elif event.key == pygame.K_UP:
                snake.vx = 0
                snake.vy = -1
            elif event.key == pygame.K_DOWN:
                snake.vx = 0
                snake.vy = 1

    # Atualização dos objetos
    snake.update()
    
    # Detecção de colisão
    if snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH//20 or snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT//20:
        game_over = True
    
    for i in range(1, len(snake.body)):
        if snake.body[0] == snake.body[i]:
            game_over = True
    
    if snake.body[0] == (coin.x, coin.y):
        coin = Coin()
        snake.body.append(snake.body[-1])
    
    # Renderização do jogo
    screen.fill(BLACK)
    snake.draw(screen)
    coin.draw(screen)
    pygame.display.flip()
    
    # Controle de FPS
    clock.tick(FPS)

# Encerramento do pygame
pygame.quit()
