import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
snake_block = 20
snake_speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)


def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])


def message(msg, color, y_offset=0):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3 + y_offset])


def game_loop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)

        score = font.render(f"Score: {snake_length - 1}", True, WHITE)
        screen.blit(score, [10, 10])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start game
game_loop()
