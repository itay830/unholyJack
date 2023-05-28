import pygame

import playerClass

vector = pygame.math.Vector2

class Camera:
    def __init__(self, player: playerClass.Player):
        self.player = player
        self.offset_float = vector(0, 0)
        self.offset = vector(0, 0)
        self.CONST = vector(-1920 / 2 + player.rect.w / 2, -1080/2)

    def follow(self, borders: list[int, int, int, int]):
        self.offset_float.x += (self.player.rect.x - self.offset_float.x + self.CONST.x)
        self.offset_float.y += (self.player.rect.y - self.offset_float.y + self.CONST.y)
        self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)
        self.offset.x = max(borders[0], self.offset.x)
        self.offset.x = min(self.offset.x, borders[1])

        self.offset.y = min(self.offset.y, borders[3])
        self.offset.y = max(self.offset.y, borders[2])

