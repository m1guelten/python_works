import pygame as pg

from constants import SQUARE_HEIGHT, SQUARE_WIDTH


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color: str = "green"
        self.size_x = SQUARE_WIDTH
        self.size_y = SQUARE_HEIGHT

    def draw(self, screen):
        pg.draw.rect(
            screen, self.color, pg.Rect(self.x, self.y, self.size_x, self.size_y)
        )
