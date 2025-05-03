import pygame
import sys
import random

pygame.init()

sw, sh = 800, 800
snake_size = 50
mark = pygame.font.Font(None, snake_size*2)

screen = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

class Snake():
    def __init__(self):
        self.x, self.y = snake_size, snake_size
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, snake_size, snake_size)
        self.body = [pygame.Rect(self.x-snake_size, self.y, snake_size, snake_size)]
        self.dead = False
    def update(self):
        global apple
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, sw) or self.head.y not in range(0, sh):
                self.dead = True
        if self.dead:
            self.x, self.y = snake_size, snake_size
            self.head = pygame.Rect(self.x, self.y, snake_size, snake_size)
            self.body = [pygame.Rect(self.x-snake_size, self.y, snake_size, snake_size)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir*snake_size
        self.head.y += self.ydir*snake_size
        self.body.remove(self.head)
class Apple():
    def __init__(self):
        self.x = int(random.randint(0, sw)/snake_size)*snake_size
        self.y = int(random.randint(0, sw)/snake_size)*snake_size
        self.rect = pygame.Rect(self.x, self.y, snake_size, snake_size)
    def update(self):
        pygame.draw.rect(screen, "red", self.rect) 
def drawGrid():
    for x in range(0, sw, snake_size):
        for y in range(0, sw, snake_size):
            rect= pygame.Rect(x,y, snake_size, snake_size)
            pygame.draw.rect(screen, '#3c3c3b', rect, 1)
score = mark.render('1', True, 'white')
score_rect = score.get_rect(center=(sw/2,sh/2))
drawGrid()
snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
    snake.update()
    screen.fill('black')
    apple.update()
    score = mark.render(f'{len(snake.body)+1}', True, 'white')
    pygame.draw.rect(screen, 'green', snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, 'green', square)
    screen.blit(score, score_rect)
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, snake_size, snake_size))
        apple = Apple()
    pygame.display.update()
    clock.tick(5)