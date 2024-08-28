import random

import pygame

WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Snake and food
BLOCK_SIZE = 20
SNAKE_SPEED = 15


def control_snake(key, x_change, y_change):
    if key == pygame.K_LEFT:
        x_change = -BLOCK_SIZE
        y_change = 0
    if key == pygame.K_RIGHT:
        x_change = BLOCK_SIZE
        y_change = 0
    if key == pygame.K_UP:
        x_change = 0
        y_change = -BLOCK_SIZE
    if key == pygame.K_DOWN:
        x_change = 0
        y_change = BLOCK_SIZE
    return x_change, y_change


def control_snake_wasd(key, x_change, y_change):
    if key == pygame.K_a:
        x_change = -BLOCK_SIZE
        y_change = 0
    if key == pygame.K_d:
        x_change = BLOCK_SIZE
        y_change = 0
    if key == pygame.K_w:
        x_change = 0
        y_change = -BLOCK_SIZE
    if key == pygame.K_s:
        x_change = 0
        y_change = BLOCK_SIZE
    return x_change, y_change


def draw_snake(snake_list, color):
    for body in snake_list:
        pygame.draw.rect(window, color, [body[0], body[1], BLOCK_SIZE, BLOCK_SIZE])


def draw_food(food_x, food_y):
    pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])


def run_game():
    clock = pygame.time.Clock()
    game_over = False

    # Snake 1 initial position and movement
    snake1_x = WIDTH / 2
    snake1_y = HEIGHT / 2
    x_change1 = 0  # Start moving right by default
    y_change1 = 0
    snake_list1 = []
    length_of_snake1 = 1

    # Snake 2 initial position and movement
    snake2_x = WIDTH / 2 + 120
    snake2_y = WIDTH / 2 + 120
    x_change2 = 0  # Start moving right by default
    y_change2 = 0
    snake_list2 = []
    length_of_snake2 = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Bye bye!")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                x_change1, y_change1 = control_snake(event.key, x_change1, y_change1)
                x_change2, y_change2 = control_snake_wasd(event.key, x_change2, y_change2)

        # Move Snake 1
        snake1_x += x_change1
        snake1_y += y_change1
        snake_head1 = [snake1_x, snake1_y]
        snake_list1.append(snake_head1)
        snake_list1 = snake_list1[-length_of_snake1:]

        # Move Snake 2
        snake2_x += x_change2
        snake2_y += y_change2
        snake_head2 = [snake2_x, snake2_y]
        snake_list2.append(snake_head2)
        snake_list2 = snake_list2[-length_of_snake2:]

        # Check for game over conditions
        if snake1_x >= WIDTH or snake1_x < 0 or snake1_y >= HEIGHT or snake1_y < 0:
            game_over = True
            print("Snake 1 game over ...")
        if snake2_x >= WIDTH or snake2_x < 0 or snake2_y >= HEIGHT or snake2_y < 0:
            game_over = True
            print("Snake 2 game over ...")
        for snake_body in snake_list1[:-1]:
            if snake_body == snake_head1:
                game_over = True
                print("Snake 1 game over ...")
        for snake_body in snake_list2[:-1]:
            if snake_body == snake_head2:
                game_over = True
                print("Snake 2 game over ...")

        # Update screen
        window.fill(BLACK)
        draw_food(food_x, food_y)
        draw_snake(snake_list1, GREEN)
        draw_snake(snake_list2, YELLOW)
        pygame.display.update()

        # Snake 1 eats food
        if snake1_x == food_x and snake1_y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake1 += 1

        # Snake 2 eats food
        if snake2_x == food_x and snake2_y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake2 += 1

        clock.tick(SNAKE_SPEED)


def game_over():
    game_start = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye bye!")
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Bye bye!")
                pygame.quit()
                quit()
            if event.key == pygame.K_c:
                game_start = True
    return game_start


if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    game_start = True
    while True:
        if game_start:
            run_game()
        game_start = game_over()
