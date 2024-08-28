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


class Snake:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.color = color
        self.x_change = 0
        self.y_change = 0
        self.body = []
        self.length = 1
        self.controls = controls
        self.score = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.body.append([self.x, self.y])
        self.body = self.body[-self.length :]

    def control(self, key):
        if key == self.controls["LEFT"]:
            self.x_change = -BLOCK_SIZE
            self.y_change = 0
        elif key == self.controls["RIGHT"]:
            self.x_change = BLOCK_SIZE
            self.y_change = 0
        elif key == self.controls["UP"]:
            self.x_change = 0
            self.y_change = -BLOCK_SIZE
        elif key == self.controls["DOWN"]:
            self.x_change = 0
            self.y_change = BLOCK_SIZE

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, self.color, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

    def check_collision(self):
        if self.x >= WIDTH or self.x < 0 or self.y >= HEIGHT or self.y < 0 or [self.x, self.y] in self.body[:-1]:
            return True
        return False

    def eat_food(self, food):
        if self.x == food[0] and self.y == food[1]:
            self.length += 1
            self.score += 1
            return True
        return False


def draw_food(window, food_x, food_y):
    pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])


def display_message(window, message, color, y_displacement=0):
    font = pygame.font.SysFont(None, 50)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_displacement))
    window.blit(text, text_rect)


def game_over_screen(window, snake1, snake2):
    window.fill(BLACK)
    display_message(window, "Game Over!", RED, -50)
    display_message(window, f"Snake 1 Score: {snake1.score}", GREEN, 0)
    display_message(window, f"Snake 2 Score: {snake2.score}", YELLOW, 50)
    display_message(window, "Press C to play again or Q to quit", WHITE, 100)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    return True
    return False


def run_game(window):
    clock = pygame.time.Clock()
    game_over = False

    snake1 = Snake(
        WIDTH / 2,
        HEIGHT / 2,
        GREEN,
        {"LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT, "UP": pygame.K_UP, "DOWN": pygame.K_DOWN},
    )

    snake2 = Snake(
        WIDTH / 2 + 120,
        HEIGHT / 2 + 120,
        YELLOW,
        {"LEFT": pygame.K_a, "RIGHT": pygame.K_d, "UP": pygame.K_w, "DOWN": pygame.K_s},
    )

    food = [
        round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE,
        round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE,
    ]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                snake1.control(event.key)
                snake2.control(event.key)

        snake1.move()
        snake2.move()

        if snake1.check_collision() or snake2.check_collision():
            game_over = True

        window.fill(BLACK)
        draw_food(window, food[0], food[1])
        snake1.draw(window)
        snake2.draw(window)
        pygame.display.update()

        if snake1.eat_food(food) or snake2.eat_food(food):
            food = [
                round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE,
                round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE,
            ]

        clock.tick(SNAKE_SPEED)

    return game_over_screen(window, snake1, snake2)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    while True:
        if not run_game(window):
            break

    pygame.quit()
