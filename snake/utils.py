import random

from constants import NUM_X, NUM_Y, SQUARE_HEIGHT, SQUARE_WIDTH


def generate_position(num_x=NUM_X, num_y=NUM_Y):
    x, y = (
        random.choice(range(num_x)) * SQUARE_WIDTH,
        random.choice(range(num_y)) * SQUARE_HEIGHT,
    )
    return x, y
