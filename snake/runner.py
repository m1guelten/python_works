"""
Example file showing a basic pygame game loop
"""


import pygame

from apple import Apple
from constants import HEIGHT, START_SNAKE_X, START_SNAKE_Y, WIDTH
from snake import Snake
from snake_collision import apple_collision, wall_collision
from utils import generate_position

running = True


def game_setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    return screen, clock


def manage_keyboard(snake: Snake):
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and snake.vector != "DOWN":
                snake.vector = "UP"
            if event.key == pygame.K_DOWN and snake.vector != "UP":
                snake.vector = "DOWN"
            if event.key == pygame.K_LEFT and snake.vector != "RIGHT":
                snake.vector = "LEFT"
            if event.key == pygame.K_RIGHT and snake.vector != "LEFT":
                snake.vector = "RIGHT"


def speed_game(snake: Snake, snake_speed_limit=40):
    if len(snake.tail) == 4:
        snake_speed_limit = 30
    elif len(snake.tail) == 9:
        snake_speed_limit = 20
    elif len(snake.tail) == 19:
        snake_speed_limit = 15
    elif len(snake.tail) > 28:
        snake_speed_limit = 10
    return snake_speed_limit


def game():
    global running
    screen, clock = game_setup()
    snake = Snake((START_SNAKE_X, START_SNAKE_Y))

    apple = Apple(generate_position())

    snake_speed = 0
    snake_speed_limit = 40

    while running and snake.alive:
        manage_keyboard(snake)

        snake_speed += 1
        if apple_collision(snake, apple):  # snake.x == apple.x and snake.y == apple.y:
            snake.tail.append({"x": snake.x, "y": snake.y})
            generate = True
            ran_x, ran_y = None, None
            while generate:
                generate = False
                ran_x, ran_y = generate_position()
                for item in snake.tail:
                    if item == {"x": ran_x, "y": ran_y}:
                        generate = True
            apple = Apple((ran_x, ran_y))

        if snake_speed > snake_speed_limit:
            snake.move()
            running = wall_collision(snake)
            speed_game(snake, snake_speed_limit)
            snake_speed = 0

        screen.fill("purple")

        snake.draw(screen)
        apple.draw(screen)
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


game()
pygame.quit()
