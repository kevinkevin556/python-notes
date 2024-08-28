import pygame
import random


WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
Yellow = (217,210,85)
Purple = (197, 5, 220)

# Snake and food
BLOCK_SIZE = 20
SNAKE_SPEED = 15 


def control_snake(event,old_x_change,old_y_change):
    x_change = old_x_change
    y_change = old_y_change
    if event.type == pygame.KEYDOWN:   
        if event.key in [pygame.K_LEFT,pygame.K_a] and  old_x_change != BLOCK_SIZE:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                    print("left")
        if event.key in [pygame.K_RIGHT,pygame.K_d] and  old_x_change != -BLOCK_SIZE:
                    x_change = BLOCK_SIZE
                    y_change = 0
                    print("right")
        if event.key in [pygame.K_UP,pygame.K_w] and  old_y_change != BLOCK_SIZE:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                    print("up")
        if event.key in [pygame.K_DOWN,pygame.K_s] and  old_y_change != -BLOCK_SIZE:
                    y_change = BLOCK_SIZE
                    x_change = 0
                    print("down")
    return x_change, y_change

def draw_snake(snake_list):
    for body in snake_list:
        pygame.draw.rect(window, Yellow, (body[0], body[1], BLOCK_SIZE, BLOCK_SIZE))


def draw_food(food_x, food_y):
    pygame.draw.rect(window, Purple, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

def draw_boom(boom_x, boom_y):
    pygame.draw.rect(window, RED, (boom_x, boom_y, 4*BLOCK_SIZE, 4*BLOCK_SIZE))

def run_game():
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)
    game_over = False

    # 起始位置、起始速度
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2
    x_change = 0
    y_change = 0

    # 蛇身資訊
    snake_list = []
    length_of_snake = 1

    # 食物位置
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    #炸彈位置
    boom_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    boom_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
    
    while not game_over:
        # 接收使用者輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Bye bye!")
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                x_change, y_change = control_snake(event,x_change,y_change)
                if event.key == pygame.K_r:
                     return
        SNAKE_SPEED = 15 + (length_of_snake-1)*0.75
        # 蛇體移動、更新蛇身
        snake_x += x_change
        snake_y += y_change

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        snake_list = snake_list[-length_of_snake:]

        # GG 條件
        if snake_x == 0 or snake_x == WIDTH-BLOCK_SIZE or snake_y == 0 or snake_y == HEIGHT-BLOCK_SIZE:
            game_over = True
            print("game over ...")
        for x in range(0,length_of_snake-1):
            if snake_head == snake_list[x]:
                game_over = True
                print("game over ...")

        # 更新畫面
        window.fill(WHITE)
        draw_food(food_x, food_y)
        draw_boom(boom_x,boom_y)
        draw_snake(snake_list)
        mesg = font.render(str((len(snake_list) - 1) * 100), True, BLACK)
        window.blit(mesg , [WIDTH -70, HEIGHT -30])
        pygame.display.update()
    

        # 進食條件
        if snake_x == food_x and snake_y == food_y:
             food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
             food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
             length_of_snake += 1
        #吃到炸彈
        if snake_x == boom_x and snake_y == boom_y:
            game_over = True
            print("game over ...")
        clock.tick(SNAKE_SPEED)



def game_over():
    game_start = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye bye!")
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                print("Bye bye!")
                pygame.quit()
                quit()
            if event.key == pygame.K_r:
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
        # Run Game
        if game_start:
            run_game()
        # After Game
        game_start = game_over()

