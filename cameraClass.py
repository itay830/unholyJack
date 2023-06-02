import pygame

import playerClass

vec = pygame.math.Vector2

class Camera:
    def __init__(self, camera_size: tuple[int, int]):
        self.offset = vec()
        self.WIDTH, self.HEIGHT = camera_size

        self.camera_center = vec(self.WIDTH//2, self.HEIGHT//2)

    def calc_offset(self, target: pygame.Rect):
        self.offset.x, self.offset.y = target.centerx - self.camera_center.x, target.centery - self.camera_center.y


    '''def follow(self, borders: list[int, int, int, int]):
        self.offset_float.x += self.player.rect.x - self.offset_float.x + self.CONST.x
        self.offset_float.y += self.player.rect.y - self.offset_float.y + self.CONST.y
        print(self.offset.x, self.offset.y)
        self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)

        self.offset.x = max(self.offset.x, borders[0])
        self.offset.x = min(self.offset.x, borders[1])

        self.offset.y = max(self.offset.y, borders[2])
        self.offset.y = min(self.offset.y, borders[3])'''

        #self.offset.x = max(-(self.W))



