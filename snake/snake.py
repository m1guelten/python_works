"""
This module is for Snake template class
"""

import pygame as pg

from constants import SQUARE_HEIGHT, SQUARE_WIDTH


class Snake:
    def __init__(self, koord, tail=[]):
        self.x = koord[0]
        self.y = koord[1]
        self.head = pg.Rect(self.x, self.y, SQUARE_WIDTH - 1, SQUARE_HEIGHT - 1)
        self.tail = tail
        self.alive = True
        self.vector = "RIGHT"

    def draw(self, screen):
        pg.draw.rect(screen, "green", self.head)
        if len(self.tail) > 0:
            for one_tail in self.tail:
                pg.draw.rect(
                    screen,
                    "green",
                    pg.Rect(
                        one_tail["x"],
                        one_tail["y"],
                        SQUARE_WIDTH - 1,
                        SQUARE_HEIGHT - 1,
                    ),
                )

    def _collision_myself(self) -> bool:
        for item in self.tail:
            if item["x"] == self.x and item["y"] == self.y:
                return False
                # self.alive = False
                # break
        return True

    def move(self):
        if len(self.tail) > 0:
            self.rewrite_tail()

        if self.vector == "UP":
            self.y -= SQUARE_HEIGHT

        if self.vector == "DOWN":
            self.y += SQUARE_HEIGHT

        if self.vector == "LEFT":
            self.x -= SQUARE_WIDTH

        if self.vector == "RIGHT":
            self.x += SQUARE_WIDTH
        self.alive = self._collision_myself()
        self.head = pg.Rect(self.x, self.y, SQUARE_WIDTH - 1, SQUARE_HEIGHT - 1)

    def rewrite_tail(self):
        for inx in range(0, len(self.tail)):
            if (inx + 1) == len(self.tail):
                self.tail[inx] = {"x": self.x, "y": self.y}
            else:
                self.tail[inx] = self.tail[inx + 1]
