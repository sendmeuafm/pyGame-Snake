import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red   = (255,0,0)
width, height = 640, 480
cell_size = 20


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The snake")
snake = [(100,100),(90,100),(80,100)]
snake_direction = (cell_size,0)

food =(width//2,height//2)
score = 0
clock = pygame.time.Clock()


def draw_snake(l_snake):
    for i in l_snake :
        pygame.draw.rect(screen, green, (i[0],i[1],cell_size, cell_size))

def draw_food(food):
    pygame.draw.rect(screen,red,(food[0],food[1], cell_size, cell_size))

while  True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(f"{event}")
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            print(f"{keys}")

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            elif keys[pygame.K_UP] and snake_direction != (0, cell_size):
                snake_direction = (0,-cell_size)
            elif keys[pygame.K_DOWN] and snake_direction != (0, -cell_size):
                snake_direction = (0,cell_size)
            elif keys[pygame.K_LEFT] and snake_direction != (cell_size,0):
                snake_direction = (-cell_size,0)
            elif keys[pygame.K_RIGHT] and snake_direction != (-cell_size,0):
                snake_direction = (cell_size,0)

    new_head = (int(snake[0][0]+snake_direction[0]), int(snake[0][1]+snake_direction[1]))
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (  random.randint(0, ((width-cell_size)//cell_size))*cell_size,
                  random.randint(0,((height-cell_size)//cell_size))*cell_size
        )
    else:
        snake.pop()

    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= width or new_head[1] >= height:
        pygame.quit()

    screen.fill(black)
    draw_snake(snake)
    draw_food(food)

    pygame.display.flip()
    clock.tick(10+score)