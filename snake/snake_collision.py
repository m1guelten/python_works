from apple import Apple
from constants import HEIGHT, WIDTH
from snake import Snake


def wall_collision(snake: Snake) -> bool:
    x, y = snake.head.x, snake.head.y
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        return False
    return True


def apple_collision(snake: Snake, apple: Apple) -> bool:
    snake_x, snake_y = snake.head.x, snake.head.y
    apple_x, apple_y = apple.x, apple.y
    if snake_x == apple_x and snake_y == apple_y:
        return True
    return False
